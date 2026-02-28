"""
Milestone script: writing conditional statements for data logic.

This script demonstrates:
- Basic if statements
- if-else branching
- if-elif-else multi-branch logic
- Numeric and string comparisons
- Logical operators: and, or, not
"""


def basic_if_statement():
    print("=== 1) Basic if Statement ===")

    order_total = 125.0
    minimum_for_discount = 100.0

    print(f"Order total: {order_total}")
    print(f"Discount threshold: {minimum_for_discount}")

    if order_total >= minimum_for_discount:
        print("Condition is TRUE: order qualifies for discount.")

    print("When condition is FALSE, the if block does not execute.")


def if_else_branching():
    print("\n=== 2) if-else Branching ===")

    stock_count = 0
    print(f"Current stock count: {stock_count}")

    if stock_count > 0:
        print("Product is in stock.")
    else:
        print("Product is out of stock.")


def if_elif_else_multiple_conditions():
    print("\n=== 3) if-elif-else for Multiple Conditions ===")

    data_quality_score = 78
    print(f"Data quality score: {data_quality_score}")

    if data_quality_score >= 90:
        print("Quality status: Excellent")
    elif data_quality_score >= 75:
        print("Quality status: Acceptable")
    elif data_quality_score >= 60:
        print("Quality status: Needs review")
    else:
        print("Quality status: Poor")


def string_and_numeric_conditions():
    print("\n=== 4) Numeric and String Comparisons ===")

    region = "north"
    monthly_sales = 42

    if region == "north":
        print("String condition TRUE: matched region 'north'.")
    else:
        print("String condition FALSE: region did not match.")

    if monthly_sales > 30:
        print("Numeric condition TRUE: monthly sales are above 30.")
    else:
        print("Numeric condition FALSE: monthly sales are 30 or below.")


def logical_operators_examples():
    print("\n=== 5) Logical Operators (and, or, not) ===")

    sales = 58
    returns = 3
    customer_tier = "standard"
    account_flagged = False

    if sales >= 50 and returns <= 5:
        print("AND condition TRUE: high sales with controlled returns.")
    else:
        print("AND condition FALSE: both requirements not met.")

    if customer_tier == "premium" or sales >= 55:
        print("OR condition TRUE: at least one condition is satisfied.")
    else:
        print("OR condition FALSE: no condition satisfied.")

    if not account_flagged:
        print("NOT condition TRUE: account is not flagged.")
    else:
        print("NOT condition FALSE: account is flagged.")


def edge_case_check():
    print("\n=== 6) Edge Case Check ===")

    score = 75
    print(f"Checking boundary value score={score}")

    if score >= 75:
        print("Boundary handled intentionally: score qualifies as Acceptable.")
    else:
        print("Boundary check failed.")


def main():
    print("Python Conditional Statements Demo")
    print("----------------------------------")

    basic_if_statement()
    if_else_branching()
    if_elif_else_multiple_conditions()
    string_and_numeric_conditions()
    logical_operators_examples()
    edge_case_check()

    print("\nDemo completed successfully.")


if __name__ == "__main__":
    main()
