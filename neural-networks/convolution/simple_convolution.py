import numpy as np

# Função de convolução
def convolution(image, kernel):
    # Dimensões da imagem e do kernel
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape
    # Dimensões do resultado da convolução
    result_height = image_height - kernel_height + 1
    result_width = image_width - kernel_width + 1
    # Inicializa a matriz de resultado
    result = np.zeros((result_height, result_width))
    # Loop pelos pixels da imagem
    for i in range(result_height):
        for j in range(result_width):
            # Calcula o produto da imagem e do kernel para a região atual
            result[i, j] = np.sum(image[i:i+kernel_height, j:j+kernel_width] * kernel)
    return result

# Função de max pooling
def max_pooling(image, size=2):
    # Dimensões da imagem
    image_height, image_width = image.shape
    # Dimensões do resultado do max pooling
    result_height = image_height // size
    result_width = image_width // size
    # Inicializa a matriz de resultado
    result = np.zeros((result_height, result_width))
    # Loop pelos grupos de pixels na imagem
    for i in range(result_height):
        for j in range(result_width):
            # Seleciona o máximo de cada grupo
            result[i, j] = np.max(image[i*size:(i+1)*size, j*size:(j+1)*size])
    return result

# Função de ativação ReLU
def relu(x):
    return np.maximum(0, x)

# Definição da rede neural convolucional
def cnn(image):
    # Primeira camada convolucional
    kernel1 = np.array([[1, 0, -1],
                        [1, 0, -1],
                        [1, 0, -1]])
    conv1 = convolution(image, kernel1)
    conv1_relu = relu(conv1)
    # Primeira camada de max pooling
    pool1 = max_pooling(conv1_relu)
    return pool1

# Teste da rede neural convolucional com uma imagem de exemplo
image = np.array([[1, 1, 1, 0],
                  [0, 1, 1, 1],
                  [0, 0, 1, 1],
                  [0, 0, 1, 0]])
result = cnn(image)
print("Resultado da convolução e max pooling:")
print(result)
