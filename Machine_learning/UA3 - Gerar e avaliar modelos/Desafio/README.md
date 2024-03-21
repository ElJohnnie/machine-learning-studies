O desenvolvimento de um sistema de aprendizado de máquina pode envolver inúmeros testes e configurações que não serão aproveitados na versão final de aplicação do algoritmo. Considerando nisso, imagine que você faz parte de uma equipe que deve desenvolver um algoritmo para buscar os parâmetros mais adequados para a classificação de espécies de uma flor em uma pesquisa de campo.

Assim, você decide escrever um novo algoritmo que contenha apenas os procedimentos necessários para efetuar os processos de transformação e aprendizado conforme os parâmetros encontrados. Para tanto, você opta por utilizar o método Pipeline, que, além de facilitar o entendimento de seus colegas de equipe, em eventual necessidade de ampliação do código, será muito mais legível, inclusive para você.

Como ponto de partida, você pode usar o algoritmo disponível a seguir para, utilizando o método Pipeline, tornar o código mais fácil de compreender.

from sklearn.datasets import load iris

from sklearn.pipeline import Pipeline

from sklearn.cluster import KMeans

from sklearn.metrics.cluster import silhouette score, davies bouldin score, calinski harabasz score
from sklearn.metrics import accuracy score

from sklearn.decomposition import PCA

from sklearn.preprocessing import StandardScaler

from sklearn.modeL selection import train test split

from sklearn import svm

import pandas as pa

X, y, y names, DESCR, , - = load iris().values()

pipe = Pipeline(steps=[
(PCA', PCA(n .components=2, random state = O)),
(Scaler', StandardScaler()),
(Kmeans', KMeans(n. clusters=3, random. state=0))

DD

clusters = pipe.fit predict(X)

y clusters = pa.DataFrame(clusters)[0].map((0: O, 2: 1, 1: 2)). values

— — — y teste real = train. test. split(X, y, random. state=50)
Xtreino, X teste, y treino, y teste clusters = train test split(X, y clusters, random. state=50)

model = svm.SVC(C = 100, gamma = le-2, kernel = 'rbf, max iter=1000000, random state=0)
model.fit(X. treino, y treino)

y—svm. prevs = model.predict(X. teste)

display(
accuracy. score(y. teste. clusters, y svm. prevs),
accuracy. score(y. teste. real, y svm. prevs),
accuracy. score(y. teste. real, y teste. clusters)

As etapas de teste, análise e validação de parâmetros devem ser eliminadas. Dessa forma, lembre-se de que o código deverá conter apenas os parâmetros finais de cada método para carregar, transformar, agrupar, separar e mostrar os três índices de precisão utilizados no código original.