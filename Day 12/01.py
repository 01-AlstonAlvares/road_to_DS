#Mini Task Requirements
    #Sort sales in descending order
    #Filter for Sales > 30 and after Jan 1, 2024
    #Group by month and calculate average sales
    #Bonus: Save monthly average sales to a CSV

import pandas as pd

df = pd.read_csv("advanced_pandas_day12.csv")
df["Date"] = pd.to_datetime(df["Date"])

#sort by sales descending
def sorted_sales():
    sorted_df = df.sort_values(by="Sales", ascending=False)
    print("Top 5 Records by Sales:")
    print(sorted_df.head())

sorted_sales()

# Filter rows where Sales > 30 and Date after Jan 2024

def filtered_rows():
    filtered = df[(df["Sales"] > 30) & (df["Date"] > "2024-01-01")]
    print("\n Filtered Rows:")
    print(filtered)

filtered_rows()

#grouping
def grrp():
    df["Month"] = df["Date"].dt.to_period("M")
    monthly_avg = df.groupby("Month")["Sales"].mean()
    print("\n🔹 Monthly Average Sales:")
    print(monthly_avg)
    monthly_avg.to_csv("monthly_avg_sales.csv")
    print("\n Monthly average sales saved to 'monthly_avg_sales.csv'")

grrp()

# Add a new column flagging High Sales
df["High_Sales"] = df["Sales"].apply(lambda x: "Yes" if x > 200 else "No")
print(df.head())


