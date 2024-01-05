import torch

#addition vector
u = torch.tensor([1.0,0.0])
v = torch.tensor([0.0,1.0])

zwer = u + v
print(zwer)


#vector multiplication
y = torch.tensor([1,2])
z = 2 * y
print(z)


#product of 2 vector
uu = torch.tensor([1,2])
vv = torch.tensor([3,2])
print(uu * vv)
