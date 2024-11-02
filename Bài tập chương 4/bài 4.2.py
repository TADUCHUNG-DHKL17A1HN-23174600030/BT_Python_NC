# Bài 4.2
import pandas as pd
import numpy as np

# Tạo danh sách và mảng
mylist = list('abcdefghijklmnopqrstuvwxyz')
myarr = np.arange(26)

# Tạo DataFrame
M = pd.DataFrame({"list": mylist, "myarr": myarr})

# Hiển thị DataFrame
print(M)