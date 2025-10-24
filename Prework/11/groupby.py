import pandas as pd
 
# Example dataset for grouping
sales_data = {
    "Region":["North", "South", "East", "West", "North", "South"],
    "Product":["A", "A", "B", "B", "A", "B"],
    "Sales":[100, 150, 200, 130, 170, 160]  
}

sales_df = pd.DataFrame(sales_data)

# Group by 'Region' and calculate total sales
grouped_sales = sales_df.groupby('Region')["Sales"].sum()
print("Total Sales by Region:")
print(grouped_sales)

# Group by Region and Product, then calculate average sales
avg_sales = sales_df.groupby(['Region', 'Product'])["Sales"].mean()
print("Average Sales by Region and Product:")
print(avg_sales)