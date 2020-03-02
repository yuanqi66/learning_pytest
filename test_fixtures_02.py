"""
@Time ： 2020/2/19 22:22
@Author ： 袁琪
@File ：test_fixtures_02.py
@IDE ：PyCharm
"""
import pytest
# 功能函数


def multiply(a, b):
    return a * b


class TestMultiply:
    # =====Fixture=====
    @classmethod
    def setup_class(cls):
        print("setup_class============>")

    @classmethod
    def teardown_class(cls):
        print("teardown_class============>")

    def setup_method(self, method):
        print("setup_method------>>")

    def teardown_method(self, method):
        print("teardown_method------>>")

    def setup(self):
        print("setup----->")

    def teardown(self):
        print("teardown----->")

    # ======测试用例======
    def test_numbers_5_6(self):
        print('test_number_5_6')
        assert multiply(5, 6) == 30

    def test_strings_b_2(self):
        print('test_strings_b_2')
        assert multiply('b', 2) == 'bb'


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_fixtures_02.py'])
