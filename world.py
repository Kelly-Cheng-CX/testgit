"""

上传

"""


class Mobile:
    me = 'CX'

    def __init__(self, color, brand, money):
        self.color = color
        self.brand = brand
        self.money = money

    def call(self, num, name):
        print(f'{Mobile.me}正在用{self.brand}手机打电话给{name},电话号码{num}')


Mobile = Mobile('紫色', '华为', '3千')
print(Mobile.call('123456789', '鹿晗'))
