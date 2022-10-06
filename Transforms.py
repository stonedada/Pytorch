from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
img_path="dataset/0000_color.png"
img=Image.open(img_path)
writer=SummaryWriter("logs")

#ToTensor
tensor_tran=transforms.ToTensor()  #先实例化一个对象
tensor_img=tensor_tran(img)     #然后调用__call__(self, pic)
writer.add_image("tensor_img",tensor_img)

#Normalize
tensor_norm=transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
print(tensor_img[0][0][0])
norm_img=tensor_norm(tensor_img)
writer.add_image("norm",norm_img)
print(norm_img[0][0][0])


#Resize
print(img.size)
size_tran=transforms.Resize((800,600))
Resize_img=size_tran(img)
Resize_img=tensor_tran(Resize_img)
writer.add_image("Resize",Resize_img,0)
print(Resize_img)

#Reszie2 & compose
size2_tran=transforms.Resize(512)
compose_tran=transforms.Compose([size2_tran,tensor_tran])
compose_img=compose_tran(img)
writer.add_image("Resize",compose_img,1)
writer.close()