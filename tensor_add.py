import torch

# 这两个Tensor加减乘除会对b自动进行Broadcasting
a = torch.rand(4, 512, 8, 8)
b = torch.rand(1, 512, 8, 8)

c1 = a + b
c2 = torch.add(a, b)
print(c1.shape, c2.shape)
print(torch.all(torch.eq(c1, c2)))
