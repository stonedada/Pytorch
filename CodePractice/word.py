# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
from collections import defaultdict, Counter

dict={}
dict=defaultdict(int)
word=input()

for a in word:
    #eg1:
    # if a in dict.keys():
    #     dict[a]+=1
    # else:
    #     dict[a]=1
    #eg2
    # dict[a]+=1
    #eg3:
    dict[a]=dict.get(a,0)+1
#eg4:
# li=[]
# for i ,a in enumerate(word):
#     li.append(a)
# dict = Counter(li)
# print("{}\n{}".format(list(dict.keys())[0],list(dict.values())[0]))


#eg1:
l=sorted(dict.items(),key=lambda x: x[1])
print(l[-1][0])
print(l[-1][1])
#eg2:
# key,value=max(dict.items(),key=lambda x: x[1])
# print("{}\n{}".format(key,value))

