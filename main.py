from student_data import get_student_data
from calculation import calculate_average
from performance import calculate_performance
from recommendation import get_recommendation

name, attendance, study_hours, internal_marks, assignment = get_student_data()

average = calculate_average(
    attendance,
    study_hours,
    internal_marks,
    assignment
)
performance = calculate_performance(average)

recommendation = get_recommendation(performance)

print("\n Output")
print(f"Student Name: {name}")
print(f"Performance Level: {performance}")
print(f"Recommendation:{recommendation}")