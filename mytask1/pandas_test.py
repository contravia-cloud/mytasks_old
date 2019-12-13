from __future__ import print_function

import pandas as pd

california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")
# california_housing_dataframe.describe()
print(california_housing_dataframe.head())
# california_housing_dataframe.hist('housing_median_age')