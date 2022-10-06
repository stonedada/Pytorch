# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
import torch
import torchvision
from torch import nn
from torch.nn import Linear
from torch.utils.data import DataLoader

dataset=torchvision.datasets.CIFAR10(root="../dataset",train=False,transform=torchvision.transforms.ToTensor(),download=False)
dataloader=DataLoader(dataset,batch_size=64)


class Test(nn.Module):
    def __init__(self):
        super(Test, self).__init__()
        self.linear1=Linear(196608,10)


    def forward(self,x):
        x=self.linear1(x)
        return  x

test=Test()

for data  in dataloader:
    imgs,target=data
    imgs=torch.reshape(imgs,(1,1,1,-1))
    print(imgs.shape)
    input=torch.flatten(imgs)
    print(input.shape)
    output=test(input)
    print(output.shape)
