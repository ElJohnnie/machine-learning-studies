from sklearn.datasets import load_iris
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

import pandas as pd

# Carregando o conjunto de dados
X, y = load_iris(return_X_y=True)

# Criando o pipeline
pipe = Pipeline(steps=[
    ('PCA', PCA(n_components=2, random_state=0)),
    ('Scaler', StandardScaler()),
    ('Kmeans', KMeans(n_clusters=3, random_state=0))
])

# Aplicando o pipeline e transformando os dados
clusters = pipe.fit_predict(X)

# Mapeando os clusters para os rótulos desejados
y_clusters = pd.DataFrame(clusters)[0].map({0: 0, 2: 1, 1: 2}).values

# Separando os dados em conjuntos de treino e teste
X_train, X_test, y_train_clusters, y_test_clusters = train_test_split(X, y_clusters, random_state=50)
_, _, y_train_real, y_test_real = train_test_split(X, y, random_state=50)

# Treinando o modelo SVM
model = svm.SVC(C=100, gamma=1e-2, kernel='rbf', max_iter=1000000, random_state=0)
model.fit(X_train, y_train_real)

# Prevendo os rótulos usando o modelo SVM
y_svm_preds = model.predict(X_test)

# Avaliando a precisão
accuracy_clusters = accuracy_score(y_test_clusters, y_svm_preds)
accuracy_real = accuracy_score(y_test_real, y_svm_preds)

# Exibindo os resultados
print("Acurácia (usando clusters):", accuracy_clusters)
print("Acurácia (usando rótulos reais):", accuracy_real)
