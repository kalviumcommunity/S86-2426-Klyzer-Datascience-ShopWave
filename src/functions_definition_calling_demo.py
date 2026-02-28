"""
Milestone script: defining and calling Python functions.

This script demonstrates:
- Defining functions with def
- Calling functions and execution flow
- Parameters and arguments
- Basic local vs global scope behavior
"""


project_label = "ShopWave"


def print_section(title):
    print(f"\n=== {title} ===")


def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python functions demo.")


def calculate_total(price, quantity):
    total = price * quantity
    print(f"Calculated total: {price} x {quantity} = {total}")
    return total


def classify_value(value):
    if value >= 80:
        return "High"
    if value >= 50:
        return "Medium"
    return "Low"


def scope_example():
    local_status = "Inside function scope"
    print(f"Global variable visible inside function: project_label = {project_label}")
    print(f"Local variable created inside function: local_status = {local_status}")


def execution_flow_demo(user_name, unit_price, units):
    print("Step 1: Function started")
    greet_user(user_name)
    total_amount = calculate_total(unit_price, units)
    band = classify_value(total_amount)
    print(f"Step 2: Value classification result = {band}")
    print("Step 3: Function finished, returning control to caller")
    return total_amount, band


def main():
    print("Python Functions: Defining and Calling Demo")
    print("-------------------------------------------")

    print_section("1) Defining and Calling a Function")
    greet_user("Data Learner")

    print_section("2) Parameters and Arguments")
    first_total = calculate_total(12.5, 4)
    second_total = calculate_total(8, 7)
    print(f"Two calls with different arguments: {first_total} and {second_total}")

    print_section("3) Function Execution Flow")
    final_total, final_band = execution_flow_demo("Klyzer", 15, 6)
    print(f"Returned values -> total: {final_total}, band: {final_band}")

    print_section("4) Basic Function Scope")
    print(f"Global variable from main: project_label = {project_label}")
    scope_example()
    print("Local variables from scope_example() are not available outside that function.")

    print("\nDemo completed successfully.")


if __name__ == "__main__":
    main()
