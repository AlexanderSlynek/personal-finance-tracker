# Personal Finance Tracker

A simple command-line Personal Finance Tracker application written in Python.

## About

This project is a console application for managing personal finances. It allows users to record income and expenses, calculate their current balance, organize transactions by category, search and sort records, and automatically save all data between program launches.

The project was created to practice Python programming and improve skills in file handling, exception handling, functions, lists, and dictionaries.

## Features

- Add income
- Add expenses
- View transaction history
- Calculate current balance
- Display total income
- Display total expenses
- Delete transactions
- Clear all transactions
- Search transactions by keyword
- Sort transactions by amount
- Display income by category
- Display expenses by category
- Automatic saving to `transactions.txt`

## Technologies

- Python 3
- `datetime`
- File handling
- Exception handling
- Functions
- Lists
- Dictionaries

## How to Run

Clone the repository:

```bash
git clone https://github.com/AlexanderSlynek/personal-finance-tracker.git
```

Go to the project folder:

```bash
cd personal-finance-tracker
```

Run the program:

```bash
python main.py
```

## Project Structure

```text
personal-finance-tracker/
│
├── main.py
└── README.md
```

## Example

```text
1 - Add income
2 - Add expense
3 - Show all transactions
4 - Show balance
5 - Show total income
6 - Show total expenses
7 - Clear all transactions
8 - Delete transaction
9 - Search transactions
10 - Sort transactions
11 - Show expense categories
12 - Show income categories
13 - Exit
```

## Data Storage

All transactions are stored locally in `transactions.txt`.

The file is created automatically by the program when transactions are added.

Example:

```text
Income;5000;Salary;Monthly salary;22.07.2026
Expense;450;Food;Lunch;22.07.2026
```

## Future Improvements

- Store data in JSON or SQLite
- Add monthly financial reports
- Export reports to Excel or PDF
- Add charts for financial analysis
- Create a graphical user interface (GUI)

## Author

Alexander Slynek