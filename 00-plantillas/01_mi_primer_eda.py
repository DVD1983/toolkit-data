import pandas as pd

# Cargamos el dataset de prueba
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

print("Primeras 5 filas:")
print(df.head())

print("\nInfo:")
print(df.info())