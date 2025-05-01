"""
This program calculates the monthly payment for a loan with monthly compounded
interest rate. The calculation is based on the details provided by the user
regarding the loan amount, Annual Percentage rate (APR), and loan duration.
"""

def prompt(string):
    print(f"==> {string}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def calculate_payment(loan_amount, monthly_interest_rate,
                      loan_duration_months):
    if monthly_interest_rate > 0: # If the loan has an interest rate
        result = loan_amount * (monthly_interest_rate
                                    / (1 - (1 + monthly_interest_rate)
                                        ** (- loan_duration_months)))
    else: # For no-interest loans
        result = loan_amount / loan_duration_months

    return result

def main():
    print("Calculate your monthly loan payment!\n"
          "Enter your loan details and get the result.")

    # 1. Ask for the loan amount
    prompt("What is the total loan amount?")
    amount = input()

    while invalid_number(amount):
        prompt("That doesn't look like a valid number. Try again.")
        amount = input()

    amount = float(amount)

    # 2. Ask for the interest rate
    prompt("What is the Annual Percentage Rate?\n"
           "Example: enter '5' for 5%, '2.5' for 2.5%, etc.")
    annual_rate = input()

    while invalid_number(annual_rate):
        prompt("That doesn't look like a valid number. Try again.")
        annual_rate = input()

    annual_rate = float(annual_rate)

    # Convert annual rate to monthly decimal
    monthly_rate = annual_rate / 100 / 12

    # 3. Ask for the loan duration
    prompt("What is the loan duration in years?")
    duration_years = input()

    while invalid_number(duration_years):
        prompt("That doesn't look like a valid number. Try again.")
        duration_years = input()

    duration_years = float(duration_years)
    duration_months = duration_years * 12

    monthly_payment = calculate_payment(amount, monthly_rate, duration_months)

    # Format the result with thousand separators and rounded to 2 decimals
    monthly_payment_rounded = f"{monthly_payment:,.2f}"

    prompt(f"Your monthly payment is: ${monthly_payment_rounded}")


while True:
    main()
    prompt("Do you want to run another calculation? (y/n)")
    answer = input().lower()
    if not answer.startswith('y'):
        prompt("Thank you for using the calculator. Goodbye.")
        break