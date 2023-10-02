# Initialize an empty dictionary to store attendance
attendance_dict = {}

def add_attendance(student_name):
    if student_name not in attendance_dict:
        attendance_dict[student_name] = 1
        print(f"{student_name} is marked as present.")
    else:
        print(f"{student_name} is already marked as present.")

def view_attendance():
    print("\nAttendance List:")
    for student, status in attendance_dict.items():
        print(f"{student}: {'Present' if status == 1 else 'Absent'}")

def main():
    while True:
        print("\nAttendance Tracker Menu:")
        print("1. Add Attendance")
        print("2. View Attendance")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            student_name = input("Enter student name: ")
            add_attendance(student_name)
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
