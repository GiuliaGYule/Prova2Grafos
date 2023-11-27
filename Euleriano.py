import networkx as nx

def eh_euleriano(grafo):
    """
    Verifica se um grafo é euleriano.

    Parâmetros:
    - grafo: Grafo representado por um objeto NetworkX.

    Retorna:
    - True se o grafo é euleriano, False caso contrário.
    """
    # Verifica se todos os vértices têm grau par
    return all(grau % 2 == 0 for grau in dict(grafo.degree()).values())

# Exemplo de uso:
grafo_euleriano = nx.Graph([(1, 2), (2, 3), (3, 1)])
grafo_nao_euleriano = nx.Graph([(1, 2), (2, 3), (3, 4)])

print("O grafo é euleriano:", eh_euleriano(grafo_euleriano))
print("O grafo não é euleriano:", eh_euleriano(grafo_nao_euleriano))
