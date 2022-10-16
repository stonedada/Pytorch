# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
import torchvision
from torch import nn
from torch.nn import Sequential, Conv2d, MaxPool2d, Flatten, Linear, CrossEntropyLoss
from torch.utils.data import DataLoader

dataset=torchvision.datasets.CIFAR10(root="../dataset",train=False,transform=torchvision.transforms.ToTensor(),download=False)
dataloader=DataLoader(dataset,batch_size=64)



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
            #Linear(64,64),
            Linear(32,10)
        )

    def forward(self,x):
        x=self.module1(x)
        return  x


mymodule =Mymodule()
loss_Cross=CrossEntropyLoss()
for data in dataloader:
    imgs,target=data
    print(imgs.shape)
    print(target.shape)
    output=mymodule(imgs)
    loss=loss_Cross(output,target)
    print(loss)



