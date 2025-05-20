import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = r"C:\Users\basum\OneDrive\Documents\Downloads\Downloads\youtube\Global YouTube Statistics.csv"
df = pd.read_csv(file_path, encoding="latin1")


print(df.info())
print("\nMissing Values:\n", df.isnull().sum())


print("\nSummary Statistics:\n", df.describe())


top_youtubers = df.sort_values(by="subscribers", ascending=False).head(10)
print("\nTop YouTubers by Subscribers:\n", top_youtubers[["Youtuber", "subscribers"]])

popular_category = df.groupby("category")["subscribers"].sum().sort_values(ascending=False)
print("\nMost Popular Categories:\n", popular_category)


plt.figure(figsize=(12, 6))
df["category"].value_counts().plot(kind="bar", title="YouTube Categories Distribution")
plt.xlabel("Category")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(10, 6))
plt.scatter(df["subscribers"], df["video views"], alpha=0.5)
plt.xlabel("Subscribers")
plt.ylabel("Video Views")
plt.title("Subscribers vs Video Views")
plt.show()


plt.figure(figsize=(12, 6))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()
