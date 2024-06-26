#!/usr/bin/python
# -*- coding: utf-8 -*-

# Implementação Perceptron
import sys
import random


class Perceptron:
    # Primeira função de uma classe (método construtor de objetos)
    # self é um parâmetro obrigatório que receberá a instância criada
    def __init__(self, amostras, saidas, taxa_aprendizado=0.1, épocas=1000, limiar=1):
        self.amostras = amostras
        self.saidas = saidas
        self.taxa_aprendizado = taxa_aprendizado
        self.epocas = épocas
        self.limiar = limiar
        self.n_amostras = len(amostras)  # número de linhas
        self.n_atributos = len(amostras[0])  # número de atributos
        self.pesos = []

    # Atribuição de treinamento para amostras e construção da matriz
    def treinar(self):
        # Inserir o valor do limiar na posição "0" para cada amostra da lista “amostra”
        for amostra in self.amostras:
            amostra.insert(0, self.limiar)

        # Gerar valores randômicos entre 0 e 1 (pesos) conforme o número de atributos
        for i in range(self.n_atributos):
            self.pesos.append(random.random())

        # Inserir o valor do limiar na posição "0" do vetor de pesos
        self.pesos.insert(0, self.limiar)

        # Inicializar contador de épocas
        n_epocas = 0

        while True:
            # Inicializar variável erro (quando terminar o loop e erro continuar False, é porque não tem mais diferença entre valor calculado e desejado)
            erro = False

            # Para cada amostra...
            for i in range(self.n_amostras):
                # Inicializar potencial de ativação
                u = 0

                # Para cada atributo...
                for j in range(self.n_atributos + 1):
                    # Multiplicar amostra e seu peso e também somar com o potencial
                    u += self.pesos[j] * self.amostras[i][j]

                # Obter a saída da rede considerando a função sinal
                y = self.sinal(u)

                # Verificar se a saída da rede é diferente da saída desejada
                if y != self.saidas[i]:
                    # Calcular o erro
                    erro_aux = self.saidas[i] - y

                    # Fazer o ajuste dos pesos para cada elemento da amostra
                    for j in range(self.n_atributos + 1):
                        self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro_aux

                    # Atualizar variável erro, já que erro é diferente de zero
                    erro = True

            # Atualizar contador de épocas
            n_epocas += 1

            # Critérios de parada do loop: erro inexistente ou o número de épocas
            if not erro or n_epocas > self.epocas:
                break

    ## Testes para "novas" amostras
    def teste(self, amostra):
        # Inserir o valor do limiar na posição "0" para cada amostra da lista “amostra”
        amostra.insert(0, self.limiar)

        # Inicializar potencial de ativação
        u = 0

        # Para cada atributo...
        for i in range(self.n_atributos + 1):
            # Multiplicar amostra e seu peso e também somar com o potencial que já tinha
            u += self.pesos[i] * amostra[i]

        # Obter a saída da rede considerando a função sinal
        y = self.sinal(u)
        print('Classe: %d' % y)

    ## Função sinal
    def sinal(self, u):
        if u >= 0:
            return 1
        return -1


# Amostras (entrada e saída) para treinamento
amostras = [[0.72, 0.82], [0.91, -0.69], [0.46, 0.80], [0.03, 0.93], [0.12, 0.25], [0.96, 0.47],
            [0.8, -0.75], [0.46, 0.98], [0.66, 0.24], [0.72, -0.15], [0.35, 0.01], [-0.16, 0.84],
            [-0.04, 0.68], [-0.11, 0.1], [0.31, -0.96], [0.0, -0.26], [-0.43, -0.65], [0.57, -0.97],
            [-0.47, -0.03], [-0.72, -0.64], [-0.57, 0.15], [-0.25, -0.43], [0.47, -0.88], [-0.12, -0.9],
            [-0.58, 0.62], [-0.48, 0.05], [-0.79, -0.92], [-0.42, -0.09], [-0.76, 0.65], [-0.77, -0.76]]

saidas = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
          1, 1, 1, 1, 1, 1]

# Chamar classe e fazer treinamento das amostras
rede = Perceptron(amostras, saidas)
rede.treinar()

# Entrando com amostra para teste
rede.teste([-0.20, -0.82])

# Fim do perceptron
