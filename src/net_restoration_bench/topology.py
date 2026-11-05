"""Network and traffic demand generation."""

from __future__ import annotations

from dataclasses import dataclass

import networkx as nx


@dataclass(frozen=True)
class Demand:
    source: str
    target: str
    bandwidth: float


def random_network(n_nodes: int, avg_degree: float, seed: int | None = None) -> nx.Graph:
    """Connected random graph with a 'capacity' attribute on every edge."""
    raise NotImplementedError


def random_demands(graph: nx.Graph, n_demands: int, seed: int | None = None) -> list[Demand]:
    """Sample source/target pairs from graph with random bandwidth requirements."""
    raise NotImplementedError
