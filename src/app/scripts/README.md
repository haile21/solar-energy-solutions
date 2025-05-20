## Streamlit Dashboard for Global Insights

This dashboard visualizes metrics like GHI, GDP, and population across countries and regions.

### data_load
- It loads only the first 100 records from each dataset.

- Merges them.

- Saves the resulting 300-row DataFrame to a file named merged_data.csv inside the same data directory.

- Returns the merged DataFrame.
### 🔧 Features

- Interactive country and metric filters
- Boxplots by region
- Top-performing regions table
- Clean UI with dynamic visualizations

###  Running the App

```bash
pip install streamlit pandas matplotlib seaborn
streamlit run app/main.py



