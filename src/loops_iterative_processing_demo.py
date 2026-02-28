"""
Milestone script: using for and while loops for iterative data processing.

This script demonstrates:
- for loops with range and lists
- while loops with condition-based repetition
- loop control using break and continue
- safe patterns to avoid infinite loops
"""


def for_loop_with_range():
    print("=== 1) for Loop with range ===")

    running_total = 0
    for day_number in range(1, 6):
        running_total += day_number
        print(f"Day {day_number}: running_total = {running_total}")

    print(f"Final total after range loop: {running_total}")


def for_loop_with_list():
    print("\n=== 2) for Loop with a List ===")

    sales_values = [12, 19, 7, 25, 14]

    for index, value in enumerate(sales_values, start=1):
        print(f"Record {index}: sales value = {value}")

    average_value = sum(sales_values) / len(sales_values)
    print(f"Average sales value: {average_value:.2f}")


def while_loop_condition_based():
    print("\n=== 3) while Loop (Condition-Based) ===")

    remaining_attempts = 3

    while remaining_attempts > 0:
        print(f"Attempts remaining: {remaining_attempts}")
        remaining_attempts -= 1

    print("Loop ended because condition became FALSE.")


def control_flow_break_continue():
    print("\n=== 4) Loop Control: break and continue ===")

    print("continue example (skip even numbers):")
    for value in range(1, 8):
        if value % 2 == 0:
            continue
        print(f"Processed odd value: {value}")

    print("\nbreak example (stop at first value > 20):")
    data_points = [8, 14, 19, 23, 31, 7]
    for point in data_points:
        if point > 20:
            print(f"Stopping early at point {point} using break")
            break
        print(f"Accepted point: {point}")


def infinite_loop_prevention():
    print("\n=== 5) Avoiding Infinite Loops ===")

    print("Unsafe pattern (example only, not executed):")
    print("while counter < 5:")
    print("    print(counter)")
    print("# Missing counter update can cause an infinite loop")

    print("\nSafe pattern (updates condition variable):")
    counter = 0
    while counter < 5:
        print(f"counter = {counter}")
        counter += 1

    print("Safe loop terminated correctly.")


def main():
    print("Python Loops for Iterative Data Processing Demo")
    print("-----------------------------------------------")

    for_loop_with_range()
    for_loop_with_list()
    while_loop_condition_based()
    control_flow_break_continue()
    infinite_loop_prevention()

    print("\nDemo completed successfully.")


if __name__ == "__main__":
    main()
