Expense Tracker - Detailed Documentation

Overview:
This Expense Tracker is a simple yet effective personal finance management tool built using Python and Flask. The application allows users to record daily expenses, create monthly budgets, generate reports, and manage shared group expenses. It uses CSV and JSON files for data storage, making it fully portable and easy to understand for beginners.

Key Features:
1. Add Expense:
   - Users can enter the name, amount, category, month, and optional group.
   - The data is stored in expenses.csv.
   - Categories include: Food, Transport, Home, Work, Fun, Misc.

2. Set Monthly Budget:
   - Users can set a spending limit for a specific month and category.
   - Stored in budgets.json.
   - The system can compare actual spending vs the budget.

3. View All Expenses:
   - Displays all entries stored in the expenses file.
   - Helps users analyze spending patterns.

4. Monthly Total Report:
   - Calculates the total amount spent in a particular month.
   - Useful for quick financial review.

5. Spending vs Budget Analysis:
   - Shows how much is spent in each category.
   - Displays status: OK, Exceeded, or 10% Remaining.

6. Group Expense Split:
   - Helps calculate how much each participant owes or should receive.
   - Useful for trips, shared meals, and group activities.

Technologies Used:
- Python 3
- HTML for UI
- CSS for styling
- CSV for storing expenses
- JSON for storing budgets and group information

Installation Instructions:
1. Create a Python virtual environment:
   python -m venv venv

2. Activate the environment:
   Windows: venv\Scripts\activate

3. Install required dependencies:
   pip install -r requirements.txt

4. Start the application:
   python app.py

5. Open the application in a browser:
   http://localhost:5000

How to Use the Application:

Adding an Expense:
- Enter details in the fields provided.
- Click Save to record the expense.
- The entry appears instantly in the expenses list.

Setting a Budget:
- Enter the month, category, and limit.
- Click Set Budget.
- Budgets are stored for use in spending analysis.

Viewing Expenses:
- Press Refresh List to see all expenses.
- Displays data in a clear table format.

Generating Monthly Total:
- Enter the month.
- Click Monthly Total to see total expenses.

Comparing Spending vs Budget:
- Enter a month.
- Click Compare.
- The app shows:
    category, spent amount, budget amount, and status.

Group Summary:
- Enter group name.
- Shows how much each person must pay or receive.

File Structure:
app.py                - Flask backend
expense.py            - Expense data model
expenses.csv          - Stores expense entries
budgets.json          - Stores monthly budgets
groups.json           - Stores group member data
templates/index.html  - Frontend UI
requirements.txt      - Python dependencies
README.txt            - Documentation

Why This App Is Useful:
- Helps users track and manage spending.
- Offers insights into financial habits.
- Supports shared expenses.
- Ideal for small projects, assignments, and beginners.
- Easy to understand and modify
