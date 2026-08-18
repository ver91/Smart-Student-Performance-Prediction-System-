def get_recommendation(performance):

    if performance == "EXCELLENT":
        return "Excellent performance. Continue the same level of effort."

    elif performance == "GOOD":
        return "Maintain attendance and continue regular study."

    elif performance == "AVERAGE":
        return "Improve study hours and focus on regular practice."

    elif performance == "POOR":
        return "Improve attendance, study hours and assignment completion."

    else:
        return "Immediate improvement is required. Seek faculty guidance."