import csv
import os

FILE_NAME = "students.csv"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Roll No", "Name", "Course", "Marks"])

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, course, marks])
    print("✅ Student added successfully")

def view_students():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def search_student():
    roll = input("Enter Roll No to search: ")
    found = False
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == roll:
                print("🎯 Student Found:", row)
                found = True
                break
    if not found:
        print("❌ Student not found")

def update_student():
    roll = input("Enter Roll No to update: ")
    rows = []
    updated = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row and row[0] == roll:
                name = input("Enter New Name: ")
                course = input("Enter New Course: ")
                marks = input("Enter New Marks: ")
                writer.writerow([roll, name, course, marks])
                updated = True
            else:
                writer.writerow(row)

    if updated:
        print("✅ Student updated")
    else:
        print("❌ Student not found")

def delete_student():
    roll = input("Enter Roll No to delete: ")
    rows = []
    deleted = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row and row[0] == roll:
                deleted = True
            else:
                writer.writerow(row)

    if deleted:
        print("🗑️ Student deleted")
    else:
        print("❌ Student not found")

def menu():
    create_file()
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("👋 Exiting program")
            break
        else:
            print("❌ Invalid choice")

menu()