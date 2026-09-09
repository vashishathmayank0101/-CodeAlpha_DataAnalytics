import pandas as pd

# Dataset load karo
df = pd.read_csv("titanic.csv")

# Pehli 5 rows dekho
print("Dataset ki jhalak:")
print(df.head())

# Dataset ka basic structure
print("\nDataset Info:")
print(df.info())

# Numerical columns ka summary (mean, min, max, etc.)
print("\nStatistical Summary:")
print(df.describe())

# Missing values check karo
print("\nMissing Values:")
print(df.isnull().sum())

# ---- Neeche wala naya code ----

# Survival rate by gender
print("\nGender ke hisaab se Survival Rate:")
print(df.groupby("Sex")["Survived"].mean())

# Survival rate by class
print("\nClass ke hisaab se Survival Rate:")
print(df.groupby("Pclass")["Survived"].mean())

# Average age
print("\nAverage Age:", df["Age"].mean())

# Kitne log kis jagah se chade (Embarked)
print("\nEmbarked Count:")
print(df["Embarked"].value_counts())