import torch

# a = torch.tensor([0.0,1.0,2.0,3.0,4.0])
# print(a.dtype)

# print(a.type())



# #FloatTensor
# ar = torch.FloatTensor([0,1,2,3,4])
# print(ar.type())
# print(ar)

are = torch.Tensor([0,1,2,3,4,5])
are_col = are.view(-1,1)
print(are_col)