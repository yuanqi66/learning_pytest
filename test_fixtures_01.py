"""
@Time ： 2020/2/19 21:44
@Author ： 袁琪
@File ：test_fixtures_01.py
@IDE ：PyCharm
"""
import pytest

# 功能函数
def multiply(a, b):
    return a * b

# =====Fixture======
def setup_module(module):
    print("setup_module=================>")

def teardown_module(module):
    print("teardown_module=================>")

def setup_function(function):
    print("setup_function-------->")

def teardown_function(function):
    print("teardown_function-------->")

def setup():
    print("setup------->")

def teardown():
    print("teardown-------->")

# =======测试用例==========
def test_multiply_3_4():
    print('test_number_3_4')
    assert multiply(3, 4) == 12

def test_multiply_a_3():
    print('test_numbers_a_3')
    assert multiply('a', 3) == 'aaa'


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_fixtures_01.py"])
