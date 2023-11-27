import heapq

def dijkstra(grafo, origem):
    """
    Implementação do algoritmo de Dijkstra para encontrar os caminhos mais curtos em um grafo ponderado.

    Parâmetros:
    - grafo: Grafo representado por um dicionário de adjacência ponderado.
    - origem: Vértice de origem para calcular os caminhos mais curtos.

    Retorna:
    - Dicionário contendo os custos mínimos para chegar a cada vértice a partir da origem.
    """
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[origem] = 0
    heap = [(0, origem)]

    while heap:
        (custo, vertice_atual) = heapq.heappop(heap)

        if custo > distancias[vertice_atual]:
            continue

        for vizinho, peso in grafo[vertice_atual].items():
            custo_total = custo + peso

            if custo_total < distancias[vizinho]:
                distancias[vizinho] = custo_total
                heapq.heappush(heap, (custo_total, vizinho))

    return distancias

# Exemplo de uso:
grafo_ponderado = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

origem = 'A'
resultado_dijkstra = dijkstra(grafo_ponderado, origem)
print(f"Caminhos mais curtos a partir de {origem}: {resultado_dijkstra}")
