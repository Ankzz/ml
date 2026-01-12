import pytest
from pytest import approx

from normalize import normalize

@pytest.mark.parametrize("scores, expected",
    [
        ([0,5,10],[0.0, 0.0, 0.0]),
        ([10,10,10],[10.0,10.0,10.0]),
        ([],[])
    ]
)

def test_normalize_scores(scores, expected):
    result = normalize(scores)
    assert approx(result)==expected
