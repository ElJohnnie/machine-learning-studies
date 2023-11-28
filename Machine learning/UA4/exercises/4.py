from sklearn.datasets import load_wine
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Carregando o conjunto de dados Wine para este exemplo
X, y = load_wine(return_X_y=True)

# Dividindo os dados em conjunto de treinamento e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando um modelo de Gaussian Naive Bayes
modelo = GaussianNB()

# Treinando o modelo usando partial_fit
modelo.partial_fit(X_treino, y_treino, classes=list(set(y)))

# Prevendo os rótulos do conjunto de teste
y_prevs = modelo.predict(X_teste)

# Calculando a acurácia
acuracia = accuracy_score(y_teste, y_prevs)

# Exibindo a acurácia
print("Acurácia:", acuracia)
