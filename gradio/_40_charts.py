#%% Load files
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

with gr.Blocks(title="Charts") as demo:
    df = pd.read_csv('common/chart_data.csv')

    #%% Bar graph
    gr.BarPlot(df, x="Product Category", y="Sales")

    #%% Line plot
    df_melted = pd.melt(df, id_vars=['Month'], value_vars=['Profit', 'Sales'], 
                    var_name='Category', value_name='Amount')
    gr.LinePlot(df_melted, x="Month", y="Amount", color="Category")

    #%% Scatter Plot
    gr.ScatterPlot(df, x= "Average Price per Unit", y="Profit")

    #%% もっと良い感じのグラフ
    fig = px.bar(data_frame = df,
        x= "Product Category",
        y= ["Sales", "Profit"],
        animation_frame = "Month",
        labels={
            'Product Category': "商品類",
            'Sales': '売上',
            'profit': "利益",
            'Month': "月",
            'value': "価格",
        }
    )
    # If it is not moved to the top, it overlaps with the navigation buttons
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="left",
        x=0
    ))

    gr.Plot(fig)


    #%% Pie chart
    labels = df["Product Category"]
    sizes = df["Units Sold"]
    explode = [0]*len(sizes)  # "explode" the 1st slice 
    explode[1] = 0.1
    explode[8] = 0.2

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Ensure circle

    gr.Plot(fig1)

if __name__ == "__main__":
    demo.launch()