def grade():
    print("\n" + "=" * 58)
    print("                 GRADE EVALUATOR")
    print("=" * 58)

    while True:
        try:
            num_courses = int(input("ENTER NUMBER OF COURSES REGISTERED  ->>> "))
            if num_courses > 0:
                break
            print("Please enter at least 1 course.")
        except ValueError:
            print("Error: Please enter a valid integer for the number of courses.")

    all_courses = []
    mis = []
    ais = []
    grades_list = []  # Renamed from 'grade' to avoid shadowing the function name

    # Ask for input for each course
    for i in range(num_courses):
        while True:
            course = input(f"\nEnter course '{i + 1}' name => ").strip()
            if course:
                break
            print("Course name cannot be empty.")

        all_courses.append(course)

        # Input validation for marks
        while True:
            try:
                get_m = float(input(f"Enter your mark in '{course}' => "))
                if 0 <= get_m <= 100:
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Error: Invalid numeric input. Please enter a valid number.")

        # Input validation for class average
        while True:
            try:
                get_a = float(input(f"Enter your class avg. in '{course}' => "))
                if 0 <= get_a <= 100:
                    break
                print("Average must be between 0 and 100.")
            except ValueError:
                print("Error: Invalid numeric input. Please enter a valid number.")

        mis.append(get_m)
        ais.append(get_a)

    # Evaluate grades
    for i in range(num_courses):
        diff = mis[i] - ais[i]
        if diff >= 10:
            grades_list.append("S")
        elif diff >= 5:
            grades_list.append("A")
        elif diff >= -5:
            grades_list.append("B")
        elif diff >= -10:
            grades_list.append("C")
        elif diff >= -15:
            grades_list.append("D")
        else:
            grades_list.append("F")

    # Print Report Card
    print("\n" + "=" * 58)
    print("\t----REPORT CARD----")
    print("=" * 58)

    for i in range(num_courses):
        print("Course        :  ", all_courses[i])
        print(f"Scored mark   ->   {mis[i]:.2f}")
        print(f"Class avg.    ->   {ais[i]:.2f}")
        print("Grade         ->  ", grades_list[i])
        print("_" * 58)


# Alias so main.py can also import evaluate_grades
evaluate_grades = grade

if __name__ == "__main__":
    grade()
