from student_data import get_student_data
from calculation import calculate_average
from performance import calculate_performance
from recommendation import get_recommendation


# Get student data
name, attendance, study_hours, internal_marks, assignment = get_student_data()


# Calculate average
average = calculate_average(
    attendance,
    study_hours,
    internal_marks,
    assignment
)


# Calculate performance
performance = calculate_performance(average)


# Generate recommendation
recommendation = get_recommendation(performance)


# Display output
print("\n Output")
print(f"Student Name: {name}")
print(f"Performance Level: {performance}")
print(f"Recommendation:{recommendation}")