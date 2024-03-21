import numpy as np

# Dados
x = np.array([0, 1, 3, 5, 8])
y = np.array([2, 4, 6, 5, 9])

# Calcula a correlação de Pearson
correlation = np.corrcoef(x, y)[0, 1]

print("Correlação de Pearson:", correlation)