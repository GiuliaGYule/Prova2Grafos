import networkx as nx

def eh_subgrafo_valorado(grafo_maior, grafo_menor):
    """
    Verifica se um grafo valorado é subgrafo de outro.

    Parâmetros:
    - grafo_maior: Grafo valorado maior.
    - grafo_menor: Grafo valorado menor.

    Retorna:
    - True se o grafo_menor é subgrafo de grafo_maior, False caso contrário.
    """
    # Verifica se os nós de grafo_menor estão em grafo_maior
    if not set(grafo_menor.nodes()).issubset(grafo_maior.nodes()):
        return False

    # Verifica se as arestas de grafo_menor estão em grafo_maior com os mesmos valores
    for u, v, data in grafo_menor.edges(data=True):
        if not grafo_maior.has_edge(u, v) or grafo_maior[u][v] != data:
            return False

    return True

# Exemplo de uso:
grafo_maior = nx.Graph()
grafo_maior.add_edge(1, 2, weight=3)
grafo_maior.add_edge(2, 3, weight=2)
grafo_maior.add_edge(3, 1, weight=1)

grafo_menor = nx.Graph()
grafo_menor.add_edge(1, 2, weight=3)
grafo_menor.add_edge(2, 3, weight=2)

print("É subgrafo valorado:", eh_subgrafo_valorado(grafo_maior, grafo_menor))
