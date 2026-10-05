# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 17:45:04 2024

@author: José Alberto Rocha Munguía
"""

"""
In-memory student list CRUD + average (DSA coursework).

Quick test:
  python3 student_management.py
  Expect several Name/Grade lines and average updates after add/modify/delete.
"""

students = []


def add_student(name, grade):
    students.append({"name": name, "grade": grade})


def modify_grades(name, new_grade):
    for student in students:
        if student["name"] == name:
            student["grade"] = new_grade


def delete_student(name):
    global students
    students = [s for s in students if s["name"] != name]


def show_students():
    for student in students:
        print(f"Name: {student['name']}, Grade: {student['grade']}")


def calculate_average():
    if not students:
        print("No students in the list.")
        return
    total_grades = sum(s["grade"] for s in students)
    average = total_grades / len(students)
    print(f"Average grade = {average}")


add_student("Putin", 10)
add_student("Trump", 6)
add_student("Peña", 3)
modify_grades("Peña", 7)
show_students()
calculate_average()
delete_student("Trump")
show_students()
add_student("Biden", 7)
calculate_average()
delete_student("Peña")
show_students()
add_student("Amlo", 8)
calculate_average()
show_students()
calculate_average()

