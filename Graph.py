import networkx as nx
import matplotlib.pyplot as plt  # Opcional, usado apenas para visualização

def construir_grafo(lista_arestas, direcionado=False, valores_arestas=None, rotulos_vertices=None):
    if direcionado:
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    if valores_arestas:
        arestas_com_valores = zip(lista_arestas, valores_arestas)
        G.add_edges_from((u, v, {'valor': valor}) for (u, v), valor in arestas_com_valores)
    else:
        G.add_edges_from(lista_arestas)

    if rotulos_vertices:
        nx.set_node_attributes(G, rotulos_vertices, 'rotulo')

    return G

def visualizar_grafo(grafo):
    pos = nx.spring_layout(grafo)  # Layout para visualização
    labels = nx.get_edge_attributes(grafo, 'valor')
    nx.draw(grafo, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
    plt.show()

# Exemplo de uso:
#lista_arestas_exemplo = [(1, 2), (2, 3), (3, 1), (1, 4)]
#valores_exemplo = [10, 20, 30, 80] #excluir daqui e da função caso n precise
#rotulos_vertices_exemplo = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}

#grafo_exemplo = construir_grafo(lista_arestas_exemplo, direcionado=True, valores_arestas=valores_exemplo, rotulos_vertices=rotulos_vertices_exemplo)
#visualizar_grafo(grafo_exemplo)
