import streamlit as st
import pandas as pd

df = pd.read_csv('common/user_data.csv')
df['date_registered'] = pd.to_datetime(df['date_registered'])

# 編集可能
# st.data_editor(
# 編集不可
st.dataframe(
    df,
    column_config={
        "date_registered":st.column_config.DatetimeColumn(
            "日付",
            format="YYYY年MM月DD日 HH:mm:ss"
        ),
        "credits_used":None
    }
) 