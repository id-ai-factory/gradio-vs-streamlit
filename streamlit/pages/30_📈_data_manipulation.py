import streamlit as st
import pandas as pd
from loguru import logger

df = pd.read_csv('common/user_data.csv')
df['date_registered'] = pd.to_datetime(df['date_registered'])

# 編集可能
# new_df = st.data_editor(
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

# logger.info(f"Jdoe is now: {new_df.loc[new_df["username"]=="jdoe"]}")