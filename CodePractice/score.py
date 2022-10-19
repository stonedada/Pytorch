# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
import os
import sys

#eg1:
# n=int(input())
#
# good=0
# excel=0
#
# for i in range(n):
#     x=int(input())
#     if x>=60:
#         good+=1
#         if x>=85:
#             excel+=1
# print("{:.0f}% \n{:.0f}%".format(good/n*100,100*excel/n))

#eg2

# n=int(input())
# a=[int(input()) for i in range(n)]
# def f(x):
#     return format(100*len([i for i in a if i>=x])/n,'.0f')+'%'
# print(f(60),f(85),sep='\n')
#

b=[i for i in range(10) if i>=5]
print(b)


ids=[0,1,2]
all_ids=[1,2,3]
id_indicator = [i in all_ids for i in ids]
print(id_indicator)