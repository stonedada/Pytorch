# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
import torchvision.datasets
from torch import nn
from torch.nn import ReLU, Sigmoid
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset=torchvision.datasets.CIFAR10(root="../dataset",train=False,transform=torchvision.transforms.ToTensor(),download=False)
dataloader=DataLoader(dataset,batch_size=64)


class Test(nn.Module):
    def __init__(self):
        super(Test, self).__init__()
        self.relu1=ReLU()
        self.sigmod=Sigmoid()


    def forward(self,x):
        x=self.sigmod(x)
        return  x


test=Test()
writer=SummaryWriter("../relu_log")
step=0
for data in dataloader:
    imgs,target=data
    writer.add_images("imgs",imgs,step)
    output=test(imgs)
    writer.add_images("output",output,global_step=step)
    step+=1

writer.close()

