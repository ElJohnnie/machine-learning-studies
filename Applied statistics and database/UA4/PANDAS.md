- O pandas é uma biblioteca popular em Python para manipulação e análise de dados. Ela oferece uma ampla gama de funções e métodos para lidar com dados de forma eficiente. Aqui estão algumas das principais funções e métodos do pandas:

- Leitura e Escrita de Dados:

```read_csv, read_excel, read_sql```: Para ler dados de arquivos CSV, Excel ou bancos de dados SQL.
```to_csv, to_excel, to_sql```: Para salvar dados em formatos CSV, Excel ou em bancos de dados.

- Estruturas de Dados:

```DataFrame```: A estrutura fundamental do pandas, semelhante a uma tabela de banco de dados.
```Series```: Uma estrutura unidimensional que pode conter diferentes tipos de dados.

- Seleção e Filtragem:

Indexação por coluna: ```df['coluna']```.
Indexação por posição: ```df.iloc[linha, coluna]```.
Filtros condicionais: ```df[df['coluna'] > valor]```.

- Manipulação de Dados:

```drop```: Para remover linhas ou colunas de um DataFrame.
```groupby```: Para agrupar dados com base em uma ou mais colunas.
```merge```, concat: Para combinar DataFrames.

- Transformação de Dados:

```apply```: Aplica uma função a elementos de uma coluna ou linha.
```map```: Mapeia valores de uma coluna usando um dicionário ou função.
```replace```: Substitui valores em um DataFrame.

- Operações Estatísticas:

```mean, median, sum```: Calcula a média, mediana e soma dos valores.
```describe```: Gera estatísticas descritivas do DataFrame.

- Visualização de Dados:

```plot```: Cria visualizações, como gráficos de linha, barras e dispersão.

- Tratamento de Dados Ausentes:

```isna, fillna```: Identifica valores ausentes e preenche-os.
```dropna```: Remove linhas com valores ausentes.

- Ordenação e Classificação:

```sort_values, sort_index```: Ordena valores por coluna ou índice.

- Estatísticas Descritivas:

```corr```: Calcula a matriz de correlação entre colunas.
```cov```: Calcula a matriz de covariância entre colunas.

- Indexação e Rótulos:

```set_index, reset_index```: Define ou redefine o índice do DataFrame.
```loc```: Permite acesso aos dados usando rótulos.
```iloc```: Permite acesso aos dados usando índices inteiros.

- Agregação e Resumo:

```agg, applyma```p: Realiza agregações personalizadas em colunas ou elementos.
```pivot_table```: Cria tabelas dinâmicas para resumir e agregar dados.

- Manipulação de Strings:

```str.contains, str.replace```: Realiza operações de string em colunas.

- Amostragem de Dados:

```sample```: Amostra aleatoriamente linhas ou colunas do DataFrame.

- Operações de Tempo:

```to_datetime```: Converte colunas em formato de data e hora.
```resample```: Realiza reamostragem de séries temporais.

- Merging e Joins Avançados:

```merge```: Realiza junções sofisticadas entre DataFrames.
```join```: Realiza junções com base nos índices.

- Operações de Vetorização:

```appl```y: Pode ser usada para aplicar funções a linhas ou colunas.
--- Operações aritméticas e lógicas: São aplicadas de forma elementar a todas as entradas. --- 

- Manipulação de Categorias:

```astype```: Converte tipos de coluna, incluindo conversão para categorias.

- Manipulação de Multi-índices:

```MultiIndex```: Permite índices hierárquicos para dados multidimensionais.

- Leitura e Escrita de Dados de Alta Performance:

```read_hdf, to_hdf```: Leitura e escrita em formatos HDF5.
```read_parquet, to_parquet```: Leitura e escrita em formato parquet.

```info()```: Esse método fornece uma visão geral concisa das informações do DataFrame, incluindo o número de entradas não nulas por coluna, o tipo de dados de cada coluna e o uso de memória.

```head(n)```: Exibe as primeiras n linhas do DataFrame, permitindo uma rápida visualização dos dados iniciais.

```tail(n)```: Exibe as últimas n linhas do DataFrame, útil para visualizar os dados finais.

```shape```: Retorna uma tupla representando a forma (número de linhas e colunas) do DataFrame.

```columns```: Retorna uma lista das colunas presentes no DataFrame.

```index```: Retorna informações sobre o índice do DataFrame.

```dtypes```: Retorna os tipos de dados das colunas do DataFrame.

```describe()```: Gera estatísticas descritivas para as colunas numéricas do DataFrame, incluindo média, desvio padrão, quartis, etc.

```nunique()```: Retorna o número de valores únicos em cada coluna.

```value_counts()```: Conta a frequência de valores únicos em uma coluna, útil para colunas categóricas.

```isna(), isnull()```: Retorna uma máscara booleana indicando os valores ausentes em todo o DataFrame.

```count()```: Retorna o número de valores não nulos em cada coluna.

```unique()```: Retorna os valores únicos em uma coluna.

```idxmax(), idxmin()```: Retorna os índices dos valores máximos e mínimos em uma coluna.

```corr()```: Calcula a matriz de correlação entre as colunas numéricas do DataFrame.

```cov()```: Calcula a matriz de covariância entre as colunas numéricas.

```sum(), mean(), median(), std()```: Calcula a soma, média, mediana e desvio padrão das colunas numéricas.

Esses são apenas alguns exemplos dos muitos métodos disponíveis no pandas para obter informações detalhadas sobre seus dados. Eles são essenciais para explorar, entender e preparar seus dados para análises mais aprofundadas.