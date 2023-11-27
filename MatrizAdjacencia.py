import networkx as nx
import numpy as np
from Graph import construir_grafo

def matriz_adjacencia(grafo):
    return nx.adjacency_matrix(grafo).todense()

def sucessores_e_antecessores(grafo, vertice):
    sucessores = list(grafo.successors(vertice))
    antecessores = list(grafo.predecessors(vertice))
    return sucessores, antecessores


# Escolher um vértice para encontrar sucessores e antecessores
#vertice_escolhido = 3

# Obter sucessores e antecessores
#sucessores, antecessores = sucessores_e_antecessores(grafo_direcionado, vertice_escolhido)

#print(f"Sucessores de {vertice_escolhido}: {sucessores}")
#print(f"Antecessores de {vertice_escolhido}: {antecessores}")

# Construir a matriz de adjacência
#matriz = matriz_adjacencia(grafo)

#print("Matriz de Adjacência:")
#print(matriz)