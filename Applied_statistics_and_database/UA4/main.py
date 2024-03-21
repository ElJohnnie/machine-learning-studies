import pandas as pd

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv('desafio.csv')

# a) Apresentar as informações sobre as notas dos alunos em cada questão
questoes_cols = df.columns[1:-1]  # Assume que as colunas de questões começam a partir da segunda coluna
print("Notas dos alunos em cada questão:")
print(df[questoes_cols])

# b) Acrescentar uma coluna com a nota de cada aluno (soma das notas das questões)
df['Nota Total'] = df[questoes_cols].sum(axis=1)

# c) Apresentar o desvio padrão e a variância das notas de cada aluno
desvio_padrao = df['Nota Total'].std()
variancia = df['Nota Total'].var()
print("\nDesvio Padrão das Notas Totais:", desvio_padrao)
print("Variância das Notas Totais:", variancia)