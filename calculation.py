def calculate_average(attendance, study_hours, internal_marks, assignment):

    study_percentage = min((study_hours / 8) * 100, 100)

    average = (
        attendance +
        study_percentage +
        internal_marks +
        assignment
    ) / 4

    return average