#include <stdio.h>

// Função do kernel CUDA para somar elementos do array
__global__ void somaArray(int* d_array, int* d_result, int size) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;

    if (idx < size) {
        atomicAdd(d_result, d_array[idx]);
    }
}

int main() {
    int size = 1024; // Tamanho do array
    int h_array[size]; // Array de entrada no host
    int h_result = 0; // Resultado no host
    int* d_array; // Array de entrada no dispositivo (GPU)
    int* d_result; // Resultado no dispositivo (GPU)

    // Inicialize o array de entrada no host
    for (int i = 0; i < size; i++) {
        h_array[i] = i;
    }

    // Aloque memória na GPU
    cudaMalloc((void**)&d_array, size * sizeof(int));
    cudaMalloc((void**)&d_result, sizeof(int));

    // Copie o array de entrada para a GPU
    cudaMemcpy(d_array, h_array, size * sizeof(int), cudaMemcpyHostToDevice);

    // Inicialize o resultado na GPU
    cudaMemset(d_result, 0, sizeof(int));

    // Configura a grade de threads e blocos
    int blockSize = 256;
    int gridSize = (size + blockSize - 1) / blockSize;

    // Chame o kernel CUDA para realizar a soma
    somaArray<<<gridSize, blockSize>>>(d_array, d_result, size);

    // Copie o resultado de volta para o host
    cudaMemcpy(&h_result, d_result, sizeof(int), cudaMemcpyDeviceToHost);

    // Libere a memória alocada na GPU
    cudaFree(d_array);
    cudaFree(d_result);

    // Imprima o resultado
    printf("A soma dos elementos do array é: %d\n", h_result);

    return 0;
}
