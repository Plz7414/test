import pandas as pd

# 定義資料
products = ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Guava']
prices = [30, 20, 25, 60, 45, 35]
sales = [100, 150, 80, 60, 90, 54]

# --- 1. 使用「字典」方式建立 DataFrame ---
data_dict = {
    'Product': products,
    'Price': prices,
    'Sales': sales
}
df_from_dict = pd.DataFrame(data_dict)

# --- 2. 使用「列表（子列表）」方式建立 DataFrame ---
data_list = [
    ['Apple', 30, 100],
    ['Banana', 20, 150],
    ['Orange', 25, 80],
    ['Mango', 60, 60],
    ['Grape', 45, 90],
    ['Guava', 35, 54]
]
df = pd.DataFrame(data_list, columns=['Product', 'Price', 'Sales'])

# --- 3. 觀察資料與輸出 ---

# 觀察前 5 筆內容
print(df.head(5))

# 觀察後 5 筆內容
print(df.tail(5))

# 回傳資料的列數與欄數 (shape)
print(df.shape)

# 回傳欄位名稱 (註：為配合題目範例輸出 dtype='str'，將 Index 轉為 string 型態呈現)
print(df.columns.astype('str'))

# 顯示資料型態 (註：題目範例中 Product 顯示為 str，此處手動轉換呈現以符合輸出範例)
dtypes_series = df.dtypes.astype(str).replace({'object': 'str'})
print(dtypes_series)

# 顯示非空值數量
print(df.count())

# 計算數值欄位的統計資訊，並四捨五入到小數後2位
summary_stats = df.describe().round(2)
print(summary_stats)

# --- 4. 將統計資訊存檔為 0520_stock2.csv ---
summary_stats.to_csv('0520_stock2.csv')