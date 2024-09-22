# import necessary packages
import polars as pl
import matplotlib.pyplot as plt


# create a function to read the dataset and filter the
def load_dataset(dataset):
    return pl.read_csv(dataset)


# calculate and print the summary statistics
def stats_overview(input_data):
    std = input_data.std()
    median = input_data.median()
    mean = input_data.mean()
    return f"The mean is {mean}; the median is {median}; the sd is {std}"


def describe_data(input_data):
    mean = pl.mean(input_data)
    median = pl.median(input_data)
    std = pl.std(input_data)
    return f"The mean is {mean}; the median is {median}; the sd is {std}"


# create a function to get the median of the data
def find_min_and_max(input_data):
    data_max = input_data.max()
    data_min = input_data.min()
    return f"The max is {data_max} and the min is {data_min}"


def create_graph(input_data):
    # Create visualization
    plt.scatter(input_data["YEAR"], input_data["ESTIMATE"])
    plt.xlabel("Year")
    plt.ylabel("Deaths per 100,000 resident population")
    plt.title("Death rates from overdose over year")
    plt.xticks(range(int(input_data["YEAR"].min()), int(input_data["YEAR"].max()), 2))
    plt.show()
