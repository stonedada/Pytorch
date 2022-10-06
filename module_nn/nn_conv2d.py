# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada

import torch
import torchvision
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset=torchvision.datasets.CIFAR10(root="../dataset",train=False,transform=torchvision.transforms.ToTensor(),download=False)
dataloader=DataLoader(dataset,batch_size=64)

class Test(nn.Module):
    def __init__(self):
        super(Test, self).__init__()
        self.conv1=nn.Conv2d(in_channels=3,out_channels=6,kernel_size=3,stride=1,padding=0)

    def forward(self,x):
        x=self.conv1(x)
        return x

test=Test()
writer=SummaryWriter(log_dir="../nnlog")
step=0
for  data in dataloader:
    imgs,target=data
    print(imgs.shape)
    output=test(imgs)
    output=torch.reshape(output,(-1,3,30,30))
    print(output.shape)
    writer.add_images("output",output,step)
    step+=0


writer.close()
