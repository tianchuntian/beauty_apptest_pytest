
"封装操作数据库的方法"
import pymysql

class OperateDB:

    def __init__(self, host='ecshop.itsoso.cn', user='ecshop', password='ecshop', db='ecshop', port=3306, charset='utf8'):
        self.cn=pymysql.connect(
             host=host,
             port=port,
             password=password,
             user=user,
             db=db,
             charset=charset
         )
        self.cursor=self.cn.cursor(cursor=pymysql.cursors.SSDictCursor)

    def clear_cart(self):
        "清除用户的购物车"
        sql="delete from ecs_cart where user_id=10390"

        self.cursor.execute(sql)

    # 18446744073709551615

    def select_order(self):
        '查询订单在不在数据库'
        sql="select * from ecs_order_info where user_id=10390"
        self.cursor.execute(sql)
        data= self.cursor.fetchall()
        num=len(data)
        return num


    def clear_order(self):
        sql='delete from ecs_order_info where user_id=10390'
        self.cursor.execute(sql)



if __name__ == '__main__':
    op = OperateDB()
    num = op.select_order()
    print(num)