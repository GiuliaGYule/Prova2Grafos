def dfs(grafo, inicio, visitados=None):
    """
    Implementação do algoritmo de busca em profundidade (DFS).

    Parâmetros:
    - grafo: Grafo representado por um dicionário de adjacência.
    - inicio: Vértice de início da busca.
    - visitados: Conjunto para rastrear vértices visitados (opcional).

    Retorna:
    - Lista de vértices visitados na ordem em que foram encontrados.
    """
    if visitados is None:
        visitados = set()

    resultado = []

    def dfs_recursiva(vertice):
        visitados.add(vertice)
        resultado.append(vertice)
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                dfs_recursiva(vizinho)

    dfs_recursiva(inicio)
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

resultado_dfs = dfs(grafo_exemplo, 'A')
print("DFS:", resultado_dfs)
