import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import keras
from datetime import datetime
df=pd.read_csv(r"D:\Summer course notes\GoogleStockPrices.csv", usecols=lambda col: col!='index')
print(df.head())
print()
print(df.describe)
print()
print(df.info)
print()