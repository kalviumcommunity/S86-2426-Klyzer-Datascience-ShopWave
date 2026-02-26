"""
Milestone script: first standalone Python script for simple data analysis.

This file demonstrates script execution flow from top to bottom using small,
in-memory sample data and basic calculations.
"""


def analyze_daily_sales(daily_sales):
    """Return basic statistics for a list of daily sales values."""
    total_sales = sum(daily_sales)
    number_of_days = len(daily_sales)
    average_sales = total_sales / number_of_days
    highest_sales = max(daily_sales)
    lowest_sales = min(daily_sales)

    return {
        "total_sales": total_sales,
        "number_of_days": number_of_days,
        "average_sales": average_sales,
        "highest_sales": highest_sales,
        "lowest_sales": lowest_sales,
    }


def main():
    print("=== First Python Script for Data Analysis ===")

    daily_sales = [1200, 1450, 980, 1750, 1600, 1100, 1900]
    print(f"Input daily sales data: {daily_sales}")

    results = analyze_daily_sales(daily_sales)

    print("\nAnalysis Results:")
    print(f"- Number of days: {results['number_of_days']}")
    print(f"- Total sales: {results['total_sales']}")
    print(f"- Average daily sales: {results['average_sales']:.2f}")
    print(f"- Highest day sales: {results['highest_sales']}")
    print(f"- Lowest day sales: {results['lowest_sales']}")

    print("\nScript completed successfully.")


if __name__ == "__main__":
    main()
