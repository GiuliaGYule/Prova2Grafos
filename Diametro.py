import networkx as nx

def diametro_grafo(grafo):
    """
    Calcula o diâmetro de um grafo.

    Parâmetros:
    - grafo: Grafo representado por um objeto NetworkX.

    Retorna:
    - Diâmetro do grafo.
    """
    if not nx.is_connected(grafo):
        return float('inf')  # Grafo não conectado

    diametro = nx.diameter(grafo)

    return diametro

# Exemplo de uso:
grafo = nx.Graph([(1, 2), (2, 3), (3, 4), (4, 1)])

diametro = diametro_grafo(grafo)
print("Diâmetro do grafo:", diametro)
