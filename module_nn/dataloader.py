import torchvision
import  torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter


if __name__ == '__main__':
    test_data = torchvision.datasets.CIFAR10("./dataset", train=False, transform=torchvision.transforms.ToTensor())
    test_loader = DataLoader(dataset=test_data, batch_size=8, shuffle=True, num_workers=4, drop_last=False)
    img, target = test_data[0]
    print(img.shape)
    print(target)

    writer=SummaryWriter("dataloaderlog")
    step = 0
    for data in test_loader:
        imgs,targets = data
        pic=imgs.resize(24,32,32)
        print(pic.shape)
        print(targets)
        # for i in range(len(imgs)):
        #writer.add_image("test_data",imgs[i],step)
        writer.add_images("test_data", imgs, step)
        step += 1
    writer.close()
    print('end')
