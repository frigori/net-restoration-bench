"""Metrics shared across all strategies: capacity overhead, restoration rate,
reaction time, churn and path stretch.
"""

from __future__ import annotations

import networkx as nx

from net_restoration_bench.solvers.base import Plan, Reaction
from net_restoration_bench.topology import Demand


def capacity_overhead(graph: nx.Graph, plan: Plan) -> float:
    """Spare capacity reserved by `plan` as a fraction of primary capacity."""
    raise NotImplementedError


def restoration_rate(demands: list[Demand], reaction: Reaction) -> float:
    """Fraction of demands that got a valid route after the failure."""
    raise NotImplementedError


def churn(before: dict[Demand, list[str]], after: dict[Demand, list[str]]) -> int:
    """Number of demands whose route changed, including unaffected ones."""
    raise NotImplementedError


def path_stretch(graph: nx.Graph, route: list[str]) -> float:
    """Route length over the shortest possible length between its endpoints."""
    raise NotImplementedError
