import streamlit as st
import pandas as pd
import plotly.express as px
from src.analysis import load_data, clean_data, overall_analysis, region_analysis

st.title("📊 Poll Results Visualizer")

# Load data
df = load_data()
df = clean_data(df)

st.subheader("Dataset Preview")
st.write(df.head())

# Overall Analysis
overall = overall_analysis(df)

st.subheader("Overall Preference")
fig1 = px.bar(x=overall.index, y=overall.values, labels={"x": "Product", "y": "Percentage"})
st.plotly_chart(fig1)

# Pie Chart
fig2 = px.pie(values=overall.values, names=overall.index, title="Vote Share")
st.plotly_chart(fig2)

# Region Analysis
region = region_analysis(df)

st.subheader("Region-wise Analysis")
st.write(region)

fig3 = px.bar(region, barmode="stack")
st.plotly_chart(fig3)

# Filter option
st.sidebar.header("Filters")
region_filter = st.sidebar.selectbox("Select Region", df["Region"].unique())

filtered_df = df[df["Region"] == region_filter]

st.subheader(f"Filtered Data: {region_filter}")
st.write(filtered_df.head())