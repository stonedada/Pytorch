# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
import torchvision.transforms
from PIL.Image import Image

imge_path=""
img=Image.open(imge_path)

transform=torchvision.transforms.Compose([torchvision.transforms.Resize((32,32)),torchvision.transforms.ToTensor()])
img=transform(img)
print(img)