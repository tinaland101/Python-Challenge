



import pandas as pd

 



df = pd.read_csv("/System/Volumes/Data/Users/christinaland/Library/Mobile Documents/com~apple~CloudDocs/PyBank/Resources/budget_data.csv")

 

# head display

print(df.head())

# 1. Total number of months included in the dataset

total_months = df.shape[0]

print(f"Total Months: {total_months}")

 

# 2. Net total amount of "Profit/Losses" over the entire period

net_total = df['Profit/Losses'].sum()

print(f"Net Total Profit/Losses: ${net_total}")

 

# 3. Calculate the changes in "Profit/Losses" over the entire period

df['Change'] = df['Profit/Losses'].diff()

 

# Average of those changes

average_change = df['Change'].mean()

print(f"Average Change in Profit/Losses: ${average_change:.2f}")

 

# 4. Greatest increase in profits

greatest_increase = df.loc[df['Change'].idxmax()]

increase_date = greatest_increase['Date']

increase_amount = greatest_increase['Change']

print(f"Greatest Increase in Profits: {increase_date} (${increase_amount})")

 

# 5. Greatest decrease in profits

greatest_decrease = df.loc[df['Change'].idxmin()]

decrease_date = greatest_decrease['Date']

decrease_amount = greatest_decrease['Change']

print(f"Greatest Decrease in Profits: {decrease_date} (${decrease_amount})")

 
