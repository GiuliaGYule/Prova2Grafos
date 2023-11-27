def bellman_ford(grafo, origem):
    """
    Implementação do algoritmo de Bellman-Ford para encontrar caminhos mais curtos em um grafo ponderado.

    Parâmetros:
    - grafo: Grafo representado por uma lista de arestas ponderadas.
    - origem: Vértice de origem para calcular os caminhos mais curtos.

    Retorna:
    - Dicionário contendo os custos mínimos para chegar a cada vértice a partir da origem.
    - None se houver um ciclo de peso negativo no grafo.
    """
    vertices = set(v for u, v, _ in grafo) | set(u for u, v, _ in grafo)
    distancias = {vertice: float('inf') for vertice in vertices}
    distancias[origem] = 0

    for _ in range(len(vertices) - 1):
        for u, v, peso in grafo:
            if distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso

    for u, v, peso in grafo:
        if distancias[u] + peso < distancias[v]:
            return None  # Ciclo de peso negativo detectado

    return distancias

# Exemplo de uso:
grafo_ponderado = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 1)
]

origem = 'A'
resultado_bellman_ford = bellman_ford(grafo_ponderado, origem)

if resultado_bellman_ford is None:
    print("O grafo contém um ciclo de peso negativo.")
else:
    print(f"Caminhos mais curtos a partir de {origem}: {resultado_bellman_ford}")
