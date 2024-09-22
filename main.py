from mylib.lib import load_dataset, describe_data, find_min_and_max, create_graph


loaded_data = load_dataset(
    "https://data.cdc.gov/api/views/95ax-ymtc/rows.csv?accessType=DOWNLOAD"
)
# furthering the cleaning this specific dataset
data = loaded_data[
    (loaded_data["STUB_NAME"] == "Total")
    & (loaded_data["AGE"] == "All ages")
    & (loaded_data["PANEL"] == "All drug overdose deaths")
    & (loaded_data["UNIT"] == "Deaths per 100,000 resident population, crude")
]
interested_column = data["ESTIMATE"]
print(describe_data(interested_column))
print(find_min_and_max(interested_column))
create_graph(data)
