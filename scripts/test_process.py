"封装class"
import time
from page.goods_choicepage import GoodsChoicePage
from page.housepage import HousePage
import pytest
from page.cartpage import CartPage
from page.paymentpage import PaymentPage
from common.op_db import OperateDB

class TestLogin:

    def test_process_case01(self,driver1):
        house=HousePage(driver1)
        house.personal_click()
        house.login_click()
        house.username_input("tianchuntian")
        house.password_input("123456")
        house.sign_click()
        house.house_click()
        #清空购物车
        op=OperateDB()
        op.clear_cart()
        #清空订单
        op.clear_order()

        #选择商品
        goods=GoodsChoicePage(driver=driver1)
        goods.mobile_click()
        goods.cheng_click()
        goods.add_cart()
        goods.car_click()

        #点击购物车结算
        cart=CartPage(driver1)
        cart.pay_click()

        #订单页面
        pay=PaymentPage(driver1)
        pay.pay_method_click()
        pay.send_method_click()
        pay.order_click()
        pay.confirm_click()
        pay.zhifubao_click()

        #从购物车中读取订单
        num=op.select_order()
        assert num==1

if __name__ == '__main__':
    pytest.main()

