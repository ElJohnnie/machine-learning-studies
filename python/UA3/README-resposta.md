De acordo com o enunciado do desafio, para que o círculo (representado pela classe Círculo – linha 1) contenha informações de posicionamento cartesiano, é importante que seja atribuído o código necessário de dois atributos (centrox e centroy – linhas 3 e 4). Para a representação do raio de um círculo, foi definido um atributo (raio – linha 5). A fim de inicializar o objeto com valores para os seus atributos, foi implementado um método inicializador em Python (linha 2 a 5).

Para cada operação sobre o círculo solicitado no enunciado, foi criado um método correspondente:
​​​​​​​• calcular a área do círculo – método area (linhas 6 e 7);
• calcular o comprimento da circunferência – método circunferencia (linhas 8 e 9);
• calcular o diâmetro do círculo – método diametro (linhas 10 e 11);
• mudar a posição do círculo – método mover (linha 12 a 14).

Por fim, foi criado um exemplo para instanciar um objeto círculo de centro (0,0) e raio 1, atribuindo-o à variável c1. Lembre-se que ao usar o nome de uma classe em Python no lado direito de um comando de atribuição, de uma vez só estão sendo chamados o seu construtor e o seu inicializador. A seguir, foram realizadas chamadas de cada método disponível sobre o objeto c1 e os resultados impressos no console. Por exemplo, para calcular a área do círculo c1, foi utilizado o código c1.area(). De forma análoga, podemos consultar o valor de um atributo do objeto círculo, como foi feito no código c1.centrox.

A seguir acompanhe o objeto criado.