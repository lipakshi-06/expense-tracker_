# expense-tracker_
Why an Expense Tracker Is Needed?
An expense tracker is needed to help individuals understand, monitor, and control their spending habits. In today’s fast-paced lifestyle, people often spend money without noticing where it goes. An expense tracker keeps a detailed record of every transaction and gives users a clear picture of their financial activities.

Key Reasons:
- Prevents Overspending – By monitoring every expense, users become aware of unnecessary spending and can make better financial decisions.
- Budget Management – It helps users set a budget and stick to it by tracking expenses category-wise and monthly.
- Financial Awareness – Users can analyze patterns in their spending and understand where most of their money goes.
- Savings Improvement – When spending is managed properly, users can save more money for future goals.
- Record Maintenance – It serves as a digital record of transactions that can be referenced anytime, reducing dependency on memory.
- Goal Setting – Helps users align spending habits with financial goals (e.g., buying a gadget, education expenses, emergency fund).

About This Project:
-This is a Python-based Expense Tracker designed to help users record and manage their daily expenses.
-It provides a simple and user-friendly interface built using Tkinter (GUI library).
-All expenses are stored permanently using SQLite database, so the data remains even after closing the application.

Features:
-Add expense with description, amount, category & date.
-Automatically records the current date if not entered manually.
-Displays all expenses in a table format with sortable columns.
-Shows total spending and category-wise expense summary.
-Allows deleting selected expense entries from the database.
-Data is stored locally in expenses.db using SQLite.

Technologies Used:
Component	                             Technology
Programming Language	                    Python
Graphical User Interface	                Tkinter
Database	                                SQLite
Date & Time Module	                      datetime

How It Works:
-On startup, it checks and creates the table expenses in SQLite if it does not exist.
-Users input the expense details, and clicking “Add Expense” stores the information in the database.
-The records automatically refresh in the table with updated totals and summaries.
-Selecting a row and clicking “Delete Selected” removes the record from the database.

output image-
<img width="750" height="612" alt="image" src="https://github.com/user-attachments/assets/429cd282-681e-45fe-af95-9b357cad5d72" />
