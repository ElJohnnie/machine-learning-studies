import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Carregando a base de dados
boston_data = load_boston()
boston_df = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)

# Adicionando a coluna alvo (target) ao DataFrame
boston_df['MEDV'] = boston_data.target

# Selecionando a variável CRIM como preditora
X = boston_df.drop(columns=['CRIM'])

# Calculando o VIF para todas as variáveis independentes
vif = pd.DataFrame()
vif["Variável"] = X.columns
vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

# Encontrando o VIF da variável CRIM
vif_crim = vif[vif['Variável'] == 'CRIM']['VIF'].values[0]

# Verificando se a variável CRIM deve ser removida ou não
if vif_crim > 10:
    resposta = "Sim, merece ser removida."
else:
    resposta = "Não merece ser removida."

print(f"VIF da variável CRIM: {vif_crim:.2f}")
print(f"A variável CRIM merece ser removida? {resposta}")