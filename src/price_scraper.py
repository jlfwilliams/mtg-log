import pickle
import pandas as pd

pickle_file_name = "clean_card_df.pickle"

# Read in pickle file of cleaned exported card data
with open(pickle_file_name, "rb") as file:
    df = pickle.load(file)
print(df.head(10))


