from common.base import Base
import time

class PaymentPage(Base):
    def __init__(self,driver):
        self.driver=driver

    "定位器"
    pay_method_loc=("id","com.insthub.ecmobile:id/balance_pay_type")
    send_method_loc=("id","com.insthub.ecmobile:id/balance_dis_type")
    zhifubao_loc=("xpath","//*[@text='支付宝']")
    shentong_loc=("xpath","//*[@text='申通快递']")
    commit_order_loc = ("id", "com.insthub.ecmobile:id/balance_submit")
    confirm_loc=("id","com.insthub.ecmobile:id/yes")
    zhifubao_pay_loc=("id","com.insthub.ecmobile:id/alipay")

    def pay_method_click(self):
        "点击支付方式"
        self.element_click(self.driver,self.pay_method_loc)
        time.sleep(1)
        self.element_click(self.driver,self.zhifubao_loc)
        time.sleep(1)

    def send_method_click(self):
        "点击配送方式"
        self.element_click(self.driver,self.send_method_loc)
        time.sleep(1)
        self.element_click(self.driver,self.shentong_loc)
        time.sleep(1)

    def order_click(self):
        "点击提交订单按钮"
        self.element_click(self.driver,self.commit_order_loc)
        time.sleep(1)

    def confirm_click(self):
        "点击弹窗的确定按钮"
        self.element_click(self.driver,self.confirm_loc)
        time.sleep(1)

    def zhifubao_click(self):
        "点击支付宝支付"
        self.element_click(self.driver,self.zhifubao_pay_loc)
        time.sleep(1)
