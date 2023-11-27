from collections import deque

def bfs(grafo, inicio):
    """
    Implementação do algoritmo de busca em largura (BFS).

    Parâmetros:
    - grafo: Grafo representado por um dicionário de adjacência.
    - inicio: Vértice de início da busca.

    Retorna:
    - Lista de vértices visitados na ordem em que foram encontrados.
    """
    visitados = set()
    fila = deque([inicio])
    resultado = []

    while fila:
        vertice = fila.popleft()
        if vertice not in visitados:
            visitados.add(vertice)
            resultado.append(vertice)
            fila.extend(vizinho for vizinho in grafo[vertice] if vizinho not in visitados)

    return resultado

# Exemplo de uso:
grafo_exemplo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

resultado_bfs = bfs(grafo_exemplo, 'A')
print("BFS:", resultado_bfs)
