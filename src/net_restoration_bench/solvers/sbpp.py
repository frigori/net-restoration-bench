"""Shared Backup Path Protection: offline MILP picks a backup route per primary
and lets backups share spare capacity, since single-link failures never
overlap in time.
"""

from __future__ import annotations

import networkx as nx

from net_restoration_bench.failure import LinkFailure
from net_restoration_bench.solvers.base import Plan, Reaction, RecoveryStrategy
from net_restoration_bench.topology import Demand


class SBPP(RecoveryStrategy):
    def plan(self, graph: nx.Graph, demands: list[Demand]) -> Plan:
        # MILP: route each demand's primary, then route a backup disjoint
        # from the primary's links, minimizing shared spare capacity.
        raise NotImplementedError

    def react(self, graph: nx.Graph, plan: Plan, failure: LinkFailure) -> Reaction:
        # Switch affected demands to their precomputed backup; everything
        # else keeps its primary route.
        raise NotImplementedError
