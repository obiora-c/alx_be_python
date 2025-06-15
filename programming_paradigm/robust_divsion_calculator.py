

# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        try:
            result = num / den
            return f"Result: {result}"
        except ZeroDivisionError:
            return "Error: cannot divide by zero."

    except ValueError:
        return "Error: Both inputs must be numeric."
