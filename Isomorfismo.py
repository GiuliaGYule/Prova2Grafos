import networkx as nx

def sao_isomorfos(grafo1, grafo2):
    """
    Verifica se dois grafos são isomorfos.

    Parâmetros:
    - grafo1, grafo2: Grafos representados por objetos NetworkX.

    Retorna:
    - True se os grafos são isomorfos, False caso contrário.
    """
    return nx.is_isomorphic(grafo1, grafo2)

# Exemplo de uso:
grafo1 = nx.Graph([('1', '2'), ('2', '3'), ('3', '1'), ('2', '4')])
grafo2 = nx.Graph([('A', 'B'), ('B', 'C'), ('C', 'A'), ('B', 'D')])

sao_isomorfos = sao_isomorfos(grafo1, grafo2)

print("Os grafos são isomorfos:", sao_isomorfos)
