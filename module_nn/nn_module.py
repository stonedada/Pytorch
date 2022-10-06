# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
from torch import  nn
import  torch

class Test(nn.Module):
    def __init__(self):
        super(Test,self).__init__()


    def forward(self,input):
        output=input+1
        return  output
test=Test()
x=torch.tensor([1.0,2.0,3.0],device='cuda')

print(":{:.3f}".format(x.data))

output=test(x)

print(output)


