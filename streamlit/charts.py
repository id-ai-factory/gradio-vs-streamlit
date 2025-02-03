#%% 読み込み
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('common/chart_data.csv')
#%%　棒グラフ

st.bar_chart(df, x="Product Category", y="Sales")
#%% 線グラフ

df_S = df.groupby("Month", as_index=False).sum()
st.area_chart(df_S, x = "Month", y = ["Sales", "Profit"])

#%% 散布図

st.scatter_chart(df, x= "Average Price per Unit", y="Profit", size = "Sales")
#%% パイチャート

labels = df["Product Category"]
sizes = df["Units Sold"]
explode = [0]*len(sizes)  # only "explode" the 2nd slice (i.e. 'Hogs')
explode[1] = 0.1
explode[8] = 0.2

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#%%
st.pyplot(fig1)


