# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
import  torch
import torchvision.datasets
from torch import nn
from torch.nn import MaxPool2d
from torch.utils.data import DataLoader

# input=torch.tensor([[1,2,0,3,1],
#                     [0,1,2,3,1],
#                     [1,2,1,0,0],
#                     [5,2,3,1,1],
#                     [2,1,0,1,1]])
# input=torch.reshape(input,(-1,1,5,5))
# print(input.dtype)
# print(torch.get_default_dtype())
# print(input.shape)
from torch.utils.tensorboard import SummaryWriter

dataset=torchvision.datasets.CIFAR10(root="../dataset",train=False,transform=torchvision.transforms.ToTensor(),download=False)
dataloader=DataLoader(dataset,batch_size=64)

writer=SummaryWriter(log_dir="../maxpoolog")
class Test(nn.Module):
    def __init__(self):
        super(Test, self).__init__()
        self.maxpool1=MaxPool2d(kernel_size=3,ceil_mode=True)

    def forward(self,x):
        x=self.maxpool1(x)
        return  x

test=Test()
step=0
for  data  in  dataloader:
    imgs,target=data
    output=test(imgs)
    writer.add_images("maxpool",output,step)
    step+=1
writer.close()