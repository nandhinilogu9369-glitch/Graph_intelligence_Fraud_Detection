# DESIGN.md

## Design Philosophy

This project is built as a **graph-native fraud detection system** that emphasizes reasoning, structure, and explainability.

The core idea is:

> Understand relationships first, then detect fraud.

Instead of treating fraud detection as a pure prediction problem, the system models entities and interactions explicitly as a graph.

---

## Why Graph Intelligence Instead of Pure ML

Traditional ML-based fraud systems often:

* Treat transactions as independent records
* Miss collusive or coordinated behavior
* Produce black-box decisions

Graph intelligence enables:

* Detection of fraud rings and communities
* Identification of influential or central entities
* Relationship-aware anomaly detection

Graph algorithms naturally capture **who is connected to whom and how**, which is critical in fraud scenarios.

---

## Key Design Choices

### Graph-First Architecture

All data is transformed into an **entity–event graph** before analysis.

Benefits:

* Preserves relational structure
* Enables multi-hop reasoning
* Supports explainable investigations

---

### Explainable Algorithms

The system relies on interpretable graph algorithms:

* PageRank for influence analysis
* Betweenness centrality for broker detection
* Louvain community detection for fraud rings

Each score has a clear meaning, making results auditable.

---

### Modular Pipeline

The pipeline is split into independent stages:

* Data generation / ingestion
* Graph construction
* Algorithm execution
* Fraud signal aggregation
* Visualization

This improves:

* Maintainability
* Debugging
* Extensibility

---

## Trade-offs

Intentional trade-offs made in this design:

* No deep learning on graphs (e.g., GNNs)
* Focus on clarity over maximum accuracy
* Batch-oriented execution instead of real-time

These trade-offs favor explainability and ownership over raw performance.

---

## Limitations

Current limitations include:

* Not optimized for very large-scale graphs
* No streaming or incremental graph updates
* Limited automated threshold tuning

These are acceptable for a Proof of Concept.

---

## Future Improvements

Potential enhancements:

* Streaming graph updates
* Graph Neural Network integration
* Temporal graph analysis
* Advanced subgraph similarity detection
* Alerting and monitoring dashboards

The modular design allows these upgrades without major refactoring.

---

## Design Ownership Statement

All architectural decisions were made deliberately to demonstrate **how fraud is reasoned about using graph structures**, not just detected.

This project reflects end-to-end understanding, explainability, and system-level thinking.
