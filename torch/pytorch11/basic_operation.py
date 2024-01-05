import torch  # 1D operation

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


#dot product  # (x*x) + (y*y)
xx = torch.tensor([1,2])
yy = torch.tensor([1,2])
dotproduct = torch.dot(xx, yy)
print(dotproduct)


#adding constant to a tensor
cons = torch.tensor([1,2,3,-1])
zzz = cons + 1  #every element inside tensor cons add 1
print(zzz)