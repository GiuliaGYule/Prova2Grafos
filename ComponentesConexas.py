import networkx as nx

def componentes_conexas(grafo):
    """
    Encontra as componentes conexas de um grafo (direcionado ou não).

    Parâmetros:
    - grafo: Grafo representado por um objeto NetworkX.

    Retorna:
    - Lista de listas, onde cada lista contém os vértices de uma componente conexa.
    """
    if isinstance(grafo, nx.DiGraph):
        return [list(componente) for componente in nx.strongly_connected_components(grafo)]
    else:
        return [list(componente) for componente in nx.connected_components(grafo)]

# Exemplo de uso:
grafo_direcionado = nx.DiGraph([(1, 2), (2, 3), (4, 5)])
grafo_nao_direcionado = nx.Graph([(1, 2), (2, 3), (4, 5)])

componentes_direcionado = componentes_conexas(grafo_direcionado)
componentes_nao_direcionado = componentes_conexas(grafo_nao_direcionado)

print("Componentes conexas no grafo direcionado:", componentes_direcionado)
print("Componentes conexas no grafo não direcionado:", componentes_nao_direcionado)
