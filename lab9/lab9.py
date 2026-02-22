class ZeroValueError(Exception):
    """Raised when the entered number is zero."""
    def __init__(self, message="Zero is not allowed."):
        super().__init__(message)
def convert_to_number(user_text):
    """
    Converts input to float.
    Raises ValueError if conversion fails.
    """
    try:
        number = float(user_text)
    except ValueError:
        raise ValueError("Input must be a numeric value.")

    if number == 0:
        raise ZeroValueError()

    return number

while True:
    raw_input_value = input("Enter a number (or type 'q' to quit): ").strip()

    if raw_input_value.lower() == "q":
        print("Program stopped.")
        break

    try:
        valid_number = convert_to_number(raw_input_value)
        print(f"Accepted number: {valid_number}")

    except ZeroValueError as e:
        print("Custom Exception:", e)

    except ValueError as e:
        print("Validation Error:", e)

    finally:
        print("Attempt finished.\n")