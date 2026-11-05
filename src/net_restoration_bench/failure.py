"""Single-link failure scenarios."""

from __future__ import annotations

from dataclasses import dataclass

import networkx as nx


@dataclass(frozen=True)
class LinkFailure:
    edge: tuple[str, str]


def single_link_failures(graph: nx.Graph) -> list[LinkFailure]:
    """One failure scenario per edge, assuming failures are never simultaneous."""
    raise NotImplementedError
