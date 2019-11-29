import time
from appium import webdriver

from common.base import Base

class HousePage(Base):
    def __init__(self,driver):
        self.driver=driver
    "封装表现层和操作层"
    #制作定位器
    personal_loc=("id","com.insthub.ecmobile:id/toolbar_tabfour")#个人中心定位器
    login_loc=("xpath","//*[@text='点击此处登录']")#点击登录定位器
    user_name_loc=("xpath","//*[@text='用户名']")#用户名输入框定位器
    password_loc=("id","com.insthub.ecmobile:id/login_password")#密码输入框定位器
    sign_loc=("xpath","//*[@text='登录']")#右上角登录按钮
    house_loc=("id","com.insthub.ecmobile:id/toolbar_tabone")


    "封装操作层"

    def personal_click(self):
        "点击个人中心"
        self.element_click(self.driver,self.personal_loc)
        time.sleep(1)


    def login_click(self):
        "点击登录"
        self.element_click(self.driver,self.login_loc)
        time.sleep(1)

    def username_input(self,username):
        "输入用户名"
        self.send_keys(self.driver,self.user_name_loc,text=username)

    def password_input(self,password):
        "输入密码"
        self.send_keys(self.driver,self.password_loc,text=password)

    def sign_click(self):
        "点击登录按钮"
        self.element_click(self.driver,self.sign_loc)
        time.sleep(3)

    def house_click(self):
        "点击首页"
        self.element_click(self.driver,self.house_loc)
        time.sleep(1)

    def cart_click(self):
        pass

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

    house=HousePage(driver)
    house.personal_click()
    time.sleep(1)
    house.login_click()

    username="诸葛亮_1"
    password="test123456"
    house.username_input(username)

    house.password_input(password)
    house.sign_click()
    house.house_click()