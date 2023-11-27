def floyd_warshall(grafo):
    """
    Implementação do algoritmo de Floyd-Warshall para encontrar todos os caminhos mais curtos em um grafo ponderado.

    Parâmetros:
    - grafo: Grafo representado por uma matriz de adjacência (infinito para ausência de aresta).

    Retorna:
    - Matriz contendo os comprimentos dos caminhos mais curtos entre todos os pares de vértices.
    """
    num_vertices = len(grafo)
    
    # Inicializa a matriz de distâncias com os comprimentos das arestas existentes e infinito para ausência de arestas.
    distancias = [[float('inf') if i != j else 0 for j in range(num_vertices)] for i in range(num_vertices)]

    # Atualiza a matriz de distâncias com base nos caminhos mais curtos.
    for i in range(num_vertices):
        for j in range(num_vertices):
            if grafo[i][j] != float('inf'):
                distancias[i][j] = grafo[i][j]

    # Algoritmo de Floyd-Warshall
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])

    return distancias

# Exemplo de uso:
infinito = float('inf')
grafo_ponderado = [
    [0, 1, 4, infinito],
    [infinito, 0, 2, 5],
    [infinito, infinito, 0, 1],
    [infinito, infinito, infinito, 0]
]

resultado_floyd_warshall = floyd_warshall(grafo_ponderado)

print("Matriz de distâncias:")
for linha in resultado_floyd_warshall:
    print(linha)
