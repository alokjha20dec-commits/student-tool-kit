# Problem Statement: STUDENT HELP KIT

## 1. Context & Background
University students constantly juggle multiple academic responsibilities. They frequently need to perform complex scientific calculations for assignments, predict their final grades based on relative class averages, and strictly monitor their attendance to avoid penalties (such as debarment from exams due to falling below the standard 75% attendance criteria). 

Currently, students rely on fragmented solutions: a physical calculator or mobile app for math, manual calculations or messy spreadsheets for relative grading, and mental math or basic calculators for attendance tracking. This fragmentation is inefficient and prone to human error, especially when calculating future attendance requirements.

## 2. Core Problem
There is a lack of a unified, accessible, and lightweight digital tool tailored specifically to the daily computational needs of a university student. Students need a way to rapidly process scientific math, evaluate their academic standing (grades), and strategically plan their class presence (attendance) within a single environment.

## 3. Proposed Solution
** STUDENT HELP KIT ** proposes a unified Command Line Interface (CLI) application built in Python. The system aggregates three highly relevant student tools into one seamless menu-driven program:

1.  **A Scientific Calculator:** Capable of handling not just basic arithmetic, but also trigonometry, logarithms, number system conversions, and financial mathematics.
2.  **A Relative Grade Evaluator:** An algorithm that automates the process of determining letter grades based on individual scores compared to class averages, producing an instant report card.
3.  **An Attendance Strategist:** A predictive calculator that takes current attendance data and future schedules to definitively tell a student how many classes they must attend to meet a 75% threshold, or how many they can afford to miss.

## 4. Objectives & Scope
*   **Simplicity & Speed:** Provide an entirely CLI-based interface for fast execution without the overhead of a Graphical User Interface (GUI).
*   **Accuracy:** Eliminate mathematical errors in critical attendance and grade calculations through strict, tested programmatic logic.
*   **Modularity:** Structure the code using independent modules (`scientific_calculator.py`, `grade_evaluator.py`, `attendence_evaluator.py`) coordinated by a `main.py` controller, ensuring easy maintenance and future scalability (e.g., adding a CGPA calculator module later).
*   **Robustness:** Implement basic error handling to gracefully catch invalid user inputs without crashing the application.