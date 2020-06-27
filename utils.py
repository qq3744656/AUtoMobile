import os

from appium import webdriver


class Driver:
    __driver = None

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            desireg_caps = {
                # 测试平台名字
                "platformName": "Android",
                # 测试平台对应的系统版本 不知道可以为空 appium自动识别版本
                "paatformVersion": "5.1",
                # 设备的名字 随意输入
                "deviceName": "samsung",
                # 测试app的包名
                "appPackage": "com.android.settings",
                # 测试app启动名
                "appActivity": ".Settings"
            }
            cls.__driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desireg_caps)
            cls.__driver.implicitly_wait(10)
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        cls.__driver.quit()


URL = os.path.dirname(os.path.abspath(__file__))
