"对selenium和appium中的方法进行二次封装"
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
class Base:
    def element_click(self,driver,locator):
        "点击元素"
        try:
            element=WebDriverWait(driver=driver,timeout=5).until(EC.presence_of_element_located(locator))
            element.click()
            return element
        except:
            print(f"元素{locator}未找到!")
            return False

    def send_keys(self,driver,locator,text):
        "输入内容"
        try:
            element=WebDriverWait(driver=driver,timeout=5).until(EC.presence_of_element_located(locator))
            element.send_keys(text)
        except:
            print(f"元素{locator}未找到!")
            return False

    def element_tap(self,driver,x,y):
        "轻敲元素"
        try:

            TouchAction(driver=driver).tap(x=x,y=y).perform()
        except:
            print(f"元素未找到")
            return False


