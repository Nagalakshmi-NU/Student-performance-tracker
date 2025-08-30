from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from sqlalchemy.exc import IntegrityError
from db import db
from models import StudentModel, GradeModel

@dataclass
class Student:
    name: str
    roll_number: str
    grades: Dict[str, float] = field(default_factory=dict)

    def add_grade(self, subject: str, score: float):
        self.grades[subject] = score

    def average(self) -> Optional[float]:
        if not self.grades:
            return None
        return sum(self.grades.values()) / len(self.grades)

class StudentTracker:
    @staticmethod
    def add_student(name: str, roll_number: str) -> bool:
        if not name.strip() or not roll_number.strip():
            raise ValueError("Name and roll number are required.")
        student = StudentModel(name=name.strip(), roll_number=roll_number.strip())
        db.session.add(student)
        try:
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False

    @staticmethod
    def add_grade(roll_number: str, subject: str, score: float) -> bool:
        if subject is None or subject.strip() == "":
            raise ValueError("Subject is required.")
        try:
            score = float(score)
        except (TypeError, ValueError):
            raise ValueError("Score must be a number.")
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100.")
        student = StudentModel.query.filter_by(roll_number=roll_number).first()
        if not student:
            return False
        grade = GradeModel.query.filter_by(student_id=student.id, subject=subject.strip()).first()
        if grade:
            grade.score = score
        else:
            grade = GradeModel(subject=subject.strip(), score=score, student_id=student.id)
            db.session.add(grade)
        db.session.commit()
        return True

    @staticmethod
    def list_students() -> List[Student]:
        out = []
        for st in StudentModel.query.order_by(StudentModel.roll_number).all():
            grades = {g.subject: g.score for g in st.grades}
            out.append(Student(name=st.name, roll_number=st.roll_number, grades=grades))
        return out

    @staticmethod
    def get_student(roll_number: str) -> Optional[Student]:
        student = StudentModel.query.filter_by(roll_number=roll_number).first()
        if not student:
            return None
        s = Student(name=student.name, roll_number=student.roll_number)
        for g in student.grades:
            s.add_grade(g.subject, g.score)
        return s

    @staticmethod
    def calculate_average(roll_number: str) -> Optional[float]:
        s = StudentTracker.get_student(roll_number)
        return s.average() if s else None

    @staticmethod
    def subject_topper(subject: str) -> Optional[Tuple[str, str, float]]:
        q = (
            db.session.query(StudentModel.name, StudentModel.roll_number, GradeModel.score)
            .join(GradeModel, GradeModel.student_id == StudentModel.id)
            .filter(GradeModel.subject == subject)
            .order_by(GradeModel.score.desc(), StudentModel.name.asc())
        )
        top = q.first()
        if top:
            return (top.name, top.roll_number, top.score)
        return None

    @staticmethod
    def class_average(subject: str) -> Optional[float]:
        from sqlalchemy import func
        avg = (
            db.session.query(func.avg(GradeModel.score))
            .filter(GradeModel.subject == subject)
            .scalar()
        )
        return float(avg) if avg is not None else None

    @staticmethod
    def overall_topper() -> Optional[Student]:
        students = StudentTracker.list_students()
        if not students:
            return None
        topper = max(students, key=lambda s: s.average() or 0)
        return topper if topper.average() is not None else None

    @staticmethod
    def delete_student(roll_number: str) -> bool:
        student = StudentModel.query.filter_by(roll_number=roll_number).first()
        if not student:
            return False
        db.session.delete(student)
        db.session.commit()
        return True

    @staticmethod
    def update_student_name(roll_number: str, name: str) -> bool:
        student = StudentModel.query.filter_by(roll_number=roll_number).first()
        if not student:
            return False
        student.name = name.strip()
        db.session.commit()
        return True

    @staticmethod
    def export_to_csv(filepath: str = "students_export.csv") -> str:
        import csv
        students = StudentTracker.list_students()
        with open(filepath, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Roll Number", "Subject", "Score"])
            for s in students:
                if s.grades:
                    for subject, score in s.grades.items():
                        writer.writerow([s.name, s.roll_number, subject, score])
                else:
                    writer.writerow([s.name, s.roll_number, "", ""])
        return filepath
