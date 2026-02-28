"""
Milestone script: structuring Python code for readability and reuse.

Script layout:
1) Imports and constants (setup)
2) Helper functions (reusable logic)
3) Main execution flow (clean top-level entry point)
"""

# ============================
# 1) Imports and setup values
# ============================

from statistics import mean

DEFAULT_TAX_RATE_PERCENT = 8


# ======================================
# 2) Helper functions (reusable section)
# ======================================

def print_section(title):
    print(f"\n=== {title} ===")


def calculate_subtotal(item_prices):
    return sum(item_prices)


def calculate_tax(subtotal, tax_rate_percent):
    return subtotal * (tax_rate_percent / 100)


def calculate_final_total(item_prices, tax_rate_percent=DEFAULT_TAX_RATE_PERCENT):
    subtotal = calculate_subtotal(item_prices)
    tax_amount = calculate_tax(subtotal, tax_rate_percent)
    final_total = subtotal + tax_amount

    return {
        "subtotal": subtotal,
        "tax_amount": tax_amount,
        "final_total": final_total,
    }


def summarize_order(order_name, item_prices):
    order_totals = calculate_final_total(item_prices)
    average_item_price = mean(item_prices)

    print(f"Order: {order_name}")
    print(f"Item prices: {item_prices}")
    print(f"Average item price: {average_item_price:.2f}")
    print(f"Subtotal: {order_totals['subtotal']:.2f}")
    print(f"Tax amount: {order_totals['tax_amount']:.2f}")
    print(f"Final total: {order_totals['final_total']:.2f}")


# ======================
# 3) Execution (top level)
# ======================

def main():
    print("Python Code Structure: Readability and Reuse Demo")
    print("--------------------------------------------------")

    print_section("A) Script Structure Overview")
    print("- Imports and constants are grouped at the top.")
    print("- Reusable functions are defined in the middle.")
    print("- Execution is kept inside main() at the bottom.")

    print_section("B) Reuse Through Functions")
    first_order_prices = [12.5, 8.0, 15.0]
    second_order_prices = [20.0, 5.5, 9.5, 14.0]

    summarize_order("Order-1", first_order_prices)
    summarize_order("Order-2", second_order_prices)

    print_section("C) Why This Structure Helps")
    print("- Repeated logic is extracted into helper functions.")
    print("- Main flow reads like a high-level story.")
    print("- Updates are easier because logic is centralized.")

    print("\nDemo completed successfully.")


if __name__ == "__main__":
    main()
