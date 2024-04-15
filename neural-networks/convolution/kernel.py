import numpy as np
import matplotlib.pyplot as plt

# Função para aplicar a convolução em uma imagem
def apply_convolution(image, kernel):
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape
    output_height = image_height - kernel_height + 1
    output_width = image_width - kernel_width + 1
    output = np.zeros((output_height, output_width))
    for i in range(output_height):
        for j in range(output_width):
            output[i, j] = np.sum(image[i:i+kernel_height, j:j+kernel_width] * kernel)
    return output

# Imagem de exemplo
image = np.array([[1, 1, 1, 0, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 1, 1, 1],
                  [0, 0, 1, 1, 0],
                  [0, 1, 1, 0, 0]], dtype=np.float32)

# Kernel de detecção de bordas
kernel = np.array([[1, 0, -1],
                   [1, 0, -1],
                   [1, 0, -1]])

# Aplicando a convolução
result = apply_convolution(image, kernel)

# Imprimindo a imagem original e o resultado da convolução
print("Imagem original:")
print(image)
print("\nResultado da convolução com o kernel de detecção de bordas:")
print(result)

# Visualizando a imagem original e o resultado da convolução
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagem Original')
plt.subplot(1, 2, 2)
plt.imshow(result, cmap='gray')
plt.title('Resultado da Convolução')
plt.show()