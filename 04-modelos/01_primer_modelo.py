import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Cargamos datos
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# 2. Limpieza mínima (usamos lo que ya aprendiste)
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})  # Convertimos texto a número

# 3. Elegimos qué columnas usa el modelo para aprender
X = df[['Pclass', 'Sex', 'Age']]  # Características
y = df['Survived']                # Lo que queremos predecir

# 4. Separamos en datos para entrenar y datos para probar
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Creamos y entrenamos el modelo - acá es automático
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# 6. Probamos qué tan bien predice
predicciones = modelo.predict(X_test)
print(f"Precisión: {accuracy_score(y_test, predicciones) * 100:.1f}%")

# 7. Probamos con una persona inventada
# Ejemplo: Mujer, clase 1, 30 años
persona = pd.DataFrame([[1, 1, 30]], columns=['Pclass', 'Sex', 'Age'])
print(f"Probabilidad de sobrevivir para mujer clase 1 de 30 años: {modelo.predict(persona)}")
# 1 = sobrevive, 0 = no sobrevive
