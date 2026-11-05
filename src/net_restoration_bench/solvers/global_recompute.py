"""Global recompute: no reserved capacity. After a failure, a central
controller re-solves routing for every demand on the network as it now is.
"""

from __future__ import annotations

import networkx as nx

from net_restoration_bench.failure import LinkFailure
from net_restoration_bench.solvers.base import Plan, Reaction, RecoveryStrategy
from net_restoration_bench.topology import Demand


class GlobalRecompute(RecoveryStrategy):
    def plan(self, graph: nx.Graph, demands: list[Demand]) -> Plan:
        # MILP over the intact network; no spare capacity reserved.
        raise NotImplementedError

    def react(self, graph: nx.Graph, plan: Plan, failure: LinkFailure) -> Reaction:
        # Remove failure.edge from the graph and re-solve the same MILP
        # for every demand (monolithic variant; an incremental one could
        # warm-start from `plan`).
        raise NotImplementedError
