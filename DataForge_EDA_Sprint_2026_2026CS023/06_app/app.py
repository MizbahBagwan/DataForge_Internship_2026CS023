import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Automated EDA Dashboard")

uploaded = st.file_uploader("Upload CSV", type=["csv"])

if uploaded is not None:

    df = pd.read_csv(uploaded)

    st.header("Dataset Shape")
    st.write(df.shape)

    st.header("Columns")
    st.write(df.columns.tolist())

    st.header("Data Types")
    st.write(df.dtypes)

    st.header("Missing Values")
    st.write(df.isna().sum())

    st.header("Numeric Summary")
    st.write(df.describe())

    numeric = df.select_dtypes(include="number").columns

    if len(numeric) > 0:

        column = st.selectbox("Select Numeric Column", numeric)

        fig, ax = plt.subplots()

        ax.hist(df[column], bins=20)

        st.pyplot(fig)

    if "Sales" in df.columns:

        st.header("Top 10 Sales")

        st.write(df.nlargest(10, "Sales"))

        st.header("Bottom 10 Sales")

        st.write(df.nsmallest(10, "Sales"))

        st.success("Automatic Insight")

        st.write(
            f"Maximum Sales = {df['Sales'].max():,.2f}"
        ) 
