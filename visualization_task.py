import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset load karo
df = pd.read_csv("titanic.csv")

# Chart 1: Gender ke hisaab se survival count
plt.figure(figsize=(6,4))
sns.countplot(x="Sex", hue="Survived", data=df)
plt.title("Gender ke hisaab se Survival Count")
plt.savefig("chart1_gender_survival.png")
plt.show()

# Chart 2: Class ke hisaab se survival rate
plt.figure(figsize=(6,4))
sns.barplot(x="Pclass", y="Survived", data=df)
plt.title("Class ke hisaab se Survival Rate")
plt.savefig("chart2_class_survival.png")
plt.show()

# Chart 3: Age distribution
plt.figure(figsize=(6,4))
sns.histplot(df["Age"].dropna(), bins=30, kde=True)
plt.title("Passengers ki Age Distribution")
plt.savefig("chart3_age_distribution.png")
plt.show()

# Chart 4: Fare vs Survival (box plot)
plt.figure(figsize=(6,4))
sns.boxplot(x="Survived", y="Fare", data=df)
plt.title("Fare vs Survival")
plt.savefig("chart4_fare_survival.png")
plt.show()

print("Saare charts ban gaye aur save ho gaye!")