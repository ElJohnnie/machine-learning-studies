def calculate_area_of_triangle(vertices):
    matrix = [list(vertex) + [1] for vertex in vertices]
    determinant = (
        matrix[0][0] * matrix[1][1] * matrix[2][2] +
        matrix[0][1] * matrix[1][2] * matrix[2][0] +
        matrix[0][2] * matrix[1][0] * matrix[2][1] -
        matrix[2][0] * matrix[1][1] * matrix[0][2] -
        matrix[2][1] * matrix[1][2] * matrix[0][0] -
        matrix[2][2] * matrix[1][0] * matrix[0][1]
    )
    area = abs(determinant) / 2
    return area

# Coordenadas dos vértices do triângulo
vertices = [[0, 0], [6, 0], [8, 2]]

# Calcular a área do triângulo usando a função
area_tri = calculate_area_of_triangle(vertices)

# Comparar com o valor esperado (15)
area_esperada = 15

print("Área do triângulo:", area_tri)
print("Área esperada:", area_esperada)

# Verificar se o resultado está próximo ao valor esperado (levando em conta possíveis erros de precisão float)
if abs(area_tri - area_esperada) < 1e-10:
    print("O resultado está correto!")
else:
    print("O resultado não está correto.")
