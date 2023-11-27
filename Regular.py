import networkx as nx
from Graph import construir_grafo

def verificar_regularidade(grafo, direcionado=False, grau='total'):
    if direcionado and grau not in ['entrada', 'saida', 'total']:
        print("Para grafos direcionados, escolha 'entrada', 'saida' ou 'total' para verificar regularidade.")
        return False
    elif not direcionado and grau != 'total':
        print("Para grafos não direcionados, escolha 'total' para verificar regularidade.")
        return False

    if direcionado:
        if grau == 'entrada':
            graus = [grafo.in_degree(v) for v in grafo.nodes()]
        elif grau == 'saida':
            graus = [grafo.out_degree(v) for v in grafo.nodes()]
        else:  # grau == 'total'
            graus = [grafo.degree(v) for v in grafo.nodes()]
    else:
        graus = [grafo.degree(v) for v in grafo.nodes()]

    regular = all(grau == graus[0] for grau in graus)

    if regular:
        print(f"O grafo é regular em termos de grau de {grau}.")
        print(f"Todos os vértices têm grau de {graus[0]} de {grau}.")
    else:
        print(f"O grafo não é regular em termos de grau de {grau}.")

    return regular

# Exemplo de lista de arestas para um grafo não direcionado
lista_arestas_exemplo_nao_direcionado = [(1, 2), (2, 3), (3, 1)]

# Construir o grafo não direcionado
grafo_nao_direcionado = construir_grafo(lista_arestas_exemplo_nao_direcionado, direcionado=False)

# Verificar a regularidade do grafo em termos de grau total
verificar_regularidade(grafo_nao_direcionado, direcionado=False, grau='total')

# Exemplo de lista de arestas para um grafo direcionado
lista_arestas_exemplo_direcionado = [(1, 2), (2, 3), (3, 1), (3, 4)]

# Construir o grafo direcionado
grafo_direcionado = construir_grafo(lista_arestas_exemplo_direcionado, direcionado=False)

# Verificar a regularidade do grafo em termos de grau de entrada
verificar_regularidade(grafo_direcionado, direcionado=False, grau='entrada')

# Verificar a regularidade do grafo em termos de grau total
verificar_regularidade(grafo_direcionado, direcionado=False, grau='total')