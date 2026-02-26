"""
Milestone script: working with Python lists, tuples, and dictionaries.

This script demonstrates:
- List creation, access, modification, append, remove, and iteration
- Tuple creation, indexed access, and immutability behavior
- Dictionary key-value access, update, and insertion
- How to choose the right structure for a task
"""


def list_examples():
    print("=== 1) Lists (Ordered + Mutable) ===")

    daily_visits = [120, 135, 110, 160]
    print(f"Original list: {daily_visits}")

    print(f"First item (index 0): {daily_visits[0]}")
    print(f"Last item (index -1): {daily_visits[-1]}")

    daily_visits[1] = 140
    print(f"After modifying index 1: {daily_visits}")

    daily_visits.append(175)
    print(f"After append(175): {daily_visits}")

    daily_visits.remove(110)
    print(f"After remove(110): {daily_visits}")

    print("Iterating through list values:")
    for value in daily_visits:
        print(f"- {value}")


def tuple_examples():
    print("\n=== 2) Tuples (Ordered + Immutable) ===")

    month_names = ("January", "February", "March")
    print(f"Tuple values: {month_names}")
    print(f"Item at index 1: {month_names[1]}")

    print("Attempting to modify tuple index 0...")
    try:
        month_names[0] = "Jan"
    except TypeError as error:
        print(f"TypeError observed: {error}")

    print("Tuples are useful when values should not change.")


def dictionary_examples():
    print("\n=== 3) Dictionaries (Key-Value Pairs) ===")

    product = {
        "name": "Notebook",
        "price": 49.99,
        "in_stock": True,
    }

    print(f"Original dictionary: {product}")
    print(f"Access by key 'name': {product['name']}")

    product["price"] = 44.99
    print(f"After updating 'price': {product}")

    product["category"] = "Stationery"
    print(f"After adding 'category': {product}")


def choosing_structure_examples():
    print("\n=== 4) Choosing the Right Structure ===")

    print("List: use when items may change (add, remove, reorder).")
    print("Tuple: use when items should stay fixed and protected.")
    print("Dictionary: use when named fields (keys) describe values.")


def main():
    print("Python Collections Demo: Lists, Tuples, Dictionaries")
    print("-----------------------------------------------------")

    list_examples()
    tuple_examples()
    dictionary_examples()
    choosing_structure_examples()

    print("\nDemo completed successfully.")


if __name__ == "__main__":
    main()
