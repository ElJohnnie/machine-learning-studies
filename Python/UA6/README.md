### Definição das funções:

- obter_notas_turma(num_alunos): Essa função recebe como argumento o número de alunos em uma turma (num_alunos). Ela solicita as notas para cada aluno de uma turma, armazenando-as em uma lista e retornando essa lista com as notas.

- calcular_media_aluno(notas_aluno): Essa função recebe como argumento a lista de notas de um aluno (notas_aluno). Ela calcula a média das notas desse aluno somando todas as notas e dividindo pela quantidade de notas. Em seguida, retorna a média calculada.

- calcular_medias_turma(notas_turma): Essa função recebe como argumento uma lista contendo as notas de todos os alunos de uma turma (notas_turma). Para cada lista de notas de aluno, ela chama a função calcular_media_aluno para calcular a média do aluno e armazenar essa média em uma lista medias_turma. Ao final, retorna a lista com as médias de todos os alunos da turma.

- exibir_medias_turmas(medias_turmas): Essa função recebe como argumento a lista de médias de todas as turmas (medias_turmas). Ela exibe as médias finais de cada turma, apresentando o número da turma e a média final correspondente.

### Função main():

- Essa é a função principal do programa, onde todo o código é executado. Primeiro, são definidos os números de turmas (num_turmas) e de alunos por turma (num_alunos).

- Em seguida, o programa entra em um loop que percorre cada turma (for i in range(num_turmas)). Para cada turma, ele imprime o número da turma e chama a função obter_notas_turma(num_alunos) para obter as notas dos alunos.

- As notas de cada turma são armazenadas em uma lista notas_todas_turmas. Após obter todas as notas das turmas, o programa chama a função calcular_medias_turma(notas_todas_turmas) para calcular as médias de todos os alunos de cada turma.

- Por fim, a função exibir_medias_turmas(medias_turmas) é chamada para mostrar na tela as médias finais de cada turma.

- Bloco if __name__ == "__main__":

- Esse bloco verifica se o código está sendo executado como um programa principal. Se estiver, chama a função main() para iniciar a execução do programa.

- O programa usa listas para armazenar as notas dos alunos e as médias das turmas. Ele também faz uso de loops (for) para percorrer as turmas e os alunos, permitindo que o usuário digite as notas para cada aluno e cada atividade do semestre.

- Ao final da execução, o programa exibirá as médias finais de cada turma.