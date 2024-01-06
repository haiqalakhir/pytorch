import torch

u = torch.tensor(1.0,requires_grad=True)
v = torch.tensor(2.0,requires_grad=True)

f = u**v + u ** 2

jon = f.backward()

print(u.grad)

