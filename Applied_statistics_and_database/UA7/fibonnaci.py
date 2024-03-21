# Importando o módulo concurrent.futures para trabalhar com concorrência em Python
import concurrent.futures as cf

# Definindo uma função chamada fib para calcular o número de Fibonacci
def fib(n):
    if n <= 2:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        raise Exception('fib(n) is undefined for n < 0')  # Lança uma exceção se n for negativo
    else:
        return fib(n-1) + fib(n-2)

# Verificando se o script está sendo executado como o programa principal
if __name__ == '__main__':
    import argparse  # Importando o módulo argparse para analisar argumentos da linha de comando
    from unittest import result  # Importando algo que parece ser desnecessário aqui

    # Criando um objeto ArgumentParser para lidar com argumentos da linha de comando
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, default=1, help='Number to calculate')
    parser.add_argument('numbers', nargs='?', type=int, default=34, help='Numbers to calculate')
    args = parser.parse_args()

    # Verificando se o número de threads especificado é maior ou igual a 1
    assert args.n >= 1, 'The number of threads has to be > 1'

    # Usando um bloco 'with' para criar um ProcessPoolExecutor com um número máximo de workers igual a args.n
    with cf.ProcessPoolExecutor(max_workers=args.n) as executor:
        # Usando o método 'map' do executor para calcular a função fib para 'args.n' vezes
        # e retornar um iterável de resultados (um gerador de resultados)
        results = executor.map(fib, [args.n] * args.n)

        # Iterando sobre os resultados e imprimindo cada um
        for result in results:
            print(result)
