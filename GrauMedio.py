import networkx as nx

def grau_medio(grafo):
    """
    Calcula o grau médio de um grafo.

    Parâmetros:
    - grafo: Grafo representado por um objeto NetworkX.

    Retorna:
    - Grau médio do grafo.
    """
    graus = dict(grafo.degree())
    num_vertices = len(grafo.nodes())

    if num_vertices == 0:
        return 0  # Grafo vazio

    soma_graus = sum(graus.values())
    grau_medio = soma_graus / num_vertices

    return grau_medio

# Exemplo de uso:
grafo = nx.Graph([(1, 2), (2, 3), (3, 4), (4, 1)])

grau_medio = grau_medio(grafo)
print("Grau médio do grafo:", grau_medio)
