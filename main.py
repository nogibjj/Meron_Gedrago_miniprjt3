from mylib.lib import load_dataset, describe_data, find_min_and_max, create_graph
import polars as pl

loaded_data = load_dataset(
    "https://data.cdc.gov/api/views/95ax-ymtc/rows.csv?accessType=DOWNLOAD"
)

# furthering the cleaning this specific dataset
data = loaded_data.filter(
    (pl.col("STUB_NAME") == "Total")
    & (pl.col("AGE") == "All ages")
    & (pl.col("PANEL") == "All drug overdose deaths")
    & (pl.col("UNIT") == "Deaths per 100,000 resident population, crude")
)
interested_column = data.select(["ESTIMATE"])

report_data = f"""
#Key statistics 
- **Mean, Median and Standard Deviation**: {describe_data(interested_column)} 
- **Range**: {find_min_and_max(interested_column)} 

# Death rate oßver the years 
<img src="./Data_visual.png" alt="Death rate over the years" style="width:600px;">
"""

create_graph(data)
with open("summary_report.md", "w") as f:
    f.write(report_data)
