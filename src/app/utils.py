import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import os

@st.cache_data
def load_data():
    current_dir = os.path.dirname(__file__)  # folder where main.py is
    data_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'data'))

    benin = pd.read_csv(os.path.join(data_dir, "benin_clean.csv"))
    benin["country"] = "Benin"

    sierraleone = pd.read_csv(os.path.join(data_dir, "sierraleone_clean.csv"))
    sierraleone["country"] = "Sierra Leone"

    togo = pd.read_csv(os.path.join(data_dir, "togo_clean.csv"))
    togo["country"] = "Togo"

    # Keep only 100 records from each
    benin = benin.head(100)
    sierraleone = sierraleone.head(100)
    togo = togo.head(100)

    # Merge and clean
    df = pd.concat([benin, sierraleone, togo], ignore_index=True)
    df.columns = df.columns.str.strip().str.lower()
    #st.write(df.columns)
    # Rename columns to be consistent
    rename_map = {}
    for col in df.columns:
        if col in ['region name', 'region', 'adm1', 'admin1']:
            rename_map[col] = 'region'
        if col in ['ghi', 'ghi (kwh/m²/day)', 'global horizontal irradiation']:
            rename_map[col] = 'ghi'

    df = df.rename(columns=rename_map)

    # Optionally save merged file
    output_path = os.path.join(data_dir, 'merged_data.csv')
    df.to_csv(output_path, index=False)

    return df


def plot_boxplot(df, metric):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x="country", y=metric, ax=ax)
    ax.set_title(f"{metric} Distribution by Region")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

# def get_top_regions(df, metric, top_n=5):
#     top = df.groupby("country")[metric].mean().sort_values(ascending=False).head(top_n)
#     return top.reset_index().rename(columns={metric: f"Avg {metric}"})
def get_top_regions(df):
    if 'ws' not in df.columns or 'ghi' not in df.columns:
        raise KeyError("Required columns 'ws' or 'ghi' not found.")

    return (
        df.groupby("ws")["ghi"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
        .head(10)
    )

