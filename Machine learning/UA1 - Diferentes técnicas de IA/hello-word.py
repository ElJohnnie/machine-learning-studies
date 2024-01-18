import random
import string

# Parâmetros do algoritmo genético
target = "Hello, World!"  # A string alvo que queremos gerar
population_size = 100  # Tamanho da população
mutation_rate = 0.01  # Taxa de mutação

# Função de fitness
def fitness(gene):
    return sum(1 for a, b in zip(gene, target) if a == b)

# Geração de uma população inicial aleatória
def generate_individual():
    return ''.join(random.choice(string.printable) for _ in range(len(target)))

population = [generate_individual() for _ in range(population_size)]

# Algoritmo genético
generation = 1
while True:
    print(f"Generation {generation}: {population[0]} (Fitness: {fitness(population[0])})")
    
    if any(individual == target for individual in population):
        print("Alvo atingido!")
        break
    
    new_population = []
    for _ in range(population_size):
        parent1, parent2 = random.choices(population, k=2)
        pivot = random.randint(1, len(target) - 1)
        child = parent1[:pivot] + parent2[pivot:]
        
        # Aplicar mutação
        if random.random() < mutation_rate:
            index = random.randint(0, len(target) - 1)
            child = child[:index] + random.choice(string.printable) + child[index + 1:]
        
        new_population.append(child)
    
    population = new_population
    generation += 1
