"""
Data processing utilities for the project.

This module contains functions for cleaning and transforming data.
"""

import pandas as pd


def clean_sales_data(df):
    """
    Clean sales data by removing duplicates and handling missing values.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Raw sales data
        
    Returns:
    --------
    pandas.DataFrame
        Cleaned sales data
    """
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Ensure no missing critical fields
    df = df.dropna(subset=['customer_id', 'order_date'])
    
    # Fill missing quantities with 0
    df['quantity'] = df['quantity'].fillna(0)
    
    return df


def calculate_revenue(df):
    """
    Calculate total revenue from sales data.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Sales data with total_amount column
        
    Returns:
    --------
    float
        Total revenue
    """
    return df['total_amount'].sum()


def get_top_customers(df, n=5):
    """
    Get top N customers by total purchase amount.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Sales data
    n : int
        Number of top customers to return
        
    Returns:
    --------
    pandas.DataFrame
        Top N customers with their total purchases
    """
    top_customers = df.groupby('customer_id')['total_amount'].sum()
    top_customers = top_customers.sort_values(ascending=False).head(n)
    return top_customers.reset_index()


if __name__ == "__main__":
    # Example usage
    print("Data processing module loaded successfully!")
    print("Available functions:")
    print("  - clean_sales_data(df)")
    print("  - calculate_revenue(df)")
    print("  - get_top_customers(df, n=5)")
