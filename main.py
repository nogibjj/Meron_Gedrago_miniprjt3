from mylib.lib import load_dataset, describe_data, find_min_and_max
import polars as pl

loaded_data = load_dataset(
    "https://data.cdc.gov/api/views/95ax-ymtc/rows.csv?accessType=DOWNLOAD"
)
# furthering the cleaning this specific dataset
# data = loaded_data[
#    (loaded_data["STUB_NAME"] == "Total")
#    & (loaded_data["AGE"] == "All ages")
#    & (loaded_data["PANEL"] == "All drug overdose deaths")
#    & (loaded_data["UNIT"] == "Deaths per 100,000 resident population, crude")


data = loaded_data.filter(
    (pl.col("STUB_NAME") == "Total")
    & (pl.col("AGE") == "All ages")
    & (pl.col("PANEL") == "All drug overdose deaths")
    & (pl.col("UNIT") == "Deaths per 100,000 resident population, crude")
)
interested_column = data.select(["ESTIMATE"])

report_data = f"""
    ## Key statistics 
    - **Mean, Median and Standard Deviation**: {describe_data(interested_column)} 
    - **Range**: {find_min_and_max(interested_column)} 
    
    ## Death rate over the years
    ![Death rate over the years](Data_visual.png)

"""

with open("summary_report.md", "w") as f:
    f.write(report_data)
