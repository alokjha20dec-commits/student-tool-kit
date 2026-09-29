# Student Help Kit 🎓

A modular, console-based utility suite built in Python designed to streamline essential day-to-day academic workflows. The suite integrates an extensive **Scientific Calculator**, a relative **Grade Evaluator**, and an **Attendance Tracker & Forecaster**.

## 📌 Project Overview

* **Project Title:** Student Help Kit

* **Author:** Alok Kumar Jha

* **Registration Number:**  26BAI11079

* **Environment:** Pure Python 3 (CLI / Terminal)

The goal of this project is to provide a fast, offline, and reliable desktop utility directly in the terminal, removing the need for separate apps or ad-supported online tools.

## 🚀 Key Features

### 1. 🧮 Scientific Calculator (`scientific_calculator.py`)

A comprehensive computation suite supporting standard and advanced operations:

* **Basic Arithmetic:** Addition, subtraction, multiplication, and division (with divide-by-zero protection).

* **Logarithmic Functions:** Custom-base and natural log computation with validation ($x > 0$ and base $\neq 1$).

* **Trigonometry:** Sine, cosine, and tangent calculations in degrees (including edge-case handling for undefined tangent angles).

* **Financial Math:** Compound interest calculator computing total accrued balance and net interest:
  

  $$
  A = P \left(1 + \frac{r}{100n}\right)^{nt}
  $$

* **Unit Conversions:** Temperature ($^\circ\text{C} \leftrightarrow ^\circ\text{F}$), Distance ($\text{km} \leftrightarrow \text{miles}$), and Weight ($\text{kg} \leftrightarrow \text{lbs}$).

* **Powers & Radicals:** Arbitrary exponentiation ($x^y$) and non-negative square root calculations.

* **Number Base Converter:** Step-by-step conversion across Binary, Decimal, Octal, and Hexadecimal representations.

* **Session History:** Keeps an audit trail of calculations performed during the session.

### 2. 📊 Grade Evaluator (`grade_evaluator.py`)

A relative grading model evaluated per course against the class mean:

| Grade | Condition | 
 | ----- | ----- | 
| **S** | Mark $\ge$ Class Average $+ 10$ | 
| **A** | Mark $\ge$ Class Average $+ 5$ | 
| **B** | Mark $\ge$ Class Average $- 5$ | 
| **C** | Mark $\ge$ Class Average $- 10$ | 
| **D** | Mark $\ge$ Class Average $- 15$ | 
| **F** | Below Class Average $- 15$ | 

Outputs a clear, tabular academic report card displaying raw marks, class averages, and assigned letter grades.

### 3. 🗓️ Attendance Evaluator (`attendence_evaluator.py`)

Predictive planner designed around the standard **75% minimum attendance rule**:

* **Current Metric:** Computes real-time percentage:
  

  $$
  \text{Attendance (\%)} = \left(\frac{\text{Classes Attended}}{\text{Classes Scheduled}}\right) \times 100
  $$

* **Target Threshold:** Calculates the total classes required across the full semester (past + upcoming):
  

  $$
  \text{Required} = \lceil 0.75 \times (\text{Scheduled} + \text{Upcoming}) \rceil
  $$

* **Actionable Insights:**

  * Tells you the exact number of future classes you **must attend** to reach or preserve 75%.

  * Calculates how many upcoming classes you can safely **miss/bunk** without dropping below the threshold.

  * Flags situations where maintaining 75% is mathematically impossible.

## 📂 Project Structure

```
Student-Help-Kit/
├── main.py                    # Application entry point & main menu driver
├── scientific_calculator.py   # Scientific calculator and unit conversion engine
├── grade_evaluator.py         # Multi-course relative grade calculator
├── attendence_evaluator.py    # Attendance calculator and semester planner
└── README.md                  # Project documentation

```

## 🛠️ Installation & Setup

### Prerequisites

* Python 3.8 or higher installed on your system.

* Standard Python libraries used (`math`, `random`) — **no external `pip` dependencies required**.

### Running the Application

1. Clone or download the repository files into a single directory:

   ```
   git clone https://github.com/your-username/student-help-kit.git
   cd student-help-kit
   
   ```

2. Run the main driver:

   ```
   python main.py
   
   ```

## 💻 Sample Usage

```
================================================================================
           ---STUDENT HELP KIT---          
================================================================================
  DEVELOPER : ALOK KUMAR JHA
  REG NO    : 26BAI11079
  PROJECT   : STUDENT HELP KIT [CALCULATOR + ATTENDANCE + GRADES]
--------------------------------------------------------------------------------
  [1] Scientific Calculator
  [2] Grade Evaluator
  [3] Attendance Evaluator
  [0] Exit 
================================================================================
Enter your choice (0-3) >>> 

```

## 🛡️ Robustness & Input Validation

* Non-numeric input handling using safe `try-except` conversions.

* Range and boundary checks (e.g., negative roots, non-positive logarithm arguments, division by zero).

* Logic checks preventing users from attending more classes than were scheduled.

## 📜 License

This project is open-source and free to use for educational purposes.