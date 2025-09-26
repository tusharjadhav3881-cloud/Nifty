import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

df=pd.read_csv("Nifty_Stocks.csv")

df.Date=df.Date.astype('datetime64[ns]')

print(df.Category.unique())
c=input("Enter Category Name:")
d=df[df.Category==c]

print(df.Symbol.unique())
s=input("Enter Symbol Name:")
r=df[df.Symbol==s]

sb.lineplot(x=r.Date,y=r.Close)
plt.xticks(rotation=90)
plt.show()
