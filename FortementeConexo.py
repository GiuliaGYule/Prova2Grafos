import networkx as nx

def eh_fortemente_conexo(grafo):
    """
    Verifica se um grafo é fortemente conexo.

    Parâmetros:
    - grafo: Grafo representado por um objeto NetworkX.

    Retorna:
    - True se o grafo é fortemente conexo (direcionado) ou conexo (não direcionado),
      False caso contrário.
    """
    if isinstance(grafo, nx.DiGraph):
        return nx.is_strongly_connected(grafo)
    else:
        return nx.is_connected(grafo)
import networkx as nx

def componentes_fortemente_conexas(grafo):
    """
    Encontra as componentes fortemente conexas de um grafo direcionado.

    Parâmetros:
    - grafo: Grafo dirigido representado por um objeto NetworkX.

    Retorna:
    - Lista de conjuntos, onde cada conjunto contém os vértices de uma componente fortemente conexa.
    """
    if isinstance(grafo, nx.DiGraph):
        return list(nx.strongly_connected_components(grafo))
    else:
        raise ValueError("Esta função é específica para grafos direcionados.")

# Exemplo de uso:
grafo_direcionado = nx.DiGraph([(1, 2), (2, 3), (3, 1), (4, 5)])
# Componentes fortemente conexas no grafo dirigido: [{1, 2, 3}, {4, 5}]
componentes_fortemente_conexas_direcionado = componentes_fortemente_conexas(grafo_direcionado)

print("Componentes fortemente conexas no grafo dirigido:", componentes_fortemente_conexas_direcionado)

# Exemplo de uso:
grafo_direcionado = nx.DiGraph([(1, 2), (2, 3), (3, 1)])
grafo_nao_direcionado = nx.Graph([(1, 2), (2, 3), (4, 5)])

fortemente_conexo_direcionado = eh_fortemente_conexo(grafo_direcionado)
fortemente_conexo_nao_direcionado = eh_fortemente_conexo(grafo_nao_direcionado)

print("É fortemente conexo (grafo direcionado):", fortemente_conexo_direcionado)
print("É fortemente conexo (grafo não direcionado):", fortemente_conexo_nao_direcionado)
