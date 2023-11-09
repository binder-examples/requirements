import pytest

from poetrypackage import data_science


def test_analyze_customer_data():
    # TODO: write the test!
    # import pdb; pdb.set_trace()
    res = data_science.analyze_customer_data()
    assert res
