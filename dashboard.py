import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(layout="wide")

st.title("🔥 Value Bets Dashboard")

engine = create_engine("sqlite:///bets.db")

try:
    df = pd.read_sql("SELECT * FROM bets ORDER BY date DESC", engine)

    if df.empty:
        st.warning("Sem dados ainda")
    else:
        st.dataframe(df)

        st.subheader("🎯 Value Bets")

        value = df[
            (df["value_home"] > 0.05) |
            (df["value_draw"] > 0.05) |
            (df["value_away"] > 0.05)
        ]

        st.dataframe(value)

except Exception as e:
    st.warning("Banco ainda não criado ou erro:")
    st.text(str(e))