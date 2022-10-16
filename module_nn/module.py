# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
import torch.nn
from torch import nn
from torch.nn import *

class Mymodule(nn.Module):
    def __init__(self):
        super(Mymodule, self).__init__()
        self.module1=Sequential(
            Conv2d(3,32,kernel_size=5,padding=2),
            MaxPool2d(kernel_size=2),
            Conv2d(in_channels=32,out_channels=32,kernel_size=5,padding=2),
            MaxPool2d(kernel_size=2),
            Conv2d(32,64,5,2),
            MaxPool2d(2),
            Flatten(),
            Linear(64,64),
            Linear(64,10),
            # torch.nn.Softmax(dim=0)
        )

    def forward(self,x):
        x=self.module1(x)
        return  x