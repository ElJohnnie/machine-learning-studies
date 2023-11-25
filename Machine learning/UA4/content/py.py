# Exemplo 1 – Treinamento de uma GaussianNB com dados
# aleatórios
# Carrega as bibliotecas utilizadas para criar o conjunto
# de dados, o modelo e os gráficos
from sklearn.datasets import make_classification
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as pyp
import seaborn as sb
# Cria conjunto de dados de 100 instâncias e 2 atributos
# não redundantes
X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=1)
# Criando e treinando o modelo
model = GaussianNB()
model.fit(X, y)
# Prevendo os rótulos de cada instância com o modelo
# treinado
y_prevs = model.predict(X)
# Criando gráficos e legendas
fig, axes = pyp.subplots(1, 2, figsize=(12,4))
sb.scatterplot(X[:,0], X[:,1], hue=y, ax=axes[0])
sb.scatterplot(X[:,0], X[:,1], hue=y_prevs, ax=axes[1])
axes[0].set_title('Conjunto Original')
axes[0].set_xlabel('‘Atributo 1’')
axes[0].set_ylabel('‘Atributo 2’')
axes[1].set_title('‘Rótulos Previstos: GaussianNB’')
axes[1].set_xlabel('‘Atributo 1’')
axes[1].set_ylabel('‘Atributo 2’')