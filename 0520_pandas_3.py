import pandas as pd

# 1. 讀取資料
df = pd.read_csv('SuperMarket Analysis.csv')

# 檢視資料筆數與前幾筆內容
print(f"資料筆數 (列數, 欄位數): {df.shape}")
print("\n--- 前 5 筆資料內容 ---")
print(df.head())

# 2. 篩選出 Branch 為 A (資料集中為 Alex) 且 Customer type 為 Member 的交易資料
# 註：本資料集之 'Alex' 即代表 A 分店
filtered_df = df[(df['Branch'] == 'Alex') & (df['Customer type'] == 'Member')]
print(f"\n篩選後 (Branch為A 且 為Member) 的交易筆數: {len(filtered_df)} 筆")

# 3. 以 Product line 為單位，計算各產品線的總銷售額（Sales）與平均評分（Rating），計算至小數後2位
product_summary = df.groupby('Product line').agg(
    Total_Sales=('Sales', 'sum'),
    Average_Rating=('Rating', 'mean')
).round(2).reset_index()

print("\n--- 各產品線銷售與評分彙總 ---")
print(product_summary)

# 找出總銷售額最高的產品線
top_product = product_summary.loc[product_summary['Total_Sales'].idxmax()]
print(f"\n🏆 總銷售額最高的產品線: {top_product['Product line']}，總銷售額為: {top_product['Total_Sales']}")

# 4. 依 City 與 Gender 分組，計算平均銷售額與交易筆數
city_gender_summary = df.groupby(['City', 'Gender']).agg(
    Average_Sales=('Sales', 'mean'),
    Transaction_Count=('Invoice ID', 'count')
).round(2).reset_index()

print("\n--- 依 City 與 Gender 分組分析 ---")
print(city_gender_summary)

# 5. 將產品線的彙總結果輸出為 0520_pandas_3OK.CSV 檔案
product_summary.to_csv('0520_pandas_3OK.CSV', index=False, encoding='utf-8-sig')
print("\n產出成功：結果已儲存至 '0520_pandas_3OK.CSV'")