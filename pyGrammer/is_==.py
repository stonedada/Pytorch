# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
#字符串的比较操作
#运算符>,>=,<,<=,==,!=
#比较规则首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符，一次比较下去
#直到两个字符串中的字符不相等时，其比较结果就是两个字符串的比较结果，后续字符将不再被比较
#比较原理：两字符进行比较时，比较的是其ordinal value（原始值）,调用内置函数ord可以
#得到指定字符的ordinal value。
#与内置函数ord对应的是内置函数chr，调用内置函数chr时指定ordinal value可以得到其对应的字符
###############################################################################
print('apple'>'app')#True
print('apple'>'banana')#False，97>98吗
print(ord('a'),ord('b'))#97 98
print(chr(97),chr(98))#a b
print(ord('周'))#21608
'''==与is的区别'''
'''== 比较的是value'''
'''is 比较的是id是否相等'''
a=b='python'
c='python'
print(a==b)
print(b==c)
print(id(a),id(b),id(c))#字符串的驻留机制
print(a is b)#a b的内存地址相等吗。
print(a is c)