from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.datasets import load_iris

# Carregando o conjunto de dados Iris para este exemplo
iris = load_iris()
X, y = iris.data, iris.target

# Criando um modelo de Support Vector Classifier (SVC)
modelo_svc = SVC(kernel='linear')

# Usando cross_val_score para realizar validação cruzada e obter pontuações de desempenho
pontuacoes = cross_val_score(modelo_svc, X, y, cv=5)  # cv=5 indica 5 partições (k=5) para a validação cruzada

# Exibindo as pontuações obtidas em cada dobra
print("Pontuações de validação cruzada:", pontuacoes)

# Exibindo a média das pontuações
print("Média das pontuações:", pontuacoes.mean())
