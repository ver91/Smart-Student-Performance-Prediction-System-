def calculate_performance(average):

    if average >= 80:
        return "EXCELLENT"

    elif average >= 60:
        return "GOOD"

    elif average >= 50:
        return "AVERAGE"

    elif average >= 40:
        return "POOR"

    else:
        return "NEEDS IMPROVEMENT"