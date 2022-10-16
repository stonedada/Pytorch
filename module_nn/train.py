# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
import torch
import torchvision
from torch import optim
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

from  module import *

#device=torch.device("cuda")
#准备数据集
train_dataset=torchvision.datasets.CIFAR10(root="../dataset",train=True,transform=torchvision.transforms.ToTensor(),download=True)
test_dataset=torchvision.datasets.CIFAR10(root="../dataset",train=False,transform=torchvision.transforms.ToTensor(),download=True)

train_dataloader=DataLoader(train_dataset,batch_size=1,drop_last=False)
teset_dataloader=DataLoader(test_dataset,batch_size=1,drop_last=False)

train_size=len(train_dataloader)
test_size=len(test_dataset)
print("训练集长度{}".format(train_size))
print("测试集长度{}".format(test_size))

#加载模型
device=torch.device("cuda:0")
torch.backends.cudnn.benchmark = False
#cuda版本查询
print(torch.version.cuda)
#cudnn版本查询
print(torch.backends.cudnn.version())
#设备名
print(torch.cuda.get_device_name(0))

module=Mymodule()
if torch.cuda.is_available():
    module.to(device)

#设置网络参数
epoch=5
train_step=0
test_step=0

#损失函数
#cross_loss=nn.CrossEntropyLoss()
#cross_loss=cross_loss.cuda()
cross_loss=nn.CrossEntropyLoss()
cross_loss.to(device)

#优化器
learning_rate=1e-2
optimizer=optim.SGD(module.parameters(),learning_rate)
writer=SummaryWriter("../logs")
for i in  range(epoch):
    #训练开始
    print("----------开始第{}轮训练------------".format(i+1))
    module.train()
    for data in train_dataloader:
        imgs,target=data
        imgs=imgs.to(device)
        target=target.to(device)
        output=module(imgs)
        loss=cross_loss(output,target)
        #loss.requires_grad_(True)
        #优化器优化模型
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        train_step += 1
        if train_step%100==0:
            print("第{}次训练，loss={}".format(train_step,loss))
            writer.add_scalar("train_loss",loss.item(),train_step)

    #测试开始
    module.eval()
    total_loss=0
    total_accuracy=0
    with torch.no_grad():
        for data in teset_dataloader:
            imgs,target=data
            # imgs = imgs.cuda()
            # target = target.cuda()
            imgs=imgs.to(device)
            target=target.to(device)
            output=module(imgs)
            loss=cross_loss(output,target)
            total_loss+=loss.item()
            accuracy=(output.argmax(1)==target).sum()
            total_accuracy+=accuracy

    print("整体测试集上的loss:{}".format(total_loss))
    print("整体正确率{}".format(total_accuracy))
    writer.add_scalar("test_loss",total_loss,test_step)
    writer.add_scalar("test_accuracy", total_accuracy/test_size, test_step)
    test_step+=1

    torch.save(module,"module_{}.pth".format(i))
    #torch.save(module.state_dict(),"module_{}.pth".format(i))
    print("模型已保存")

writer.close()

