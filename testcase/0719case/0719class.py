#coding=utf-8
#抽象
#定义一个类
class Person:
    def name(self,name1):
        self.name=name1

    def speak(self):
        print "%s 我是一个人"%self.name

    def song(self):
        print "%s 我会唱歌"%self.name

    def think(self):
        print "%s 我可以独立思考"%self.name

    def exercise(self):
        pass

    def fly_airport(self,name):
        print "%s fsdfk"%self.name
#静态是属性 动态是方法
x=Person()  #实例化对象 对象是属性（眼睛歪 鼻子斜 胸大无脑）
x.name='沙城'
x.song() #调用类里面的方法
x.speak()
x.think()

#类的继承  子类（父类，基类）
class Mylist(list):
    pass
a=Mylist()
a.append(1)
a.append(2)
a.append(3)
print a
a.sort()
print a
#子类的方法 如果跟父类重名的话，那么就是重写父类的方法
class Cat(Person):
    def speak(self):
        print "%s我是一只猫，喵喵"%self.name
blackcat=Cat()
blackcat.name="sunshine"
blackcat.speak()
#类的多态
class AA:
    def fun(self):
        print "我是A类"
class BB:
    def fun(self):
        print "我是B类"
aa=AA()
bb=BB()
aa.fun()
bb.fun()
#类的私有(老婆是自己的)共有（苍老师是世界的）
class C:
    name="asdf"  #定义公共的变量
c=C()
print c.name  #只要实例化，都可以使用
class D:
    _name="qqqq"  #定义私有变量
    def getname(self):   #定义方法
        print self._name
d=D()
d.getname()   #如果要使用私有变量，只能通过类的方法去调用才行
#类的魔法构造  可以直接传参
class E:
    def __init__(self,user):
        print self.name
e=E()


