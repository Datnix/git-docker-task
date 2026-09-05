import pandas as pd


def test_total_revenue():
    data = {"quantity": [2, 3], "price": [100, 200]}

    df = pd.DataFrame(data)

    df["total"] = df["quantity"] * df["price"]

    total_revenue = df["total"].sum()

    assert total_revenue == 800
