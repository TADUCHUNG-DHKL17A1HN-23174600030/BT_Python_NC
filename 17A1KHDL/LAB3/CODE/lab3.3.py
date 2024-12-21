import pandas as pd
stocks1=pd.read_csv('D:/17A3KHDL/LAB3/DATA/stocks1.csv')
stocks2=pd.read_csv('D:/17A3KHDL/LAB3/DATA/stocks2.csv')

# Gồm stocks 1 với stock2 2
stocks=pd.concat([stocks1,stocks2], ignore_index=True)
print(stocks)

# TÍNH GIÁ TRỊ TRUNG BÌNH (OPEN,HIGH,LOW,CLOSE) CHO MỖI NGÀY
stocks['date'] = pd.to_datetime(stocks['date'])
stocks_ngay = stocks.groupby('date')[['open', 'high', 'low', 'close']].mean()
print('Giá trung bình (open, high, low, close) cho mỗi ngày :')
print(stocks_ngay)

# Hiển thị 5 dòng đầu tiên của kết quả
print('Hiển thi 5 dòng đầu của kết quả :')
print(stocks.head())

