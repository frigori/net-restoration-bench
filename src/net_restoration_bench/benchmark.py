"""Runs every strategy over the same topologies and failure scenarios, and
collects the metrics needed to compare them.
"""

from __future__ import annotations

from dataclasses import dataclass

import networkx as nx

from net_restoration_bench.failure import LinkFailure
from net_restoration_bench.solvers.base import RecoveryStrategy
from net_restoration_bench.topology import Demand


@dataclass(frozen=True)
class BenchmarkResult:
    strategy: str
    failure: LinkFailure
    capacity_overhead: float
    restoration_rate: float
    reaction_time_s: float
    path_stretch: float


def run(
    graph: nx.Graph,
    demands: list[Demand],
    failures: list[LinkFailure],
    strategies: dict[str, RecoveryStrategy],
) -> list[BenchmarkResult]:
    """Plan once per strategy, then react to every failure scenario and
    record metrics for each (strategy, failure) pair.
    """
    raise NotImplementedError
