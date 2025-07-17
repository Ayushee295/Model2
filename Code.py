import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
df=pd.read_csv(r"D:\Summer course notes\GoogleStockPrices.csv", usecols=lambda col: col!='index')
print(df.head())
print()
print(df.describe)
print()
print(df.info)
print()
df['Date']=pd.to_datetime(df['Date'])
plt.plot(df['Date'],df['Open'],color='blue', label='open')
plt.plot(df['Date'],df['Close'],color='yellow', label='close')
plt.legend()
plt.show()
df['Date']=pd.to_datetime(df['Date'])
plt.plot(df['Date'],df['Volume'])
plt.show()
sns.heatmap(df.select_dtypes(include=np.number).corr(),annot=True,cbar=False)
plt.show()