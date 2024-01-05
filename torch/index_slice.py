import torch

#index sama mcm list in python
c = torch.tensor([20,1,2,3,4])

c[0] = 100
c[4] = 0

# print(c)


#slice
d = c[1:4]
print(d)

c[3:5] = torch.tensor([300.0, 400.0])
print(c)
