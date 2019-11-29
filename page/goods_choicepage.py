import time

from common.base import Base
from appium import webdriver

class GoodsChoicePage(Base):
    def __init__(self,driver):
        self.driver=driver
    "封装定位器"
    mobile_loc=("xpath","//*[@text='手机']")
    chen_x=400
    chen_y=200
    cart_loc=("xpath","//*[@text='加入购物车']")
    car_loc=("id","com.insthub.ecmobile:id/good_detail_shopping_cart")
    "封装点击手机的操作"
    def mobile_click(self):
        "点击手机"
        self.element_click(self.driver,self.mobile_loc)
        time.sleep(1)

    def cheng_click(self):
        "点击秤"
        self.element_tap(self.driver,self.chen_x,self.chen_y)
        time.sleep(1)

    def add_cart(self):
        "加入购物车"
        self.element_click(self.driver,self.cart_loc)
        time.sleep(1)

    def car_click(self):
        "点击购物车"
        self.element_click(self.driver,self.car_loc)
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

    goods=GoodsChoicePage(driver)
    goods.mobile_click()
    time.sleep(2)
    goods.cheng_click()
    goods.add_cart()
    goods.car_click()