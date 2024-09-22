# import necessary packages
import polars as pl
import matplotlib.pyplot as plt


# create a function to read the dataset and filter the
def load_dataset(dataset):
    return pl.read_csv(dataset)


# calculate and print the summary statistics
def describe_data(input_data):
    std = round(input_data.std().item(), 2)
    median = round(input_data.median().item(), 2)
    mean = round(input_data.mean().item(), 2)
    return f"The mean is {mean}; the median is {median}; the sd is {std}"


# create a function to get the median of the data
def find_min_and_max(input_data):
    data_max = input_data.max()
    data_min = input_data.min()
    return f"The max is {data_max.item()} and the min is {data_min.item()}"


def create_graph(input_data):
    # Create visualization
    plt.scatter(input_data.select(["YEAR"]), input_data.select(["ESTIMATE"]))
    plt.xlabel("Year")
    plt.ylabel("Deaths per 100,000 resident population")
    plt.title("Death rates from overdose over year")
    plt.xticks(range(int(input_data["YEAR"].min()), int(input_data["YEAR"].max()), 2))
    plt.show()
