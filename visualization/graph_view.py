from pyvis.network import Network


def visualize(G, output_file, suspicious_nodes=None):
    if suspicious_nodes is None:
        suspicious_nodes = []

    net = Network(
        height="800px",
        width="100%",
        bgcolor="#ffffff",
        font_color="black",
        directed=False
    )

    # -----------------------
    # Physics & Layout Tuning
    # -----------------------
    net.toggle_physics(False)
    net.repulsion(
        node_distance=180,
        central_gravity=0.2,
        spring_length=120,
        spring_strength=0.05,
        damping=0.9
    )

    # Color mapping
    color_map = {
        "user": "#4CAF50",     # green
        "device": "#FF9800",   # orange
        "ip": "#03A9F4"        # blue
    }

    # ---------
    # Counters
    # ---------
    counts = {"user": 0, "device": 0, "ip": 0}

    # -----------
    # Add Nodes
    # -----------
    for node, attrs in G.nodes(data=True):
        ntype = attrs.get("type", "unknown")
        counts[ntype] = counts.get(ntype, 0) + 1

        degree = G.degree(node)
        is_suspicious = node in suspicious_nodes

        # Size logic: suspicious nodes dominate visually
        if is_suspicious:
            size = 28
        else:
            size = max(8, min(16, degree))

        net.add_node(
            node,
            label=node,
            color="red" if is_suspicious else color_map.get(ntype, "#9E9E9E"),
            size=size,
            title=(
                f"Node: {node}<br>"
                f"Type: {ntype}<br>"
                f"Connections: {degree}<br>"
                f"Suspicious: {is_suspicious}"
            )
        )

    # -----------
    # Add Edges (de-cluttered)
    # -----------
    for u, v, attrs in G.edges(data=True):
        # Skip weak/noisy connections
        if G.degree(u) < 2 and G.degree(v) < 2:
            continue

        etype = attrs.get("type", "interaction")
        net.add_edge(
            u,
            v,
            title=f"Event: {etype}",
            color="rgba(180,180,180,0.25)"
        )

    # -----------------
    # Add Legend Nodes
    # -----------------
    net.add_node(
        "LEGEND_USER",
        label=f"User (Green): {counts.get('user', 0)}",
        color=color_map["user"],
        shape="box",
        x=-800,
        y=-300,
        fixed=True
    )

    net.add_node(
        "LEGEND_DEVICE",
        label=f"Device (Orange): {counts.get('device', 0)}",
        color=color_map["device"],
        shape="box",
        x=-800,
        y=-200,
        fixed=True
    )

    net.add_node(
        "LEGEND_IP",
        label=f"IP (Blue): {counts.get('ip', 0)}",
        color=color_map["ip"],
        shape="box",
        x=-800,
        y=-100,
        fixed=True
    )

    net.add_node(
        "LEGEND_FRAUD",
        label=f"Suspicious (Red): {len(suspicious_nodes)}",
        color="red",
        shape="box",
        x=-800,
        y=0,
        fixed=True
    )

    net.write_html(output_file)
    print("Graph visualization saved to", output_file)
