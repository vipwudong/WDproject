class Bicycle:
    def run(self,km):
        #字面量插值传递km参数
        print(f"一共骑行了{km}km")
bike = Bicycle()
bike.run(100)

class Ebicycle(Bicycle):
    pass
    # 构造方法：类里面无法传入参数，必须使用构造方法
    def __init__(self,valume):
        # 其他类里面需要引用必须要加self,
        # 实例属性，类体中，方法内，以self.变量名的方式去定义的变量
        self.valume = valume
        # 普通属性，类体内，方法内，局部变量（只在当前的方法内有用）
        # valume = valume
    def fill_charge(self,vol):
        print(f"电动车已充电{vol}度")
        print(f"充完电还有{vol + self.valume}度")

    def run(self):

        pass
        super().
# 构造函数的参数，需要在实例化类的时候传递
ebick = Ebicycle(100)
ebick.fill_charge(10)
ebick.run(1000)
    # 第二种调用父类的方法
    raise Exception()