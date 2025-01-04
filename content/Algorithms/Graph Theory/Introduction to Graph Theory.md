---
title: Introduction to Graph Theory
tags:
  - algorithms
  - graph-theory
  - graph
date: 2025-01-04
---

## Types of graphs

- **Undirected graph**: a graph whose edges can be traversed in either direction
- **Directed graph**: a graph whose edges can only be traversed in a specified direction (usually indicated by an arrow) ^directed-graph
- **Weighted graph**: a graph whose edges are given numerical weights
- **Bipartite graph**: a graph which can be split into two groups such that no two vertices in each group are connected by an edge
  - Chromatic number is at most 2. It is 1 if there are no edges.
- **Complete graph**: a graph where every two vertices are connected by an edge, the degree of every node is $N - 1$. The graph contained all possible edges between the nodes.
- **Regular graph**: a graph whose vertices all have the same degree. A graph whose vertices have degree $k$ is called a $k$-regular graph.
- **Connected graph**: a graph in which there exists a path between every pair of vertices
- **Simple graph**: a graph with no self-loops and no multiple edges
- **Acyclic graph**: a graph with no cycles
- **Tree**: an undirected, acyclic, connected graph where there exists exactly one path between any pair of vertices

Fun fact: for a graph with $N$ vertices,

- it has $N - 1$ edges
- it is acyclic
- it is connected

If any two conditions mentioned earlier are satisfied, so is the third one.

- The degree of a node is the number of its neighbours. The sum of degrees in a graph is always $2m$, where $m$ is the number of edges, because each edge increases the degree of exactly two nodes by one.
