# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/st onedada
import torch
from torch import nn
from torch.nn import L1Loss

input=torch.tensor([1,2,5],dtype=torch.float32)
target=torch.tensor([1,2,3],dtype=torch.float32)

input=torch.reshape(input,(1,1,1,3))
target=torch.reshape(target,(1,1,1,3))

loss=L1Loss()

result=loss(input,target)

print(result)

x=torch.tensor([[0.1,0.2,0.3]])
y=torch.tensor([1])
loss_cross=nn.CrossEntropyLoss()
result_loss=loss_cross(x,y)
print(result_loss)

