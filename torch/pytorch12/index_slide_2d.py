import torch

a = torch.tensor([[11, 12, 13], [21, 22, 23], [31, 32, 33]])

print(a[1][2])
print(a[0][0])
print(a[0,0:2])  #exlusive 2    # ambik index 0 and 1 shj

print(a[1:3,2])
