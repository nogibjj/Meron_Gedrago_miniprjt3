# import necessary packages
import polars as pl
import matplotlib.pyplot as plt


# create a function to read the dataset and filter the
def load_dataset(dataset):
    data_set = pl.read_csv(dataset)
    return data_set


# calculate and print the summary statistics
def describe_data(input_data):
    mean = pl.mean(input_data)
    median = pl.median(input_data)
    std = pl.std(input_data)
    return f"The mean is {mean}; the median is {median}; the sd is {std}"


# create a function to get the median of the data
def find_min_and_max(input_data):
    data_max = pl.max(input_data)
    data_min = pl.min(input_data)
    return f"The max is {data_max} and the min is {data_min}"


def create_graph(input_data):
    # Create visualization
    plt.scatter(input_data["YEAR"], input_data["ESTIMATE"])
    plt.xlabel("Year")
    plt.ylabel("Deaths per 100,000 resident population")
    plt.title("Death rates from overdose over year")
    plt.xticks(range(int(input_data["YEAR"].min()), int(input_data["YEAR"].max()), 2))
    plt.show()
