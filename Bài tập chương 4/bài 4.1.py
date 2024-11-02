# Bài 4.1
import pandas as pd
import numpy as np

# Tạo danh sách, mảng và từ điển
mylist = list('abcdefghijklmnopqrstuvw')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

# Tạo chuỗi pandas từ danh sách
series_from_list = pd.Series(mylist)

# Tạo chuỗi pandas từ mảng
series_from_array = pd.Series(myarr)

# Tạo chuỗi pandas từ từ điển
series_from_dict = pd.Series(mydict)

# Hiển thị kết quả
print("Series từ danh sách:")
print(series_from_list)
print("\nSeries từ mảng:")
print(series_from_array)
print("\nSeries từ từ điển:")
print(series_from_dict)