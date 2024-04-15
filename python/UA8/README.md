### O problema

A linguagem Python tem uma sintaxe considerada como sendo de fácil aprendizado. Na maioria das vezes, pode-se resolver a maioria das tarefas em apenas uma linha de código, enquanto seriam necessárias mais linhas em outras linguagens. Desse modo, é bastante fácil para o programador reduzir e resolver possíveis erros. 

Você trabalha em uma equipe de desenvolvimento, e seu colega pediu ajuda para identificar por que o erro abaixo está aparecendo quando ele tenta executar o seu programa:

```
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: list indices must be integers or slices, not str]
```

Ao analisar o código, você identificou o seguinte trecho de código relacionado ao problema:

```
lista = [a, b, c]
print(lista['a'])
```

A solução está no arquivo py.py