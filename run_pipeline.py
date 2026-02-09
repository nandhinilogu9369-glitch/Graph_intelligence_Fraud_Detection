from data_generator.generate_events import generate_events
from graph_engine.graph_builder import build_graph

from algorithms.pagerank import run_pagerank
from algorithms.betweenness import run_betweenness
from algorithms.community_louvain import detect_communities
from graph_engine.subgraph_similarity import detect_similar_subgraphs

from visualization.graph_view import visualize


def main():
    print("Generating synthetic events...")
    generate_events("events.csv", 300)

    print("Building graph...")
    G = build_graph("events.csv")

    print("Running graph algorithms...")
    pr = run_pagerank(G)
    bc = run_betweenness(G)
    # ----------------------------------------
    # Community Detection (Filtered Subgraph)
    # ----------------------------------------
    community_nodes = [
    n for n, data in G.nodes(data=True)
    if data.get("type") in ("user", "device")
]

    community_graph = G.subgraph(community_nodes)
    communities = detect_communities(community_graph)
    print("\nCommunity sizes:")

    for idx, members in enumerate(communities):
       print(f"Community {idx}: {len(members)} nodes")



    print("\nTop PageRank Nodes:")
    for k, v in sorted(pr.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(k, round(v, 4))

    print("\nTop Betweenness Nodes:")
    for k, v in sorted(bc.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(k, round(v, 4))

    print(f"\nCommunities detected: {len(communities)}")

    # -------------------------------
    # Fraud Scoring (Graph Reasoning)
    # -------------------------------
    fraud_scores = {}
    for node in G.nodes():
        fraud_scores[node] = (
            pr.get(node, 0) * 0.6 +
            bc.get(node, 0) * 0.4
        )

    suspicious_nodes = sorted(
        fraud_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    suspicious_node_ids = [n for n, _ in suspicious_nodes]

    # -------------------------------
    # Scalability safeguard
    # -------------------------------
    MAX_SIM_NODES = 20
    suspicious_node_ids = suspicious_node_ids[:MAX_SIM_NODES]

    print("\nTop Suspicious Nodes:")
    for n, s in suspicious_nodes:
        print(n, round(s, 4))

    # ----------------------------------------
    # Subgraph Similarity Detection
    # ----------------------------------------
    print("\nRunning subgraph similarity detection...")

    similar_subgraphs = detect_similar_subgraphs(
        G=G,
        candidate_nodes=suspicious_node_ids,
        radius=2,
        threshold=0.75
    )

    if similar_subgraphs:
        print(f"Structurally similar subgraphs found: {len(similar_subgraphs)}")
        for pair in similar_subgraphs:
            print(
                f"Nodes {pair['node_1']} ↔ {pair['node_2']} | "
                f"Similarity: {pair['similarity_score']}"
            )
    else:
        print("No structurally similar subgraphs detected.")

    # -------------------------------
    # Visualization
    # -------------------------------
    visualize(
        G,
        "fraud_graph.html",
        suspicious_nodes=suspicious_node_ids
    )

    print("\nVisualization complete.")
    print("Open fraud_graph.html in your browser.")


if __name__ == "__main__":
    main()
