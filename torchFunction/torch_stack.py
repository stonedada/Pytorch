import torch

a = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = torch.tensor([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
c = torch.stack([a, b], 0)
d=torch.stack([a,b],1)
print(a,a.shape)
print(b,b.shape)
print(c,c.shape)
print(d,d.shape)

# # 输出信息：
# tensor([[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]])
# tensor([[11, 22, 33],
#         [44, 55, 66],
#         [77, 88, 99]])
# tensor([[[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]],
#
#         [[11, 22, 33],
#          [44, 55, 66],
#          [77, 88, 99]]])