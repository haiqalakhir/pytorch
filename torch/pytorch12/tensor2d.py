import torch

a = [[11,12,13],[21,22,23],[31,32,33]]

are = torch.tensor(a)
print(are)

print(are.ndimension())

print(are.shape)    # to get size ->  torch.Size(3,3)

print(are.size())   # to get shape -> (3,3)

print(are.numel())  # number of element in tensor