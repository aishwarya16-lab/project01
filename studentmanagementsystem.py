import json

class Student:
    def __init__(self, student_id, name, grade_level):
        self.student_id = student_id
        self.name = name
        self.grade_level = grade_level
        self.attendance = []
        self.grades = {}
        self.messages = []

    def mark_attendance(self, date, present=True):
        self.attendance.append({'date': date, 'present': present})

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def receive_message(self, message):
        self.messages.append(message)

    def to_dict(self):
        return {
            'student_id': self.student_id,
            'name': self.name,
            'grade_level': self.grade_level,
            'attendance': self.attendance,
            'grades': self.grades,
            'messages': self.messages
        }

    @staticmethod
    def from_dict(data):
        student = Student(data['student_id'], data['name'], data['grade_level'])
        student.attendance = data.get('attendance', [])
        student.grades = data.get('grades', {})
        student.messages = data.get('messages', [])
        return student

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Grade Level: {self.grade_level}"

class Teacher:
    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name
        self.messages = []

    def send_message(self, student, message):
        student.receive_message(f"From {self.name}: {message}")

    def to_dict(self):
        return {
            'teacher_id': self.teacher_id,
            'name': self.name,
            'messages': self.messages
        }

    @staticmethod
    def from_dict(data):
        teacher = Teacher(data['teacher_id'], data['name'])
        teacher.messages = data.get('messages', [])
        return teacher

    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}"

class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.teachers = {}

    def enroll_student(self, student_id, name, grade_level):
        if student_id in self.students:
            print(f"Student with ID {student_id} already enrolled.")
        else:
            self.students[student_id] = Student(student_id, name, grade_level)
            print(f"Enrolled student {name} with ID {student_id}.")

    def add_teacher(self, teacher_id, name):
        if teacher_id in self.teachers:
            print(f"Teacher with ID {teacher_id} already exists.")
        else:
            self.teachers[teacher_id] = Teacher(teacher_id, name)
            print(f"Added teacher {name} with ID {teacher_id}.")

    def mark_attendance(self, student_id, date, present=True):
        if student_id in self.students:
            self.students[student_id].mark_attendance(date, present)
            print(f"Marked attendance for student ID {student_id} on {date}: {'Present' if present else 'Absent'}.")
        else:
            print(f"Student ID {student_id} not found.")

    def add_grade(self, student_id, subject, grade):
        if student_id in self.students:
            self.students[student_id].add_grade(subject, grade)
            print(f"Added grade for student ID {student_id} in {subject}: {grade}.")
        else:
            print(f"Student ID {student_id} not found.")

    def send_message(self, teacher_id, student_id, message):
        if teacher_id in self.teachers and student_id in self.students:
            self.teachers[teacher_id].send_message(self.students[student_id], message)
            print(f"Message sent from teacher ID {teacher_id} to student ID {student_id}.")
        else:
            print("Teacher or student ID not found.")

    def get_student_info(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            info = str(student) + "\\n"
            info += "Attendance:\\n"
            for record in student.attendance:
                info += f"  Date: {record['date']}, Present: {record['present']}\\n"
            info += "Grades:\\n"
            for subject, grade in student.grades.items():
                info += f"  {subject}: {grade}\\n"
            info += "Messages:\\n"
            for msg in student.messages:
                info += f"  {msg}\\n"
            return info
        else:
            return f"Student ID {student_id} not found."

def main():
    sms = StudentManagementSystem()

    # Example usage
    sms.enroll_student("S001", "Alice Johnson", "10th Grade")
    sms.enroll_student("S002", "Bob Smith", "11th Grade")

    sms.add_teacher("T001", "Mrs. Thompson")

    sms.mark_attendance("S001", "2024-06-01", True)
    sms.mark_attendance("S002", "2024-06-01", False)

    sms.add_grade("S001", "Math", "A")
    sms.add_grade("S002", "Science", "B+")

    sms.send_message("T001", "S001", "Please see me after class.")

    print(sms.get_student_info("S001"))

if __name__ == "__main__":
    main()
