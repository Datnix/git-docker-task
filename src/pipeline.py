import pandas as pd

df = pd.read_csv("data/sales.csv")

# Validate data
if (df["quantity"] <= 0).any():
    raise ValueError("Quantity must be greater than 0")

if (df["price"] < 0).any():
    raise ValueError("Price must be greater than or equal to 0")

df["total"] = df["quantity"] * df["price"]

total_revenue = df["total"].sum()

print("Total Revenue:", total_revenue)

df.to_csv("data/processed_sales.csv", index=False)
