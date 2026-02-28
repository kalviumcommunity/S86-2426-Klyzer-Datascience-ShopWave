"""
Milestone script: writing readable variable names and comments (PEP 8 basics).

This script demonstrates:
- poor vs readable variable naming
- snake_case naming consistency
- constants in uppercase
- comments that explain intent, not obvious operations
"""


MAX_ALLOWED_DISCOUNT_PERCENT = 30


def show_poor_naming_example():
    print("=== 1) Poor Naming Example (for comparison) ===")

    x = 250
    y = 15
    z = x - (x * y / 100)

    print(f"x={x}, y={y}, z={z}")
    print("These names hide intent and slow down code review.")


def show_readable_naming_example(order_total, discount_percent):
    print("\n=== 2) Readable Naming Example (PEP 8) ===")

    if discount_percent > MAX_ALLOWED_DISCOUNT_PERCENT:
        print(
            "Discount reduced to policy maximum "
            f"({MAX_ALLOWED_DISCOUNT_PERCENT}%)."
        )
        discount_percent = MAX_ALLOWED_DISCOUNT_PERCENT

    discount_amount = order_total * (discount_percent / 100)
    final_total_after_discount = order_total - discount_amount

    print(f"order_total={order_total}")
    print(f"discount_percent={discount_percent}")
    print(f"discount_amount={discount_amount}")
    print(f"final_total_after_discount={final_total_after_discount}")


def show_commenting_practices(sales_values):
    print("\n=== 3) Useful Comments: Explain Intent ===")

    # Intent: identify a stable central value to reduce sensitivity to spikes.
    sorted_sales_values = sorted(sales_values)
    middle_index = len(sorted_sales_values) // 2
    median_sales_value = sorted_sales_values[middle_index]

    print(f"sales_values={sales_values}")
    print(f"sorted_sales_values={sorted_sales_values}")
    print(f"median_sales_value={median_sales_value}")

    print("Comment quality check:")
    print("- Good: explains why median is used here.")
    print("- Bad: comments like 'sort list' or 'print value' add no value.")


def show_consistency_example():
    print("\n=== 4) Naming Consistency Across a File ===")

    monthly_subscription_count = 120
    active_trial_count = 18
    churned_subscription_count = 5

    net_active_subscriptions = monthly_subscription_count - churned_subscription_count
    conversion_rate_percent = (active_trial_count / monthly_subscription_count) * 100

    print(f"monthly_subscription_count={monthly_subscription_count}")
    print(f"active_trial_count={active_trial_count}")
    print(f"churned_subscription_count={churned_subscription_count}")
    print(f"net_active_subscriptions={net_active_subscriptions}")
    print(f"conversion_rate_percent={conversion_rate_percent:.2f}")


def main():
    print("Python Readable Naming and Comments Demo")
    print("----------------------------------------")

    show_poor_naming_example()
    show_readable_naming_example(order_total=250, discount_percent=35)
    show_commenting_practices([45, 18, 90, 30, 52])
    show_consistency_example()

    print("\nDemo completed successfully.")


if __name__ == "__main__":
    main()
