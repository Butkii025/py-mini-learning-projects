def calculate_cgpa():
    """Calculates the Cumulative Grade Point Average (CGPA)."""

    num_subjects = int(input("Enter the number of subjects: "))

    total_credit_points = 0
    total_credits = 0

    for i in range(num_subjects):
        print(f"\n--- Subject {i + 1} ---")
        grade_input = input("Enter grade (e.g., A, B+, C): ").upper()
        credit_hours = float(input("Enter credit hours: "))

        grade_point = 0
        if grade_input == 'A+':
            grade_point = 4.0
        elif grade_input == 'A':
            grade_point = 4.0
        elif grade_input == 'A-':
            grade_point = 3.7
        elif grade_input == 'B+':
            grade_point = 3.3
        elif grade_input == 'B':
            grade_point = 3.0
        elif grade_input == 'B-':
            grade_point = 2.7
        elif grade_input == 'C+':
            grade_point = 2.3
        elif grade_input == 'C':
            grade_point = 2.0
        elif grade_input == 'C-':
            grade_point = 1.7
        elif grade_input == 'D+':
            grade_point = 1.3
        elif grade_input == 'D':
            grade_point = 1.0
        elif grade_input == 'F':
            grade_point = 0.0
        else:
            print("Invalid grade entered. Assuming 0.0 grade point.")

        total_credit_points += (grade_point * credit_hours)
        total_credits += credit_hours

    if total_credits == 0:
        cgpa = 0.0
    else:
        cgpa = total_credit_points / total_credits

    print(f"\nYour CGPA is: {cgpa:.2f}")

calculate_cgpa()