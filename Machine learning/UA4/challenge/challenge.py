import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB

# Carregando o conjunto de dados
X, y = load_breast_cancer(return_X_y=True)

# Definindo o intervalo de valores para var_smoothing
valores_var_smoothing = np.logspace(-11, -8, 10)

# Dicionário para armazenar resultados
resultados = {}

# Loop para testar cada valor de var_smoothing
for var_smoothing in valores_var_smoothing:
    modelo = GaussianNB(var_smoothing=var_smoothing)
    pontuacoes = cross_val_score(modelo, X, y, cv=5, scoring='accuracy')
    resultados[var_smoothing] = pontuacoes.mean()

# Encontrando o melhor valor de var_smoothing
melhor_var_smoothing = max(resultados, key=resultados.get)
melhor_acuracia = resultados[melhor_var_smoothing]

print("Melhor valor de var_smoothing:", melhor_var_smoothing)
print("Acurácia correspondente:", melhor_acuracia)
