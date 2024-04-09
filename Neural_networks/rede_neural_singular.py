### Exemplo básico de um neurônio artificial ###
import math
import time


### Definições das variáveis
### 1- Forçamos um possível loop infinito com o input e o output
input = -1
output_desire = 1

input_weight = 1
### Taxa de aprendizado
learning_rate = 0.01

### 2- Porém, o bias/viés nos permite ainda ajustar mesmo tendo um input fadado a erro
bias = 1
bias_weight = 0.5

### 3- Definição de até quando deve aprender
error = math.inf
iteration = 0

### 4- função de ativação
def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0

### 5- Loop de Aprendizado
while error != 0:
    ### Temporizado para ver as iterações
    time.sleep(0.5)

    iteration += 1
    print("### Iteração: ", iteration)

    sum = (input * input_weight) + (bias * bias_weight)
    print("### Soma: ", sum)

    output = activation(sum)

    error = output_desire - output
    print('### Erro', error)

### 6- ajuste de pesos
    if error != 0:
        input_weight = input_weight + (learning_rate * input * error)
        bias_weight = bias_weight + (learning_rate * bias * error)

print('### Aprendeu!', '### Entrada:', input, '### Saída:', output, '### Saída esperada:', output_desire)

### Basicamente, esse código demonstra como um neurônio artificial pode ser treinado para produzir uma saída desejada com base em uma entrada e ajustes de peso.