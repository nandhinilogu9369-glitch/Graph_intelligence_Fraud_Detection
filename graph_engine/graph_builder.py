import csv
import networkx as nx


def build_graph(event_file):
    G = nx.Graph()

    with open(event_file) as f:
        reader = csv.DictReader(f)

        for row in reader:
            G.add_node(row["user"], type="user")
            G.add_node(row["device"], type="device")
            G.add_node(row["ip"], type="ip")

            G.add_edge(row["user"], row["device"], type=row["event"])
            G.add_edge(row["device"], row["ip"], type="access")

    return G
