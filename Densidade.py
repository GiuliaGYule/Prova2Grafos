import networkx as nx

def densidade_grafo(grafo):
    """
    Calcula a densidade de um grafo não direcionado.

    Parâmetros:
    - grafo: Grafo representado por um objeto NetworkX.

    Retorna:
    - Densidade do grafo.
    """
    num_vertices = len(grafo.nodes())
    num_arestas = len(grafo.edges())

    if num_vertices < 2:
        return 0  # Grafo vazio ou com apenas um vértice

    return 2 * num_arestas / (num_vertices * (num_vertices - 1))

# Exemplo de uso:
grafo = nx.Graph([(1, 2), (2, 3), (3, 1), (2, 4)])

densidade = densidade_grafo(grafo)
print("Densidade do grafo:", densidade)
