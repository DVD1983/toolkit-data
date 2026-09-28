import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# Cuántos sobrevivieron por sexo
tabla = df.groupby('Sex')['Survived'].mean()

plt.figure()
tabla.plot(kind='bar')
plt.title('Tasa de supervivencia por sexo')
plt.ylabel('Porcentaje que sobrevivió')
plt.xticks(rotation=0)
plt.show()

print(tabla)