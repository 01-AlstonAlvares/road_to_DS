#Reading and printing average age of a csv
import pandas as pd
df  = pd.read_csv("sample.csv")
print(df.head(2))
print("Average age:", df["Age"].mean())
