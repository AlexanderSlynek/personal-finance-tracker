Personal Finance Tracker

Overview

Personal Finance Tracker is a command-line application written in Python that helps users manage their personal finances.

The application allows users to record income and expenses, monitor their balance, organize transactions by category, and store financial data between program launches.

This project was created to practice Python programming, file handling, data processing, and working with functions.

Features

Record income

Record expenses

View transaction history

Calculate current balance

Display total income

Display total expenses

Delete individual transactions

Clear all transactions

Search transactions by keyword

Sort transactions by amount

Display income grouped by category

Display expenses grouped by category

Automatically save all data to a local file

Technologies

Python 3

datetime

File I/O

Exception handling

Lists

Dictionaries

Project Structure

personal-finance-tracker/
│
├── personal_finance_tracker.py
├── transactions.txt
└── README.md

Getting Started

Clone the repository:

git clone https://github.com/AlexanderSlynek/personal-finance-tracker.git

Open the project folder:

cd personal-finance-tracker

Run the application:

python personal_finance_tracker.py

Example

1 - Add income
2 - Add expense
3 - Show all transactions
4 - Show balance
5 - Show total income
6 - Show total expense
7 - Clear all transactions
8 - Delete transaction
9 - Search transactions
10 - Sort transactions
11 - Expense categories
12 - Income categories
13 - Exit

Data Storage

All transactions are stored in the transactions.txt file.

Each transaction contains:

Transaction type

Amount

Category

Comment

Date

Example:

Income;3500;Salary;Monthly salary;22.07.2026

Future Improvements

Store data in JSON or SQLite

Monthly statistics

Graphical user interface (Tkinter or PyQt)

Charts for income and expenses

Export reports to Excel or PDF

Budget planning

Author

Alexander Slynek

This project was developed as a personal learning project to improve Python programming skills.