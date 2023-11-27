import networkx as nx

def categorizar_cadeias_com_comprimento(grafo, vertice_inicial):
    """
    Categoriza, classifica e retorna as cadeias em um grafo a partir de um vértice inicial,
    incluindo o comprimento de cada cadeia.

    Parâmetros:
    - grafo: Grafo (direcionado ou não direcionado) representado por um objeto NetworkX.
    - vertice_inicial: Vértice inicial para começar a busca.

    Retorna:
    - Lista de tuplas (cadeia, comprimento, categoria),
      onde cada cadeia é uma lista de vértices, comprimento é o número de vértices na cadeia,
      e a categoria é "elementar" ou "simples".
    """
    cadeias = []
    visitados = set()

    def bfs(caminho):
        vertice_atual = caminho[-1]
        vizinhos = set(grafo.neighbors(vertice_atual)) - visitados

        for vizinho in vizinhos:
            visitados.add(vizinho)
            nova_cadeia = caminho + [vizinho]
            categoria = "elementar" if len(set(nova_cadeia)) == len(nova_cadeia) else "simples"
            cadeias.append((nova_cadeia, len(nova_cadeia), categoria))
            bfs(nova_cadeia)

    bfs([vertice_inicial])
    return cadeias

# Exemplo de uso:
grafo = nx.Graph([(1, 2), (1, 3), (2, 4), (3, 4), (4, 1)])
vertice_inicial = 1

resultado = categorizar_cadeias_com_comprimento(grafo, vertice_inicial)
print("Cadeias categorizadas com comprimento a partir do vértice", vertice_inicial, ":", resultado)
