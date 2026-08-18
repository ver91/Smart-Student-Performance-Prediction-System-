def get_student_data():
    print("STUDENT PERFORMANCE SYSTEM")

    name = input("Enter Student Name: ")

    attendance = float(input("Enter Attendance (%): "))
    study_hours = float(input("Enter Study Hours per Day: "))
    internal_marks = float(input("Enter Internal Marks (%): "))
    assignment = float(input("Enter Assignment Completion (%): "))

    return name, attendance, study_hours, internal_marks, assignment