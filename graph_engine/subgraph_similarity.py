"""
Subgraph Similarity Detection
----------------------------

MAX_SIM_NODES = 20
suspicious_node_ids = suspicious_node_ids[:MAX_SIM_NODES]

Detects structurally similar subgraphs that may indicate
reused fraud patterns or coordinated fraud rings.

Approach:
- Extract ego-graphs around candidate nodes
- Compare subgraphs using Jaccard similarity on:
  - Neighbor sets
  - Node type distributions
  - Edge type distributions

No ML used. Fully explainable graph reasoning.
"""

import networkx as nx
from itertools import combinations
from collections import Counter


def extract_ego_subgraph(G, node, radius=2):
    """
    Extract ego graph centered at `node`
    """
    return nx.ego_graph(G, node, radius=radius)


def _node_type_signature(subgraph):
    return Counter(
        subgraph.nodes[n].get("type", "unknown")
        for n in subgraph.nodes
    )


def _edge_type_signature(subgraph):
    return Counter(
        subgraph.edges[e].get("type", "unknown")
        for e in subgraph.edges
    )


def jaccard_similarity(dict_a, dict_b):
    """
    Compute Jaccard similarity between two feature dictionaries
    """
    set_a = set(dict_a.keys())
    set_b = set(dict_b.keys())

    if not set_a and not set_b:
        return 0.0

    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)

    return len(intersection) / len(union)


def subgraph_similarity_score(g1, g2):
    """
    Compute similarity score between two subgraphs
    """
    node_sim = jaccard_similarity(
        _node_type_signature(g1),
        _node_type_signature(g2)
    )

    edge_sim = jaccard_similarity(
        _edge_type_signature(g1),
        _edge_type_signature(g2)
    )

    neighbor_sim = jaccard_similarity(
        Counter(g1.nodes),
        Counter(g2.nodes)
    )

    return round((node_sim + edge_sim + neighbor_sim) / 3, 4)


def detect_similar_subgraphs(G, candidate_nodes, radius=2, threshold=0.75):
    """
    Identify pairs of nodes whose surrounding subgraphs
    are structurally similar.
    """
    ego_graphs = {
        n: extract_ego_subgraph(G, n, radius)
        for n in candidate_nodes
    }

    similar_pairs = []

    for n1, n2 in combinations(candidate_nodes, 2):
        score = subgraph_similarity_score(
            ego_graphs[n1],
            ego_graphs[n2]
        )

        if score >= threshold:
            similar_pairs.append({
                "node_1": n1,
                "node_2": n2,
                "similarity_score": score
            })

    return similar_pairs


if __name__ == "__main__":
    print("Subgraph similarity module loaded.")
