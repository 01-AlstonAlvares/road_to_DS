#Mini Task
    #Load the provided CSV.
    #Plot one line chart and one histogram.
    #Try styling them with titles, labels, and different colors.
    #Save one of your plots to a PNG file.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 29],
    "Salary": [50000, 60000, 75000, 80000, 62000]
}
df = pd.DataFrame(data)

#Line plot
plt.figure(figsize=(6,4))
plt.plot(df["Age"], df["Salary"], marker = 'o')
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid(True)
plt.tight_layout()
plt.savefig("age_salary_line_plot.png")
plt.close()

#Bar chart
plt.figure(figsize=(6, 4))
df["Age"].value_counts().sort_index().plot(kind ='bar')
plt.title("Count of People by Age")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("age_bar_chart.png")
plt.close()

#Histogram
plt.figure(figsize=(6, 4))
plt.hist(df["Salary"], bins = 5, color='skyblue', edgecolor = 'black')
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("salary_histogram.png")
plt.close()

#Scatterplot
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x="Age", y="Salary", hue="Name")
plt.title("Seaborn: Age vs Salary")
plt.tight_layout()
plt.savefig("age_salary_scatterplot.png")
plt.close()