import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# Esto responde una pregunta de negocio automática
print(df['Sex'].value_counts())
print(df['Pclass'].value_counts())
print(df['Survived'].value_counts())