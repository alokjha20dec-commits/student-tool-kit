import sys

from scientific_calculator import cal
from grade_evaluator import evaluate_grades as grade

try:
    from attendance_evaluator import attendance
except ImportError:
    from attendence_evaluator import attendance


def display_menu():
    print("\n" + "=" * 80)
    print(f"{'--- STUDENT HELP KIT ---':^80}")
    print("=" * 80)
    print("  DEVELOPER : ALOK KUMAR JHA")
    print("  REG NO    : 26BAI11079")
    print("  PROJECT   : STUDENT HELP KIT [CALCULATOR + ATTENDANCE + GRADES]")
    print("-" * 80)
    print("  ABOUT:")
    print("  An all-in-one console application built to handle")
    print("  SCIENTIFIC CALCULATOR, GRADE EVALUATOR, and ATTENDANCE EVALUATOR tasks.")
    print("=" * 80)
    print("  [1] Scientific Calculator")
    print("  [2] Grade Evaluator")
    print("  [3] Attendance Evaluator")
    print("  [0] Exit")
    print("=" * 80)


def main():
    menu_actions = {
        "1": ("Scientific Calculator", cal),
        "2": ("Grade Evaluator", grade),
        "3": ("Attendance Evaluator", attendance),
    }

    while True:
        display_menu()

        try:
            choice = input("Enter your choice (0-3) >>> ").strip()
        except (KeyboardInterrupt, EOFError):
            choice = "0"

        if choice == "0":
            print("\n" + "*" * 80)
            print("  Logging off: ALOK KUMAR JHA (26BAI11079)")
            print("  Thanks for using the STUDENT HELP KIT. Goodbye!")
            print("*" * 80 + "\n")
            sys.exit(0)

        if choice in menu_actions:
            name, func = menu_actions[choice]
            print(f"\nOpening {name}...\n")
            try:
                func()
            except Exception as e:
                print(f"\n[Error encountered in {name}]: {e}")
            input("\nPress Enter to return to main menu...")
        else:
            print("\n[!] Invalid selection! Please enter 0, 1, 2, or 3.")


if __name__ == "__main__":
    main()