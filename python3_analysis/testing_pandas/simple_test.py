from time import time

start_load = time()
import pandas as pd
print(time() - start_load,"loading pandas")

start_init = time()
pd.DataFrame()
print(time() - start_init,"creating a single dataframe")

