# Student Attendance Management System

students = {}

while True:
    print("\n--- Student Attendance Management System ---")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View All Attendance")
    print("4. View Student Attendance")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    # 1. Add Student
    if choice == "1":
        student_id = input("Enter Student ID: ").strip()

        if student_id in students:
            print("Student already exists.")
        else:
            name = input("Enter Student Name: ").strip()
            students[student_id] = {
                "name": name,
                "present": 0,
                "total": 0
            }
            print("Student added successfully.")

    # 2. Mark Attendance
    elif choice == "2":
        student_id = input("Enter Student ID: ").strip()

        if student_id not in students:
            print("Student not found.")
        else:
            while True:
                status = input("Enter P for Present or A for Absent: ").strip().upper()

                if status in ["P", "A"]:
                    students[student_id]["total"] += 1

                    if status == "P":
                        students[student_id]["present"] += 1
                        print("Attendance marked as Present.")
                    else:
                        print("Attendance marked as Absent.")
                    break
                else:
                    print("Invalid input. Please enter P or A only.")

    # 3. View All Attendance
    elif choice == "3":
        if not students:
            print("No students available.")
        else:
            print("\n--- Attendance Records ---")
            for sid, data in students.items():
                total = data["total"]
                present = data["present"]
                percentage = (present / total * 100) if total > 0 else 0
                print(f"ID: {sid} | Name: {data['name']} | Attendance: {present}/{total} ({percentage:.2f}%)")

    # 4. View Individual Student Attendance
    elif choice == "4":
        student_id = input("Enter Student ID: ").strip()

        if student_id not in students:
            print("Student not found.")
        else:
            data = students[student_id]
            total = data["total"]
            present = data["present"]
            percentage = (present / total * 100) if total > 0 else 0

            print("\n--- Student Attendance ---")
            print(f"Name: {data['name']}")
            print(f"Attendance: {present}/{total}")
            print(f"Percentage: {percentage:.2f}%")

    # 5. Exit
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select between 1 to 5.")
