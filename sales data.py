import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("All packages are installed successfully!")

#just to make sure all the packages are installed before start.

import pandas as pd

# make sure the path of the csv are correct
try:
    df = pd.read_csv('C:/Users/AsUs/Desktop/sales_data.csv')  # for Windows

    print(df.head())  # just to show the files already found or not
except FileNotFoundError:
    print("Error: Fail CSV tidak dijumpai. Sila semak semula path atau nama fail.")
#if not found, the terminal output will show this sentence

#Then start to query the data (calculate the TOTAL SALES OF PRODUCTS)
# Add a 'Total' column
df['Total'] = df['Quantity'] * df['Price']

# Display the updated dataset
print(df.head())
# Total sales by product
total_sales_per_product = df.groupby('Product')['Total'].sum()

print(total_sales_per_product) #Just in the terminal output appear the product and their total sales


#Start to import matpltolibrary

import matplotlib.pyplot as plt
import seaborn as sns

# Create a bar plot of total sales per product
plt.figure(figsize=(8, 6))
sns.barplot(x=total_sales_per_product.index, y=total_sales_per_product.values)
plt.title('Total Sales per Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Group sales by date
daily_sales = df.groupby(df['Date'].dt.date)['Total'].sum()

# Create a line plot of sales over time
plt.figure(figsize=(10, 6))
daily_sales.plot(kind='line')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# Scatter plot between Price and Total Sales
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['Price'], y=df['Total'])
plt.title('Correlation Between Price and Total Sales')
plt.xlabel('Product Price')
plt.ylabel('Total Sales')
plt.show()

# Save the updated dataset with the 'Total' column
df.to_csv('C:/Users/AsUs/Desktop/sales_analysis_result.csv', index=False)



