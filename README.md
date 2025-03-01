# Home Loan EMI Calculator

This is a simple Python script that calculates the Equated Monthly Installment (EMI) for a loan based on user input. The script prompts the user to enter the loan amount, duration, interest rate, and optional down payment, then computes the EMI.

## Features

- Takes user input for loan amount, duration, interest rate, and down payment.
- Uses the standard EMI formula for calculations.
- Provides accurate and rounded EMI results.

## Formula Used

The EMI calculation follows this formula:

\(EMI = \frac{P \times r \times (1 + r)^n}{(1 + r)^n - 1}\)

Where:

- **P** = Principal loan amount
- **r** = Monthly interest rate (annual rate divided by 12)
- **n** = Loan duration in months

## How to Use

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/emi-calculator.git
   cd emi-calculator
   ```
2. Run the script:
   ```sh
   python emi_calculator.py
   ```
3. Enter the required values when prompted.
4. View the calculated EMI output.

## Example Usage

```
Enter the loan amount: 10000
Enter the loan duration in months: 12
Enter the monthly interest rate (as decimal, e.g., 0.1 for 10%): 0.1
Enter the down payment amount (if any, else 0): 0
Monthly EMI: 1467.63
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License.

## Contributions

Feel free to fork this repository, submit issues, or contribute enhancements.

---

Made with ❤️ by Shivraj

