import json

# users dictionary for login
users = {"admin": "admin123", "student1": "pass123"}

# Function to load data from file 
def load_data_from_file(filename="students.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No data file found. Starting with an empty database.")
        return {}

# Function to save data from file
def save_data_to_file(data, filename="students.json"):
    with open(filename, "w") as file:
        json.dump(data, file)
        print("Data saved successfully!")

# Function to handle user login
def login(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None

# Function to add a student 
def add_student():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    if student_id in students:
        print("Student ID already exists!")
    else:
        students[student_id] = student_name
        print("Student added successfully!")

# Function to view all students
def view_students():
    if not students:
        print("No students found.")
    else:
        print("\nStudent List:")
        for student_id, student_name in students.items():
            print(f"ID: {student_id}, Name: {student_name}")

# Function to delete a student
def delete_student():
    student_id = input("Enter the student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

# Function to view a student's profile
def view_profile(username):
    if username in students:
        print(f"\nYour Profile:\nID: {username}, Name: {students[username]}")
    else:
        print("Profile not found.")

# load students data from file 
students = load_data_from_file()

# Main program flow
username = login(users)

if username:
    if username == "admin":
        while True:
            print("\nAdmin Menu:")
            print("1. Add Student")
            print("2. View Students")
            print("3. Delete Student")
            print("4. Save and Exit")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                add_student()
            elif choice == "2":
                view_students()
            elif choice == "3":
                delete_student()
            elif choice == "4":
                save_data_to_file(students)
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        while True:
            print("\nStudent Menu:")
            print("1. View Profile")
            print("2. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                view_profile(username)
            elif choice == "2":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")