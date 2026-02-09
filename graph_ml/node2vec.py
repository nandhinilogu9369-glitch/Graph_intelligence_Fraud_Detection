import numpy as np


def node2vec(G, dim=8):
    embeddings = {}
    for node in G.nodes():
        embeddings[node] = np.random.rand(dim)
    return embeddings
