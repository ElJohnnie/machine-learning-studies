def obter_notas_turma(num_alunos):
    notas_turma = []
    for i in range(num_alunos):
        notas_aluno = []
        print(f"\nDigite as notas do aluno {i + 1}:")
        for j in range(5):
            nota = float(input(f"Nota {j + 1}: "))
            notas_aluno.append(nota)
        notas_turma.append(notas_aluno)
    return notas_turma

def calcular_media_aluno(notas_aluno):
    return sum(notas_aluno) / len(notas_aluno)

def calcular_medias_turma(notas_turma):
    medias_turma = []
    for notas_aluno in notas_turma:
        media_aluno = calcular_media_aluno(notas_aluno)
        medias_turma.append(media_aluno)
    return medias_turma

def exibir_medias_turmas(medias_turmas):
    print("\nMédias finais das turmas:")
    for i, media_turma in enumerate(medias_turmas):
        print(f"Turma {i + 1}: {media_turma:.2f}")

def main():
    num_turmas = 9
    num_alunos = 24
    notas_todas_turmas = []
    for i in range(num_turmas):
        print(f"\nTurma {i + 1}")
        notas_turma = obter_notas_turma(num_alunos)
        notas_todas_turmas.append(notas_turma)
    medias_turmas = calcular_medias_turma(notas_todas_turmas)
    exibir_medias_turmas(medias_turmas)

if __name__ == "__main__":
    main()
