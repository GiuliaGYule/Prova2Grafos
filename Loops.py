import networkx as nx
from Graph import construir_grafo

def verificar_lacos(grafo):
    laços = list(nx.selfloop_edges(grafo))
    numero_de_lacos = len(laços)

    if numero_de_lacos > 0:
        print(f"O grafo possui {numero_de_lacos} laço(s) nas arestas:")
        for laço in laços:
            print(laço)
    else:
        print("O grafo não possui laços.")

    return numero_de_lacos

# Exemplo de lista de arestas com um laço
lista_arestas_exemplo_com_laco = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 4), (3, 3)]

# Construir o grafo
grafo_com_laco = construir_grafo(lista_arestas_exemplo_com_laco, direcionado=False)

# Verificar a presença de laços
numero_de_lacos = verificar_lacos(grafo_com_laco)