# Bài 4.3
import pandas as pd
import numpy as np

ser1=pd.Series(list('abcdefghimnopqrstuvwxyz'))
ser2=pd.Series(np.arange(26))

result=pd.concat([ser1,ser2],axis=0)
result