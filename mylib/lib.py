# import packages
import pandas as pd
import matplotlib.pyplot as plt


# create a function to read the dataset and filter the
def load_dataset(dataset):
    data_set = pd.read_csv(dataset)
    return data_set


# calculate and print the summary statistics
def describe_data(input_data):
    mean = input_data.mean()
    median = input_data.median()
    std = input_data.std()
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
