#Mini Task
    #Load the provided CSV.
    #Plot one line chart and one histogram.
    #Try styling them with titles, labels, and different colors.
    #Save one of your plots to a PNG file.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("time_series_day11.csv")
df["Date"] = pd.to_datetime(df["Date"])  # Ensure it's datetime
df.set_index("Date", inplace=True) # Set Date as index

# 2. Plot original daily sales
plt.figure(figsize=(10, 4))
df["Sales"].plot()
plt.title("Daily Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# 3. Resample to Monthly Average Sales

monthly_avg = df["Sales"].resample("ME").mean()

plt.figure(figsize=(10, 4))
monthly_avg.plot(color='orange')
plt.title("Monthly Average Sales")
plt.xlabel("Month")
plt.ylabel("Avg Sales")
plt.grid(True)
plt.show()

# 4. Rolling Average (7-day window)
df["Rolling_7D"] = df["Sales"].rolling(window= 9).mean()
plt.figure(figsize=(10, 4))
df[["Sales", "Rolling_7D"]].plot()
plt.title("7-Day Rolling Average of Sales")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# 5. Filter data for a specific range (e.g., Jan–Jun 2024)
filtered_df = df["2024-01":"2024-06"]

plt.figure(figsize=(10, 4))
filtered_df["Sales"].plot()
plt.title("Sales from Jan to Jun 2024")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.show()