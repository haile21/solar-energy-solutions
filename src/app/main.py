import streamlit as st

from utils import load_data, get_top_regions, plot_boxplot   # your helpers

# ───────────────────────────────────────────────────────────────
# Page / layout
# ───────────────────────────────────────────────────────────────
st.set_page_config(
    layout="wide",
    page_title="Global Insights Dashboard"
)

st.title("Global Insights Dashboard")

# ───────────────────────────────────────────────────────────────
# Data
# ───────────────────────────────────────────────────────────────
df = load_data()                       # returns column-names in lower-case
country_list = sorted(df["country"].unique())

# ───────────────────────────────────────────────────────────────
# Sidebar filters
# ───────────────────────────────────────────────────────────────
st.sidebar.header("Filters")

selected_countries = st.sidebar.multiselect(
    "Select countries",
    options=country_list,
    default=country_list[:5]
)

metric = st.sidebar.selectbox(
    "Select metric",
    options=["ghi", "gdp", "population"]      # ensure lower-case to match df
)

# ───────────────────────────────────────────────────────────────
# Filter data
# ───────────────────────────────────────────────────────────────
filtered_df = df[df["country"].isin(selected_countries)]

# ───────────────────────────────────────────────────────────────
# Plots & tables
# ───────────────────────────────────────────────────────────────
st.subheader(f"{metric.upper()} distribution by region")
plot_boxplot(filtered_df, metric)            # uses lower-case "region"

st.subheader("🏆 Top regions (average value)")
top_regions = get_top_regions(filtered_df)   # use filtered data
st.dataframe(top_regions, use_container_width=True)
