# 定义类，首字母要大写
class Dog:
    # 属性
    color ="white"
    bodytype ="big"
    leg = 4
    # 方法
    def eat(self):
        print("吃狗粮")
    def cry(self):
        print("看家ing")
    def run(self):
        print("出去遛弯")

print(Dog.leg)

# 实例化
dog = Dog()
dog.run()
