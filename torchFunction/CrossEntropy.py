# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
import torch
predict = torch.randn((4,3))
predict = torch.nn.functional.softmax(predict,dim = 1)
target = torch.empty(4,dtype=torch.long).random_(3)
loss = torch.nn.CrossEntropyLoss()
loss_ = loss(predict,target)
print(predict)
print(target)
print(loss_)