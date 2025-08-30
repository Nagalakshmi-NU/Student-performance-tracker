from db import db

class StudentModel(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    roll_number = db.Column(db.String(50), unique=True, nullable=False)
    grades = db.relationship("GradeModel", backref="student", cascade="all, delete-orphan")

class GradeModel(db.Model):
    __tablename__ = "grades"
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(80), nullable=False)
    score = db.Column(db.Float, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
