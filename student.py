class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"{self.name}, {self.roll_number}, CGPA: {self.cgpa}"

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:
students = [
    Student("Alice", "101", 3.9),
    Student("Bob", "102", 3.7),
    Student("Charlie", "103", 3.8),
    Student("David", "104", 3.6),
]

sorted_students = sort_students(students)
for student in sorted_students:
    print(student)
