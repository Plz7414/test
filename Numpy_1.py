import numpy as np
import csv


data_list = []
with open('Stock_1.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:

        data_list.append([
            float(row[1]),
            int(row[2]),
            int(row[3]),
            int(row[4]),
            float(row[5])
        ])


data_array = np.array(data_list)

prices = data_array[:, 0]
stocks = data_array[:, 1:4]
discounts = data_array[:, 4]


total_stock = np.sum(stocks, axis=1)

stock_value = total_stock * prices


discounted_price = prices * discounts


is_popular = total_stock > np.mean(total_stock)
popularity_label = np.where(is_popular, 'Yes', 'No')


with open('Stock_ok.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(header + ['Total_Stock', 'Stock_Value', 'Discounted_Price', 'Is_Popular'])


    with open('Stock_1.csv', 'r', encoding='utf-8') as f_old:
        old_reader = csv.reader(f_old)
        next(old_reader) 
        for i, row in enumerate(old_reader):
            new_row = row + [
                int(total_stock[i]),
                f"{stock_value[i]:.2f}",
                f"{discounted_price[i]:.2f}",
                popularity_label[i]
            ]
            writer.writerow(new_row)

print("分析完成！結果已存至 Stock_ok.csv")