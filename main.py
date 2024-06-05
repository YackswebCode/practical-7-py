import flet as ft


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.subjects = {}

    def add_subject(self, subject, score):
        self.subjects[subject] = score

    def calculate_grade(self):
        total_score = sum(self.subjects.values())
        average_score = total_score / len(self.subjects)
        if average_score >= 90:
            return 'A'
        elif average_score >= 80:
            return 'B'
        elif average_score >= 70:
            return 'C'
        elif average_score >= 60:
            return 'D'
        else:
            return 'F'

    def generate_report(self):
        report = f"Report for {self.name} (ID: {self.student_id})\n"
        report += "Subject Scores:\n"
        for subject, score in self.subjects.items():
            report += f"  {subject}: {score}\n"
        report += f"Overall Grade: {self.calculate_grade()}\n"
        return report


class School:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
        else:
            print(f"Student with ID {student_id} already exists.")

    def add_score(self, student_id, subject, score):
        if student_id in self.students:
            self.students[student_id].add_subject(subject, score)
        else:
            print(f"No student found with ID {student_id}.")

    def generate_student_report(self, student_id):
        if student_id in self.students:
            return self.students[student_id].generate_report()
        else:
            return f"No student found with ID {student_id}."

    def generate_all_reports(self):
        reports = ""
        for student_id in self.students:
            reports += self.students[student_id].generate_report() + "\n"
        return reports


def main(page: ft.Page):
    school = School()

    def add_student(e):
        student_id = student_id_input.value
        name = name_input.value
        school.add_student(student_id, name)
        output_area.controls.append(ft.Text(f"Student {name} with ID {student_id} added."))
        student_id_input.value = ""
        name_input.value = ""
        page.update()

    def add_score(e):
        student_id = score_student_id_input.value
        subject = subject_input.value
        score = float(score_input.value)
        school.add_score(student_id, subject, score)
        output_area.controls.append(ft.Text(f"Score {score} for subject {subject} added for student ID {student_id}."))
        score_student_id_input.value = ""
        subject_input.value = ""
        score_input.value = ""
        page.update()

    def generate_report(e):
        student_id = report_student_id_input.value
        report = school.generate_student_report(student_id)
        output_area.controls.append(ft.Text(report))
        report_student_id_input.value = ""
        page.update()

    def generate_all_reports(e):
        reports = school.generate_all_reports()
        output_area.controls.append(ft.Text(reports))
        page.update()

    student_id_input = ft.TextField(label="Student ID")
    name_input = ft.TextField(label="Student Name")
    add_student_button = ft.ElevatedButton(text="Add Student", on_click=add_student)

    score_student_id_input = ft.TextField(label="Student ID")
    subject_input = ft.TextField(label="Subject")
    score_input = ft.TextField(label="Score", keyboard_type=ft.KeyboardType.NUMBER)
    add_score_button = ft.ElevatedButton(text="Add Score", on_click=add_score)

    report_student_id_input = ft.TextField(label="Student ID")
    generate_report_button = ft.ElevatedButton(text="Generate Report", on_click=generate_report)
    generate_all_reports_button = ft.ElevatedButton(text="Generate All Reports", on_click=generate_all_reports)

    output_area = ft.Column()

    page.add(
        ft.Column([
            ft.Row([student_id_input, name_input, add_student_button]),
            ft.Row([score_student_id_input, subject_input, score_input, add_score_button]),
            ft.Row([report_student_id_input, generate_report_button, generate_all_reports_button]),
            output_area
        ])
    )


ft.app(target=main)
