from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Exemplo de dados de treinamento
corpus = [
    ('Este é um bom filme', 'positivo'),
    ('O ator principal é excelente', 'positivo'),
    ('Que filme terrível', 'negativo'),
    ('Eu não gostei da atuação', 'negativo'),
]

# Separando os dados em features (X) e rótulos (y)
X, y = zip(*corpus)

# Convertendo o texto para representação vetorial usando CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Dividindo os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando e treinando o modelo Naive Bayes
model = MultinomialNB()
model.fit(X_train, y_train)

# Fazendo previsões no conjunto de teste
y_pred = model.predict(X_test)

# Avaliando a precisão do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo: {accuracy:.2f}')

# Exibindo relatório de classificação
print('\nRelatório de Classificação:')
print(classification_report(y_test, y_pred))