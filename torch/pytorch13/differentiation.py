import torch

x = torch.tensor(2.0,requires_grad=True)
y = x**2

jo = y.backward()

print(x.grad)  # dy/dx(x=2) = x^2


xx = torch.tensor(2.0,requires_grad=True)
zz = xx**2+2*xx+1
jon = zz.backward()
print(xx.grad)