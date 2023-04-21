import torchvision
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
dataset_transform=torchvision.transforms.Compose([transforms.ToTensor()])

train=torchvision.datasets.CIFAR10("./dataset",train=True,transform=dataset_transform,download=True)
set=torchvision.datasets.CIFAR10("./dataset",train=False,transform=dataset_transform,download=True)
print(train[0])

imag,target=train[0]
print(train.classes[target])
writer=SummaryWriter("imaglog")
for i in range(10):
    imag,target=train[i]
    writer.add_image("train",imag,i)

writer.close()