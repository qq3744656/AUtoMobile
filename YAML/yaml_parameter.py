import allure
import pytest

from YAML.sum_data import get_my_data
"""
allure generate report -o --clean ./html
"""

class TestSum:

    @allure.severity(allure.severity_level.BLOCKER)# 阻断性的级别
    @allure.step(title="描述信息")
    @pytest.mark.parametrize("a,b,c", [[1, 2, 3], [4, 5, 9], [10, 10, 20]])
    def test_sum(self, a, b, c):
        allure.attach("测试步骤和测试数据的说明eg:a%s,b%s,c%s" % (a, b, c), "文件名")
        assert a + b == c

    @allure.severity(allure.severity_level.CRITICAL) # 致命级别的BUG NORMAL一般 MINOR较轻 TRIVIAL可忽略的用例
    @pytest.mark.parametrize("a,b,c", get_my_data())
    def test01_sum(self, a, b, c):
        allure.attach("合理的修饰测试步骤的具体内容eg:a%s,b%s,c%s" % (a, b, c), "文件名自定义")
        assert a + b == c


if __name__ == '__main__':
    pytest.main(["yaml_parameter.py", "-s"])
