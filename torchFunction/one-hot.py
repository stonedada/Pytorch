# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
import torch
class Our_CrossEntropy(torch.nn.Module):

    def __init__(self):
        super(Our_CrossEntropy, self).__init__()

    def forward(self, x, y):
        P_i = torch.nn.functional.softmax(x, dim=1)
        y = torch.nn.functional.one_hot(y)
        loss = y * torch.log(P_i + 0.0000001)
        loss = -torch.mean(torch.sum(loss, dim=1), dim=0)
        return loss
y=torch.tensor([3,2])
y=torch.nn.functional.one_hot(y)
print(y)