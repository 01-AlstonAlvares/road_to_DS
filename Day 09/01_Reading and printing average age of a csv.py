#Use a CSV file that contains columns like Name, Age, and Salary.
#Try:
#1.Checking how many missing values are in each column.
#2.Filling or dropping missing values.
#3.Filtering rows where Age > 25.
#4.Saving the cleaned result.
import pandas as pd
df  = pd.read_csv("sample_day9.csv")
print(df.isnull().sum())
df =  df.dropna()
df["Age"]= df["Age"].fillna(df["Age"].mean())
print(df[df["Age"] > 25])
df.to_csv("cleaned_data.csv", index = False)