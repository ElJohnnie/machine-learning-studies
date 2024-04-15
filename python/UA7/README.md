### Explicação do código:

- A função calcular_media é definida para encapsular a lógica do cálculo da média e a leitura das notas do aluno.

- O nome do aluno é lido usando a função input.

- Em seguida, é criada uma lista vazia chamada notas para armazenar as notas inseridas pelo professor.

- Utiliza-se um laço de repetição while True para ler as notas indefinidamente até que o professor digite "fim".

- Dentro do loop, o programa lê a nota digitada pelo professor. Se o professor digitar "fim", o loop é interrompido usando break.

- Caso contrário, a nota é convertida para um número float e é verificado se está entre 0 e 10. Se for válido, a nota é adicionada à lista notas. Caso contrário, uma mensagem de erro é exibida.

- Após o loop, é calculada a média das notas usando a função sum para somar todas as notas e o operador de divisão / para obter a média.

- Se existirem notas na lista, o nome do aluno e a média são impressos na tela. Caso contrário, é informado que nenhuma nota foi inserida.

- A função calcular_media() é chamada para iniciar o processo de leitura das notas e cálculo da média.