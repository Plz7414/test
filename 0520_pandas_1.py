import pandas as pd

# 1. 先用 list 建立 stock1
stock1_list = [120, 80, None, 60, 95, None, 110]
stock1 = pd.Series(stock1_list)

# 2. 加入索引建立 stock2
index_list = ["Apple", "Banana", "Orange", "Mango", "Grape", "Peach", "Melon"]
stock2 = pd.Series(stock1_list, index=index_list)

# 3. 將 stock2 轉為字典 stock3
stock3 = stock2.to_dict()

# --- 開始列印輸出範例內容 ---

# 輸出 stock1
print("stock1")
print(stock1)
print()

# 輸出 stock2
print("stock2")
print(stock2)
print()

# 輸出 stock3
print("stock3")
print(stock3)
print()

# 輸出 Banana 的庫存值
print(f"Banana 庫存： {stock2['Banana']}\n")

# 計算與檢查缺失值
print("缺失值檢查：")
null_check = stock2.isnull()
print(null_check)
print()

print(f"缺失值數量： {null_check.sum()}")

# 4. 把 stock2 存檔為 0520_stock.csv（不包含 header，符合 Series 預設存檔格式）
stock2.to_csv("0520_stock.csv", header=False)