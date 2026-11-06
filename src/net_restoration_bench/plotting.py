"""The four comparison figures from the proposal, plus a quick topology view.
Each plot takes a tidy pandas DataFrame (one row per run) rather than
BenchmarkResult directly, since the columns needed here (load, network size,
churn) aren't produced by benchmark.run yet.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

from net_restoration_bench.solvers.base import Route


def overhead_vs_load(df: pd.DataFrame) -> plt.Figure:
    """Capacity overhead vs. load, one line per strategy.
    Expects columns: strategy, load, capacity_overhead.
    """
    raise NotImplementedError


def restoration_rate_vs_load(df: pd.DataFrame) -> plt.Figure:
    """Restoration rate vs. load, one line per strategy.
    Expects columns: strategy, load, restoration_rate.
    """
    raise NotImplementedError


def solver_time_vs_network_size(df: pd.DataFrame) -> plt.Figure:
    """Planning time vs. network size, log-scaled y axis.
    Expects columns: strategy, network_size, planning_time_s.
    """
    raise NotImplementedError


def churn_by_strategy(df: pd.DataFrame) -> plt.Figure:
    """Churn per strategy with confidence intervals.
    Expects columns: strategy, churn.
    """
    raise NotImplementedError


def draw_topology(
    graph: nx.Graph,
    primary_routes: dict[str, Route] | None = None,
    backup_routes: dict[str, Route] | None = None,
) -> plt.Figure:
    """Network layout with primary routes solid and backups dashed."""
    raise NotImplementedError
