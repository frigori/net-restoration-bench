"""Fast Reroute: precompute a local bypass for every link, so only the
segment around a failure is replaced and reaction is near-instant.
"""

from __future__ import annotations

import networkx as nx

from net_restoration_bench.failure import LinkFailure
from net_restoration_bench.solvers.base import Plan, Reaction, RecoveryStrategy
from net_restoration_bench.topology import Demand


class FastReroute(RecoveryStrategy):
    def plan(self, graph: nx.Graph, demands: list[Demand]) -> Plan:
        # Shortest paths for primaries, plus a precomputed bypass for every
        # link (e.g. shortest path between its endpoints excluding the link).
        raise NotImplementedError

    def react(self, graph: nx.Graph, plan: Plan, failure: LinkFailure) -> Reaction:
        # Splice the precomputed bypass for `failure.edge` into each
        # affected demand's route; nothing else changes.
        raise NotImplementedError
