def loan_emi(amount, duration, rate, down_payment=0):
    """
    Calculate the Equated Monthly Installment (EMI) for a loan.
    
    Parameters:
    amount (float): Total loan amount (principal).
    duration (int): Loan duration in months.
    rate (float): Monthly interest rate (as a decimal, e.g., 0.1 for 10%).
    down_payment (float, optional): Initial amount paid upfront. Default is 0.
    
    Returns:
    float: EMI amount rounded to 2 decimal places.
    """
    loan_amount = amount - down_payment
    emi = (loan_amount * rate * ((1 + rate) ** duration)) / (((1 + rate) ** duration) - 1)
    return round(emi, 2)

# Example usage
if __name__ == "__main__":
    amount = float(input("Enter the loan amount: "))  # Principal amount
    duration = int(input("Enter the loan duration in months: "))  # Loan duration in months
    rate = float(input("Enter the monthly interest rate (as decimal, e.g., 0.1 for 10%): "))  # Monthly interest rate
    down_payment = float(input("Enter the down payment amount (if any, else 0): "))
    
    emi_value = loan_emi(amount, duration, rate, down_payment)
    print(f"Monthly EMI: {emi_value}")

