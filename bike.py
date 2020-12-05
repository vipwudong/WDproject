class Bicycle:
    def run(self,km):
        print(f"用脚骑行了{km}km,好累呀")
class EBicycle(Bicycle):
    def __init__(self,value):
        self.value = value
    def fil_charge(self,vol):
        print(f"电动车已充电{vol}度")
        print(f"充完点还剩{vol+self.value}度")
    def run(self,km):
        #有电的时候能骑行的公里数
        e_km = self.value*10
        print(f"电动车的最大公里数{e_km}km")
        if e_km - km <= 0:
            print(f"用电骑行了{e_km}km")
            #调用父类的方法 super()
            super().run(km - e_km)
            #普通实例化调用父类方法
            # bike = Bicycle()
            # bike.run(km - e_km)
        else:
            print(f"用电骑行了{km}km")
ebike = EBicycle(500)
ebike.run(10000)

