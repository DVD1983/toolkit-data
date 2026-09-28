import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# Limpiamos un toque antes de graficar
df['Age'] = df['Age'].fillna(df['Age'].median())

# Gráfico 1: Histograma
plt.figure()
df['Age'].hist(bins=30)
plt.title('Distribución de edades - Titanic')
plt.xlabel('Edad')
plt.ylabel('Cantidad de pasajeros')
plt.show()
