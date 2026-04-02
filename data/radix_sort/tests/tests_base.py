import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from base_us import radix_sort as base_radix_sort
from modified_es import ordenamiento_radix as es_radix_sort
from modified_obf import oirewuond as obf_radix_sort


TEST_CASES = [
    [170, 45, 75, 90, 802, 24, 2, 66],
    [1],
    [5, 3, 8, 1, 9, 2],
    [100, 200, 300, 10, 20],
    [999, 1, 500, 42, 7],
    [0, 0, 0],
    [1000000, 999999, 1],
]


@pytest.mark.parametrize("array", TEST_CASES)
def test_base_and_es_same_output(array):
    result_base = base_radix_sort(array.copy())
    result_es = es_radix_sort(array.copy())
    assert result_base == result_es


@pytest.mark.parametrize("array", TEST_CASES)
def test_base_output_is_sorted(array):
    result = base_radix_sort(array.copy())
    assert result == sorted(array)


@pytest.mark.parametrize("array", TEST_CASES)
def test_es_output_is_sorted(array):
    result = es_radix_sort(array.copy())
    assert result == sorted(array)


@pytest.mark.parametrize("array", TEST_CASES)
def test_base_and_obf_same_output(array):
    result_base = base_radix_sort(array.copy())
    result_obf = obf_radix_sort(array.copy())
    assert result_base == result_obf