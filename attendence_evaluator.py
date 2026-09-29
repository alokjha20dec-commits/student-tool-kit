import math


def attendance():
    print("\n" + "=" * 60)
    print("               ATTENDANCE EVALUATOR")
    print("=" * 60)

    try:
        attended = int(input("ENTER TOTAL NUMBER OF CLASSES ATTENDED => "))
        conducted = int(input("ENTER TOTAL NUMBER OF CLASSES CONDUCTED => "))
        upcoming = int(input("ENTER NUMBER OF UPCOMING CLASSES => "))
    except ValueError:
        print("Error: Please enter valid integer numbers.")
        return

    # Validations
    if conducted <= 0:
        print("Error: Total conducted classes must be greater than zero.")
        return
    if attended < 0 or upcoming < 0:
        print("Error: Class counts cannot be negative.")
        return
    if attended > conducted:
        print("Error: Attended classes cannot exceed conducted classes.")
        return

    # Calculations
    total_semester_classes = conducted + upcoming
    current_pct = (attended / conducted) * 100

    # Total classes needed across the whole semester for 75%
    total_needed = math.ceil(0.75 * total_semester_classes)

    # Classes still required out of upcoming ones
    needed_upcoming = max(0, total_needed - attended)

    # Classes that can be skipped
    bunkable = upcoming - needed_upcoming

    print("\n" + "-" * 60)
    print(f"CURRENT ATTENDANCE: {current_pct:.2f}% ({attended}/{conducted})")
    print("-" * 60)

    # Evaluation
    if bunkable < 0:
        max_possible = (
            (attended + upcoming) / total_semester_classes
        ) * 100
        print(
            "STATUS: DEBAR - You cannot reach 75% even if you attend every remaining class."
        )
        print(f"MAX ACHIEVABLE ATTENDANCE: {max_possible:.2f}%")
    else:
        if current_pct >= 75:
            print("STATUS: You are currently AT OR ABOVE the 75% criteria.")
        else:
            print("STATUS: You are currently BELOW the 75% criteria.")

        if needed_upcoming == 0:
            print("REQUIREMENT: 75% is already secured for the whole semester!")
        else:
            print(
                f"REQUIREMENT: Attend at least {needed_upcoming} of the {upcoming} remaining class(es)."
            )

        print(
            f"BUNK BUDGET: You can afford to bunk up to {bunkable} class(es)."
        )

    print("-" * 60 + "\n")


if __name__ == "__main__":
    attendance()