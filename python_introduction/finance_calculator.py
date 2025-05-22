# Step 1: Ask the user for their monthly income
# We use float() because income can have decimal values (e.g., 2500.50)
monthly_income_str = input("Enter your monthly income: ")
monthly_income = float(monthly_income_str)

# Step 2: Ask the user for their total monthly expenses
# Similarly, expenses can have decimal values
monthly_expenses_str = input("Enter your total monthly expenses: ")
monthly_expenses = float(monthly_expenses_str)

# Step 3: Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Step 4: Define the annual interest rate (5%)
annual_interest_rate = 0.05

# Step 5: Calculate projected savings after one year with interest
# Given formula: Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
# This can also be simplified to: Monthly Savings * 12 * (1 + 0.05)
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Step 6: Display all results
print(f"\n--- Your Financial Summary ---")
print(f"Monthly Income: ${monthly_income:.2f}") # .2f to display 2 decimal places
print(f"Monthly Expenses: ${monthly_expenses:.2f}")
print(f"Monthly Savings: ${monthly_savings:.2f}")
print(f"Projected Savings after one year (with 5% interest): ${projected_savings:.2f}")