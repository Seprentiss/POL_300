import ssl
import pandas as pd
ssl._create_default_https_context = ssl._create_unverified_context

path = "https://www.stat.purdue.edu/scs/docs/Cars.csv"

# You should use the path above to create a dataframe.
# Look at the columns in dataframe carefully and choose the columns you need.
# After calculate the sum, return it.

def create_csv_df(path):

    return pd.read_csv(path)

def calculate(dataframe):
    # using created csv file to calculate the sum
    sum = 0
    mpg_11 = dataframe[dataframe["mpg"] == 11]
    for engine in mpg_11["engine"]:
        sum += engine
    # return the sum you calculated
    return sum

print(calculate(create_csv_df(path)))