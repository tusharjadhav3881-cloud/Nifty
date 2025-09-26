import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Nifty_Stocks.csv")

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

st.title("Nifty Stocks Price Visualization")

# Select Category
categories = df['Category'].unique()
c = st.selectbox("Select Category:", categories)

# Filter dataframe by Category
d = df[df['Category'] == c]

# Select Symbol from filtered category
symbols = d['Symbol'].unique()
s = st.selectbox("Select Symbol:", symbols)

# Filter dataframe by Symbol within selected category
r = d[d['Symbol'] == s]

# Plot
fig, ax = plt.subplots()
sb.lineplot(x=r['Date'], y=r['Close'], ax=ax)
ax.set_title(f"Closing Price for {s} in Category {c}")
plt.xticks(rotation=90)
plt.tight_layout()

st.pyplot(fig)

