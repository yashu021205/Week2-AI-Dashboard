import streamlit as st
import pandas as pd
import plotly.express as px

st.title("AI Dashboard - Titanic Dataset")

df = pd.read_csv("Titanic-Dataset.csv")

st.subheader("Dataset Overview")
st.write(df.head())

st.subheader("Data Cleaning")
df.fillna(0, inplace=True)
st.success("Missing values handled")

st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Passengers", len(df))
col2.metric("Survived", int(df["Survived"].sum()))
col3.metric("Average Age", round(df["Age"].mean(), 2))

gender = st.selectbox(
    "Select Gender",
    df["Sex"].unique()
)

filtered = df[df["Sex"] == gender]

st.subheader("Visualizations")

fig1 = px.bar(filtered, x="Pclass")
st.plotly_chart(fig1)

fig2 = px.pie(filtered, names="Survived")
st.plotly_chart(fig2)

fig3 = px.histogram(filtered, x="Age")
st.plotly_chart(fig3)

fig4 = px.scatter(filtered, x="Age", y="Fare")
st.plotly_chart(fig4)

fig5 = px.box(filtered, y="Fare")
st.plotly_chart(fig5)