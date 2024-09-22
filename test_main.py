from main import load_dataset, describe_data, find_min_and_max


# assinging a test data csv that has a very simple data with the from 1921 to 2023

test_data = load_dataset("test.csv")
column_of_int = test_data.select(["Number of employees"])


def test_load_data():
    test_data = load_dataset("test.csv")
    assert test_data is not None


def test_stats_describe():
    summary_stats = describe_data(column_of_int)
    assert summary_stats is not None


def test_range():
    range_stats = find_min_and_max(column_of_int)
    assert range_stats is not None


if __name__ == "__main__":
    test_load_data()
    test_stats_describe()
    test_range()
