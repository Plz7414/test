import pandas as pd

file_path = "Grocery_Inventory_and_Sales_Dataset.csv"
df = pd.read_csv(file_path)

df["Unit_Price"] = (
    df["Unit_Price"].astype(str).str.replace("$", "").str.strip().astype(float)
)

print("--- (1) 每個商品的總庫存價值 (全部商品) ---")
df["Total_Inventory_Value"] = df["Stock_Quantity"] * df["Unit_Price"]

pd.set_option("display.max_rows", None)

print(df[["Product_Name", "Total_Inventory_Value"]])
print("\n" + "=" * 50 + "\n")


print("--- (2) 最暢銷的商品 ---")
sales_by_product = df.groupby("Product_Name")["Sales_Volume"].sum().reset_index()
best_seller = sales_by_product.sort_values(
    by="Sales_Volume", ascending=False
).iloc[0]
print(f"最暢銷的商品是：【{best_seller['Product_Name']}】")
print(f"總銷售量為：{best_seller['Sales_Volume']:,} 件")
print("\n" + "=" * 50 + "\n")


print("--- (3) 打 9 折後的收入 ---")
df["Revenue"] = df["Sales_Volume"] * df["Unit_Price"]
total_original_revenue = df["Revenue"].sum()
discounted_total_revenue = total_original_revenue * 0.9

print(f"原始總收入：${total_original_revenue:,.2f}")
print(f"打 9 折後的總收入：${discounted_total_revenue:,.2f}")