import networkx as nx


def run_betweenness(G):
    return nx.betweenness_centrality(G)
