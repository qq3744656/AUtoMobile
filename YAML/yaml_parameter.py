import pytest

from YAML.sum_data import get_data


class TestSum:

    @pytest.mark.parametrize("a,b,c", [[1, 2, 3], [4, 5, 9], [10, 10, 21]])
    def test_sum(self, a, b, c):
        assert a + b == c

    @pytest.mark.parametrize("a,b,c", get_data())
    def test01_sum(self, a, b, c):
        assert a + b == c



if __name__ == '__main__':
    pytest.main(["yaml_parameter.py", "-s"])
