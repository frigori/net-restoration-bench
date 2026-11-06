import pandas as pd
import pytest

from net_restoration_bench.plotting import overhead_vs_load


def test_overhead_vs_load_not_implemented_yet():
    with pytest.raises(NotImplementedError):
        overhead_vs_load(pd.DataFrame())
