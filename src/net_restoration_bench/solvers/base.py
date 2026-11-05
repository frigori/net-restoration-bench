"""Common interface every recovery strategy implements, so they can be benchmarked
on the same metrics in net_restoration_bench.benchmark.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

import networkx as nx

from net_restoration_bench.failure import LinkFailure
from net_restoration_bench.topology import Demand

Route = list[str]  # sequence of node ids from source to target


@dataclass(frozen=True)
class Plan:
    """Output of plan(): a primary route per demand, plus whatever spare
    capacity or backup routes the strategy reserved ahead of any failure.
    """

    primary_routes: dict[Demand, Route]
    reserved_capacity: dict[tuple[str, str], float]


@dataclass(frozen=True)
class Reaction:
    """Output of react(): the routes actually carrying traffic after a failure,
    and the wall-clock time the strategy took to produce them.
    """

    routes: dict[Demand, Route]
    reaction_time_s: float


class RecoveryStrategy(ABC):
    """Base class for SBPP, Fast Reroute and global recompute."""

    @abstractmethod
    def plan(self, graph: nx.Graph, demands: list[Demand]) -> Plan:
        """Precompute routes (and any spare capacity) before any failure happens."""

    @abstractmethod
    def react(self, graph: nx.Graph, plan: Plan, failure: LinkFailure) -> Reaction:
        """Produce the routes that carry traffic once `failure` has occurred."""
