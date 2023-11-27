import networkx as nx
from Graph import construir_grafo, visualizar_grafo

def grau_vertice(grafo, vertice):
    """
    Imprime o grau do vértice em um grafo.

    Parâmetros:
    - grafo: Grafo representado por um objeto NetworkX.
    - vertice: Vértice cujo grau será impresso.

    Retorna:
    - Nenhum (a função apenas imprime).
    """
    if nx.is_directed(grafo):
        grau_entrada = grafo.in_degree(vertice)
        grau_saida = grafo.out_degree(vertice)
        print(f"Grau de entrada do vértice {vertice}: {grau_entrada}")
        print(f"Grau de saída do vértice {vertice}: {grau_saida}")
    else:
        grau = grafo.degree(vertice)
        print(f"Grau do vértice {vertice}: {grau}")

lista_arestas = [(1, 2), (1, 3), (2, 3)]
grafo = construir_grafo(lista_arestas, direcionado=True, valores_arestas=None, rotulos_vertices=None)
visualizar_grafo(grafo)
vertice_escolhido = 3
grau_vertice(grafo, vertice_escolhido)
# Escolher um vértice para encontrar o grau
#vertice_escolhido_direcionado = 3

# Obter o grau do vértice
#grau_entrada, grau_saida = grau_do_vertice(grafo_direcionado, vertice_escolhido_direcionado)

#print(f"Grau de entrada do vértice {vertice_escolhido_direcionado}: {grau_entrada}")
#print(f"Grau de saída do vértice {vertice_escolhido_direcionado}: {grau_saida}")