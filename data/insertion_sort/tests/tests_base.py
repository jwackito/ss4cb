import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from base_us import insertion_sort as base_insertion_sort
from modified_es import ordenar_por_insercion as es_insertion_sort
from modified_obf import a as obf_insertion_sort


TEST_CASES = [
    [64, 34, 25, 12, 22, 11, 90],
    [1],
    [5, 3, 8, 1, 9, 2],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [3, 3, 3, 3],
    [-5, -1, -3, -2, -4],
    [0, -1, 1, -2, 2],
]


@pytest.mark.parametrize("array", TEST_CASES)
def test_base_and_es_same_output(array):
    result_base = base_insertion_sort(array.copy())
    result_es = es_insertion_sort(array.copy())
    assert result_base == result_es


@pytest.mark.parametrize("array", TEST_CASES)
def test_base_output_is_sorted(array):
    result = base_insertion_sort(array.copy())
    assert result == sorted(array)


@pytest.mark.parametrize("array", TEST_CASES)
def test_es_output_is_sorted(array):
    result = es_insertion_sort(array.copy())
    assert result == sorted(array)


@pytest.mark.parametrize("array", TEST_CASES)
def test_base_and_obf_same_output(array):
    result_base = base_insertion_sort(array.copy())
    result_obf = obf_insertion_sort(array.copy())
    assert result_base == result_obf