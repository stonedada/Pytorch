# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada


# 1、子类不重写init，继承父类init
#
# 2、子类重写init， 不继承父类init
#
# 3、子类重写init，同时继承父类init(super关键字)

class Father(object):
    def __init__(self,name):
        self.name=name
        print("name: {}".format(self.name) )

    def Get_Name(self):
        return  'Father' +self.name

# 情况一：（子类不重写init,继承父类init）
class Son_1(Father):
    def get_name(self):
        return 'Son_1 '+self.name

#情况二：（子类重写init， 不继承父类init）
class Son_2(Father):
    def __init__(self,name):
        self.name=name
        print("hi")
    def get_name(self):
        return 'Son_2 ' + self.name

#情况三：（子类重写init，同时继承父类init(super关键字)）
class Son_3(Father):
    def __init__(self,name):
        #super(Son_3, self).__init__(name)
        Father.__init__(self,name)
        print("hi")
        self.name=name
    def get_name(self):
        return "Son_3 "+self.name
if __name__=='__main__':

    son1=Son_1('I am here')
    print(son1.get_name())
    son2=Son_2('I am here')
    print(son2.get_name())
    son3=Son_3('I am here')
    print(son3.get_name())



