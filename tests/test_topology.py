import pytest

from net_restoration_bench.topology import random_demands, random_network


def test_random_network_not_implemented_yet():
    with pytest.raises(NotImplementedError):
        random_network(n_nodes=10, avg_degree=3, seed=0)


def test_random_demands_not_implemented_yet():
    with pytest.raises(NotImplementedError):
        random_demands(graph=None, n_demands=5, seed=0)
