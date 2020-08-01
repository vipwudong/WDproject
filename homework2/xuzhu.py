"""
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
"""
from homework2.TongLao import TongLao
# 定义XuZhu类，继承童姥
class XuZhu(TongLao):
    def read(self):
        print("罪过罪过")
# 实例化
Xz = XuZhu(3000,1500)
Xz.read()

