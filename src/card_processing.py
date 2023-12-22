import pandas as pd
import pickle

file_path = "/home/cubes/codebase/mtg_card_tracker/data/Inventory_Finn091_2023.October.07.csv"
pickle_file_name = "clean_card_df.pickle"

# Read into dataframe and print first 10
df = pd.read_csv(file_path)
print(df.head(10))

# Remove unused columns
df.drop(columns=['Tradelist Count', 'Condition', 'Altered Art', 'Misprint', 'Signed', 'Artist Proof', 'Textless', 'Promo', 'Printing Note', 'Tags', 'My Price'], inplace=True)
print(df.head(10))

# Convert 'Price' column to number
format_money  = lambda x: float(x.replace('$', ''))
df['Price'] = df['Price'].apply(format_money)

# Multiply the count times the Price to get a Value for that card
df['Value']  = df['Count'] *  df['Price']
print(df.head(10))

# Print 10 most valuable cards
print("Most valuable cards")
print(df.sort_values('Price', axis=0, ascending=False).head(10))

# Count number of cards worth more than $2
print(f'Number of Unique cards: {df["Count"].count()}')
print(f'Total cards: {df["Count"].sum()}')
print(f'Cards worth more than $2: {df[df["Price"] >= 2.0]["Count"].sum()}')

# Sum the Value column to get total collection value
total_value = df['Value'].sum()
print(f"Total Value: ${total_value:.2f}")
print(f"Value of cards worth more than $2: ${df[df['Price'] >= 2.0]['Value'].sum():.2f}")

with open(pickle_file_name, "wb") as file:
    pickle.dump(df, file)
