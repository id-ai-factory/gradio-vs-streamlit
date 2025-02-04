#%% Load files
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt


with gr.Blocks(title="File Comparator") as demo:
    df = pd.read_csv('common/chart_data.csv')

    #%% Bar graph
    gr.BarPlot(df, x="Product Category", y="Sales")

    #%% Line plot
    df_melted = pd.melt(df, id_vars=['Month'], value_vars=['Profit', 'Sales'], 
                    var_name='Category', value_name='Amount')
    gr.LinePlot(df_melted, x="Month", y="Amount", color="Category")

    #%% Scatter Plot
    gr.ScatterPlot(df, x= "Average Price per Unit", y="Profit")

    #%% Pie chart
    labels = df["Product Category"]
    sizes = df["Units Sold"]
    explode = [0]*len(sizes)  # only "explode" the 2nd slice (i.e. 'Hogs')
    explode[1] = 0.1
    explode[8] = 0.2

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    gr.Plot(fig1)

demo.launch()