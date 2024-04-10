import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_sizes, output_size):
        self.input_size = input_size
        self.hidden_sizes = hidden_sizes
        self.output_size = output_size
        
        # Inicialização dos pesos
        self.weights = [np.random.randn(input_size, hidden_sizes[0])]
        self.weights += [np.random.randn(hidden_sizes[i], hidden_sizes[i+1]) for i in range(len(hidden_sizes) - 1)]
        self.weights += [np.random.randn(hidden_sizes[-1], output_size)]
        
        # Inicialização dos biases
        self.biases = [np.zeros((1, hidden_size)) for hidden_size in hidden_sizes]
        self.biases += [np.zeros((1, output_size))]
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def forward(self, X):
        # Propagação para a frente
        self.activations = [X]
        for i in range(len(self.weights)):
            self.activations.append(self.sigmoid(np.dot(self.activations[i], self.weights[i]) + self.biases[i]))
        return self.activations[-1]
    
    def backward(self, X, y, output, learning_rate):
        # Retropropagação
        error = y - output
        deltas = [error * self.sigmoid_derivative(output)]
        for i in range(len(self.weights) - 1, 0, -1):
            error_hidden = deltas[-1].dot(self.weights[i].T)
            deltas.append(error_hidden * self.sigmoid_derivative(self.activations[i]))
        deltas.reverse()
        
        # Atualização dos pesos e biases
        for i in range(len(self.weights)):
            self.weights[i] += self.activations[i].T.dot(deltas[i]) * learning_rate
            self.biases[i] += np.sum(deltas[i], axis=0) * learning_rate
        
    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output, learning_rate)
            if epoch % 100 == 0:
                loss = np.mean(np.square(y - output))
                print(f'Epoch {epoch}: Loss = {loss}')

# Exemplo de uso
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([[0], [1], [1], [0]])

input_size = 2
hidden_sizes = [4, 4, 4, 4,]
output_size = 1

# Criando e treinando a rede neural
model = NeuralNetwork(input_size, hidden_sizes, output_size)
model.train(X_train, y_train, epochs=1000, learning_rate=0.1)

# Fazendo previsões
predictions = model.forward(X_train)
print('Predictions:')
for i, prediction in enumerate(predictions):
    print(f'Input: {X_train[i]}, Predicted Output: {prediction[0]}')
