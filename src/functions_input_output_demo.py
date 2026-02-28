"""
Milestone script: passing data into functions and returning results.

This script demonstrates:
- parameters and arguments
- return statements
- reusing returned values in other computations
- avoiding hardcoded values and print-only function design
"""


def calculate_revenue(unit_price, units_sold):
    return unit_price * units_sold


def apply_discount(amount, discount_percent):
    discount_value = amount * (discount_percent / 100)
    return amount - discount_value


def calculate_tax(amount, tax_rate_percent):
    return amount * (tax_rate_percent / 100)


def build_summary(label, value):
    return f"{label}: {value:.2f}"


def safe_divide(total, count):
    if count == 0:
        return None
    return total / count


def main():
    print("Python Functions: Input and Output Data Flow Demo")
    print("-------------------------------------------------")

    print("\n=== 1) Parameters and Arguments ===")
    base_revenue = calculate_revenue(25.0, 12)
    print(f"Revenue from calculate_revenue(25.0, 12): {base_revenue}")

    second_revenue = calculate_revenue(18.5, 20)
    print(f"Revenue from calculate_revenue(18.5, 20): {second_revenue}")

    print("\n=== 2) Returning Values ===")
    discounted_total = apply_discount(base_revenue, 10)
    print(f"Discounted total (10% off): {discounted_total}")

    print("\n=== 3) Reusing Returned Results ===")
    tax_value = calculate_tax(discounted_total, 8)
    final_total = discounted_total + tax_value
    print(build_summary("Tax value", tax_value))
    print(build_summary("Final total", final_total))

    average_order = safe_divide(final_total, 4)
    print(f"Average order value (4 orders): {average_order:.2f}")

    print("\n=== 4) Avoiding Common Mistakes ===")
    print("- Values are passed as arguments, not hardcoded inside main calculations.")
    print("- Functions return data; printing is done in main() for clearer control.")
    print("- safe_divide returns None for invalid input (count=0) to avoid crashes.")

    no_orders_average = safe_divide(final_total, 0)
    print(f"safe_divide(final_total, 0) returned: {no_orders_average}")

    print("\nDemo completed successfully.")


if __name__ == "__main__":
    main()
