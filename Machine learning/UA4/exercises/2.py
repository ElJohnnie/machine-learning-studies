from sklearn.datasets import load_wine
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score

# Carregando o conjunto de dados Wine para este exemplo
X, y = load_wine(return_X_y=True)

# Criando um modelo de Gaussian Naive Bayes
modelo = GaussianNB()
modelo.fit(X, y)

# Usando cross_val_score para realizar validação cruzada e obter pontuações de desempenho
pontuacoes = cross_val_score(modelo, X, y, cv=5)  # cv=5 indica 5 partições (k=5) para a validação cruzada

# Exibindo as pontuações obtidas em cada dobra
print("Pontuações de validação cruzada:", pontuacoes)

# Exibindo a média das pontuações
print("Média das pontuações:", pontuacoes.mean())
