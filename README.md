Personal Finance Tracker

A console-based application written in Python for managing personal income and expenses.

⸻

Description

Personal Finance Tracker is a command-line application that allows users to record and organize their financial transactions.

The program supports adding income and expenses, calculating the current balance, searching and sorting transactions, displaying statistics by category, and automatically saving data between program launches.

This project was created to practice Python programming, file handling, and working with data structures.

⸻

Features

Function	Description
Add Income	Record income transactions
Add Expense	Record expense transactions
Transaction History	View all saved transactions
Balance Calculation	Calculate the current balance
Total Income	Display the total amount of income
Total Expenses	Display the total amount of expenses
Delete Transaction	Remove a selected transaction
Clear History	Delete all saved transactions
Search	Find transactions by keyword
Sorting	Sort transactions by amount
Expense Categories	View expenses grouped by category
Income Categories	View income grouped by category
Data Persistence	Automatically save transactions to a file

⸻

Technologies

* Python 3
* datetime
* File handling
* Exception handling
* Lists
* Dictionaries

⸻

Project Structure

personal-finance-tracker/
│
├── personal_finance_tracker.py
├── transactions.txt
└── README.md

⸻

Installation

Clone the repository:

git clone https://github.com/AlexanderSlynek/personal-finance-tracker.git

Open the project directory:

cd personal-finance-tracker

Run the application:

python personal_finance_tracker.py

⸻

Example Menu

1  - Add income
2  - Add expense
3  - Show all transactions
4  - Show balance
5  - Show total income
6  - Show total expenses
7  - Clear all transactions
8  - Delete transaction
9  - Search transactions
10 - Sort transactions
11 - Show expense categories
12 - Show income categories
13 - Exit

⸻

Data Format

Transactions are stored in the transactions.txt file.

Each record contains:

Transaction Type ; Amount ; Category ; Comment ; Date

Example:

Income;3500;Salary;Monthly salary;22.07.2026
Expense;450;Food;Lunch;22.07.2026

⸻

Future Improvements

* Store data in JSON or SQLite
* Add monthly statistics
* Add data visualization
* Export reports to Excel or PDF
* Develop a graphical user interface (GUI)

⸻

Author

Alexander Slynek

Python learning project.