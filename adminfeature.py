students = {}

def add_student():
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    if id in students:
        print("Student ID already exists!")
    else:
        students[id] = name
        print("Student added successfully!")

def view_students():
    print("\nStudent Profiles:")
    if not students:
        print("No students found.")
    else:
        for id, name in students.items():
            print(f"ID: {id}, Name: {name}")

def delete_student():
    id = input("Enter the student ID to delete: ")
    if id in students:
        del students[id]
        print("Student deleted successfully!")
    else:
        print("Student not found.")