def calcular_media():
    nome_aluno = input("Digite o nome do aluno: ")
    notas = []
    
    # Laço de repetição para ler as notas digitadas pelo professor
    while True:
        nota_str = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
        
        # Verifica se o professor digitou 'fim' para encerrar a entrada de notas
        if nota_str.lower() == 'fim':
            break
        
        # Tenta converter a nota digitada para um número float
        try:
            nota = float(nota_str)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite uma nota válida.")
    
    # Calcula a média das notas
    if len(notas) > 0:
        media = sum(notas) / len(notas)
        print(f"Aluno: {nome_aluno}")
        print(f"Média: {media:.2f}")
    else:
        print("Nenhuma nota foi inserida.")

# Chamada da função principal
calcular_media()