"""
@Time ： 2020/2/19 22:41
@Author ： 袁琪
@File ：test_parameterize.py
@IDE ：PyCharm
"""

import pytest
import math

# pytest参数化
"""
base,exponent,expected用来定义参数名称，每一个元组都是一条测试用例的测试数据
ids参数默认为None，用于定义测试用例的名称
"""


@pytest.mark.parametrize(
    "base, exponent, expected",
    [(2, 2, 4),
     (2, 3, 8),
     (1, 9, 1),
     (0, 9, 0)],
    ids=["case1", "case2", "case3", "case4"]
)
def test_pow(base, exponent, expected):
    assert math.pow(base, exponent) == expected


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_parameterize.py"])
    # pytest.main(["-v", "-s", "test_parameterize.py", '--workers=1', '--tests-per-worker=4'])
