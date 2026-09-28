import pandas as pd

df = pd.read_csv(
	"https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)

print(f"Nulos en Age antes: {df['Age'].isna().sum()}")
df["Age"] = df["Age"].fillna(df["Age"].median())
print(f"Nulos en Age después: {df['Age'].isna().sum()}")
