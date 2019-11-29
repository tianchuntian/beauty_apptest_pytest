import time

import pytest
from appium import webdriver


@pytest.fixture()
def driver1(request):
    desired_caps = {
        "platformName": "android",
        "platformVersion": "5.1.1",
        "deviceName": "127.0.0.1:21503",
        "appPackage": "com.insthub.ecmobile",
        "appActivity": ".activity.EcmobileMainActivity",
        "unicodeKeyboard": True,
        "resetKeyboard": True
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    # time.sleep(2)

    # def end():
    #     driver.quit()  # 关闭app
    # # addfinalizer()用于用例执行完之后的操作
    # request.addfinalizer(end)  # 执行终结函数

    return driver
