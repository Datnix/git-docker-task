import pandas as pd

df = pd.read_csv("data/sales.csv")

df["total"] = df["quantity"] * df["price"]

total_revenue = df["total"].sum()
print("Total Revenue: ", total_revenue)

df.to_csv("data/processed_sales.csv", index=False)
