import time
from appium.webdriver import webdriver
from common.base import Base
from page.housepage import HousePage


class CartPage(Base):
    payment_loc = ("xpath", "//*[@text='结算']")

    def __init__(self, driver):
        self.driver = driver

    def pay_click(self):
        "点击购物车中结算按钮"
        self.element_click(self.driver, self.payment_loc)
        time.sleep(1)


if __name__ == '__main__':
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

    house = HousePage(driver)
    house.personal_click()
    time.sleep(1)
    house.login_click()

    username = "tianchuntian"
    password = "123456"
    house.username_input(username)
    house.password_input(password)
    house.sign_click()
    house.house_click()
