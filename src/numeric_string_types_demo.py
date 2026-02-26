"""
Milestone script: understanding numeric and string data types in Python.

This script demonstrates:
- Integers and floats
- Basic arithmetic
- String creation and manipulation
- Safe mixing of numbers and strings
- Type inspection and simple debugging patterns
"""


def numeric_examples():
    print("=== 1) Numeric Data Types ===")

    whole_number = 25
    decimal_number = 12.5

    print(f"whole_number = {whole_number} (type: {type(whole_number).__name__})")
    print(f"decimal_number = {decimal_number} (type: {type(decimal_number).__name__})")

    addition = whole_number + 5
    subtraction = whole_number - 3
    multiplication = whole_number * 2
    true_division = whole_number / 4
    floor_division = whole_number // 4

    print("\nArithmetic results:")
    print(f"- Addition: {whole_number} + 5 = {addition}")
    print(f"- Subtraction: {whole_number} - 3 = {subtraction}")
    print(f"- Multiplication: {whole_number} * 2 = {multiplication}")
    print(f"- True division: {whole_number} / 4 = {true_division}")
    print(f"- Floor division: {whole_number} // 4 = {floor_division}")

    precision_result = 0.1 + 0.2
    print(f"\nNumeric precision example: 0.1 + 0.2 = {precision_result}")


def string_examples():
    print("\n=== 2) String Data Types ===")

    first_name = "Data"
    last_name = "Scientist"
    full_label = first_name + " " + last_name

    print(f"first_name = {first_name} (type: {type(first_name).__name__})")
    print(f"last_name = {last_name} (type: {type(last_name).__name__})")
    print(f"Concatenated string: {full_label}")

    message = "Python data types are important"
    print("\nString access examples:")
    print(f"- Full message: {message}")
    print(f"- First character: {message[0]}")
    print(f"- First 6 characters: {message[:6]}")


def mixed_type_examples():
    print("\n=== 3) Mixing Numbers and Strings Safely ===")

    sales_count = 42
    print("Attempting to combine text and number directly...")

    try:
        bad_message = "Sales count: " + sales_count
        print(bad_message)
    except TypeError as error:
        print(f"TypeError observed: {error}")

    safe_message = "Sales count: " + str(sales_count)
    print(f"Fixed using str(): {safe_message}")

    number_as_text = "150"
    converted_number = int(number_as_text)
    print(f"Converted '150' to int: {converted_number} (type: {type(converted_number).__name__})")


def type_inspection_examples():
    print("\n=== 4) Inspecting Data Types ===")

    sample_values = [10, 3.14, "100", "analysis"]

    for value in sample_values:
        print(f"Value: {value!r} -> type: {type(value).__name__}")


def main():
    print("Python Numeric and String Data Types Demo")
    print("-----------------------------------------")

    numeric_examples()
    string_examples()
    mixed_type_examples()
    type_inspection_examples()

    print("\nDemo completed successfully.")


if __name__ == "__main__":
    main()
