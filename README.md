<<<<<<< HEAD
# Graph Intelligence Platform for Fraud Detection

## 🎯 Project Objective

The objective of this project is to build an **end-to-end graph-native fraud detection system** that identifies:

* Fraud rings
* Collusive behavior
* Influential and suspicious entities

Instead of relying on black-box machine learning models, this system prioritizes **graph reasoning, structure-aware analysis, and explainability**.

---

## 🧠 High-Level Architecture

**Pipeline Overview**

Data → Graph Construction → Graph Algorithms → Fraud Signals → Visualization

**Execution Flow:**

1. Generate or load transactional / event data
2. Construct an entity–event graph
3. Apply graph algorithms
4. Identify suspicious nodes and subgraphs
5. Visualize fraud networks interactively

---

## ⚙️ Proof of Concept (PoC)

The Proof of Concept demonstrates that the complete graph-based fraud detection pipeline executes successfully and produces meaningful results.

### How to Run

1️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

2️⃣ **Run the Pipeline**

```bash
python run_pipeline.py
```

---

## 📤 Outputs

After execution, the system generates the following artifacts:

### 🔎 Interactive Visualization

* `fraud_graph.html`

  * Interactive graph showing detected fraud patterns
  * Nodes represent entities
  * Edges represent relationships or transactions

Open the visualization by launching the file in any web browser.

### 📊 Console Outputs

The console logs display:

* High-risk nodes
* Centrality scores
* Community-level anomalies

These outputs validate the correctness of the fraud detection logic.

---

## ✅ Key Highlights

* Graph-first fraud detection approach
* Explainable algorithms (PageRank, Betweenness Centrality, Louvain Community Detection)
* Subgraph analysis for fraud pattern discovery
* Fully reproducible and modular pipeline

---

## 📌 Tech Stack

* Python
* NetworkX
* Graph algorithms (centrality, community detection)
* HTML-based interactive graph visualization

---

## 📘 Summary

This project demonstrates how **graph intelligence** can uncover fraud patterns that are difficult to detect using traditional ML approaches.

The emphasis is on **explainability, reasoning, and structural insights**, making the system suitable for fraud analysis and investigation workflows.
=======
# Graph_intelligence_Fraud_Detection
>>>>>>> 7a31499adffb4841215280010d8845959b605ebb
