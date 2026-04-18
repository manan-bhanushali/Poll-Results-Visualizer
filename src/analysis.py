import pandas as pd

def load_data(path="data/poll_data.csv"):
    return pd.read_csv(path)

def clean_data(df):
    df = df.dropna()
    return df

def overall_analysis(df):
    counts = df["Product"].value_counts()
    percent = (counts / len(df)) * 100
    return percent

def region_analysis(df):
    table = pd.crosstab(df["Region"], df["Product"])
    percent = table.div(table.sum(axis=1), axis=0) * 100
    return percent

def save_summary(percent):
    percent.to_csv("outputs/summary.csv")