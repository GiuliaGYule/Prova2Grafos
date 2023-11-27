import networkx as nx
import matplotlib.pyplot as plt

def distribuicao_graus(grafo):
    """
    Imprime a distribuição dos graus de um grafo.

    Parâmetros:
    - grafo: Grafo representado por um objeto NetworkX.
    """
    graus = dict(nx.degree(grafo))
    histograma = nx.degree_histogram(grafo)

    print("Distribuição dos Graus:")
    for grau, frequencia in enumerate(histograma):
        if frequencia > 0:
            print(f"Grau {grau}: {frequencia} vértices")

    # Visualização do histograma (opcional)
    plt.bar(range(len(histograma)), histograma, align="center")
    plt.title("Distribuição dos Graus")
    plt.xlabel("Grau")
    plt.ylabel("Frequência")
    plt.show()

# Exemplo de uso:
grafo_exemplo = nx.Graph([(1, 2), (2, 3), (3, 4), (4, 1), (4, 2)])

distribuicao_graus(grafo_exemplo)
