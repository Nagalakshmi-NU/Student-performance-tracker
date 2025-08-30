from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from db import init_db
from tracker import StudentTracker
from models import StudentModel, GradeModel
from db import db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret-key'
    init_db(app)

    @app.route('/')
    def index():
        return render_template('home.html')

    @app.route('/students')
    def list_students():
        students = StudentTracker.list_students()
        return render_template('list_students.html', students=students)

    @app.route('/students/add', methods=['GET', 'POST'])
    def add_student():
        if request.method == 'POST':
            name = request.form.get('name', '').strip()
            roll = request.form.get('roll_number', '').strip()
            subjects = request.form.getlist('subject[]')
            scores = request.form.getlist('marks[]')
            try:
                ok = StudentTracker.add_student(name, roll)
            except ValueError as e:
                flash(str(e), 'danger')
                return render_template('add_student.html')
            if not ok:
                flash('Roll number already exists.', 'danger')
                return render_template('add_student.html')
            # Add grades
            for i in range(len(subjects)):
                sub = subjects[i].strip() if i < len(subjects) else ''
                sc = scores[i].strip() if i < len(scores) else ''
                if sub and sc != '':
                    try:
                        StudentTracker.add_grade(roll, sub, float(sc))
                    except ValueError as e:
                        flash(f'Grade error: {e}', 'danger')
            flash('Student added successfully!', 'success')
            return redirect(url_for('list_students'))
        return render_template('add_student.html')

    @app.route('/students/<roll_number>')
    def view_student(roll_number):
        s = StudentTracker.get_student(roll_number)
        if not s:
            flash('Student not found.', 'warning')
            return redirect(url_for('list_students'))
        avg = s.average()
        return render_template('view_student.html', student=s, average=avg)

    @app.route('/grades/add', methods=['GET', 'POST'])
    def add_grade():
        if request.method == 'POST':
            roll = request.form.get('roll_number', '').strip()
            subject = request.form.get('subject', '').strip()
            score = request.form.get('score', '').strip()
            try:
                ok = StudentTracker.add_grade(roll, subject, float(score))
            except ValueError as e:
                flash(str(e), 'danger')
                return render_template('add_grade.html')
            if ok:
                flash('Grade saved!', 'success')
                return redirect(url_for('view_student', roll_number=roll))
            else:
                flash('Student not found. Please check the roll number.', 'danger')
        # Provide list of students for dropdown
        students = StudentModel.query.order_by(StudentModel.roll_number).all()
        return render_template('add_grade.html', students=students)

    @app.route('/stats/topper', methods=['GET', 'POST'])
    def subject_topper():
        result = None
        subject = None
        if request.method == 'POST':
            subject = request.form.get('subject', '').strip()
            result = StudentTracker.subject_topper(subject)
            if result is None:
                flash('No grades found for that subject.', 'info')
        return render_template('subject_topper.html', result=result, subject=subject)

    @app.route('/stats/class-average', methods=['GET', 'POST'])
    def class_average():
        avg = None
        subject = None
        if request.method == 'POST':
            subject = request.form.get('subject', '').strip()
            avg = StudentTracker.class_average(subject)
            if avg is None:
                flash('No grades found for that subject.', 'info')
        return render_template('class_average.html', average=avg, subject=subject)

    @app.route('/overall_topper')
    def overall_topper():
        topper = StudentTracker.overall_topper()
        return render_template('overall_topper.html', topper=topper)

    @app.route('/students/delete/<roll_number>', methods=['POST'])
    def delete_student(roll_number):
        if StudentTracker.delete_student(roll_number):
            flash('Student deleted successfully.', 'success')
        else:
            flash('Student not found.', 'danger')
        return redirect(url_for('list_students'))

    @app.route('/students/edit/<roll_number>', methods=['GET', 'POST'])
    def edit_student(roll_number):
        s = StudentTracker.get_student(roll_number)
        if not s:
            flash('Student not found.', 'warning')
            return redirect(url_for('list_students'))
        if request.method == 'POST':
            name = request.form.get('name', '').strip()
            subjects = request.form.getlist('subject[]')
            scores = request.form.getlist('marks[]')
            # update name
            StudentTracker.update_student_name(roll_number, name)
            # delete existing grades and re-add
            student_row = StudentModel.query.filter_by(roll_number=roll_number).first()
            GradeModel.query.filter_by(student_id=student_row.id).delete()
            db.session.commit()
            for i in range(len(subjects)):
                sub = subjects[i].strip() if i < len(subjects) else ''
                sc = scores[i].strip() if i < len(scores) else ''
                if sub and sc != '':
                    try:
                        StudentTracker.add_grade(roll_number, sub, float(sc))
                    except ValueError as e:
                        flash(f'Grade error: {e}', 'danger')
            flash('Student updated successfully.', 'success')
            return redirect(url_for('list_students'))
        return render_template('edit_student.html', student=s)

    @app.route('/search', methods=['GET', 'POST'])
    def search():
        student = None
        if request.method == 'POST':
            roll = request.form.get('roll_number', '').strip()
            student = StudentTracker.get_student(roll)
            if not student:
                flash('Student not found.', 'info')
        return render_template('search.html', student=student)

    @app.route('/export_csv')
    def export_csv():
        path = StudentTracker.export_to_csv()
        return send_file(path, as_attachment=True)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
