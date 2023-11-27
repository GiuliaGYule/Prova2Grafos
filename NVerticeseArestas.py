import networkx as nx

def contar_vertices_arestas(grafo):
    """
    Conta o número de vértices e arestas de um grafo.

    Parâmetros:
    - grafo: Grafo representado por um objeto NetworkX.

    Retorna:
    - Uma tupla (número de vértices, número de arestas).
    """
    num_vertices = nx.number_of_nodes(grafo)
    num_arestas = nx.number_of_edges(grafo)
    return num_vertices, num_arestas

# Exemplo de uso:
grafo_exemplo = nx.Graph([(1, 2), (2, 3), (3, 1)])

num_vertices, num_arestas = contar_vertices_arestas(grafo_exemplo)

print(f"O grafo possui {num_vertices} vértices e {num_arestas} arestas.")
