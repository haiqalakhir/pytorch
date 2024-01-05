import torch
import numpy as np
import matplotlib.pyplot as plt

#universal functions
a = torch.tensor([1,-1,1,-1], dtype=torch.float32) # tell python the datatype
mean_a = a.mean()  # The mean function typically works with floating-point or complex data types.
print(mean_a)


b = torch.tensor([1,-2,3,4,5])
max_b = b.max()
print(max_b)


# dlm slide xkena round off pon
np.pi
x = torch.tensor([0, np.pi/2, np.pi], dtype=torch.int16)
y = torch.sin(x)
ronse = torch.round(y)
print(ronse)




xuz = torch.linspace(0, 2*np.pi, 100)
yuz = torch.sin(xuz)
print(yuz)

# %matplotlib inline  # ni guna utk jupyter notebook ja
plt.plot(xuz.numpy(), yuz.numpy())
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Wave')
plt.grid(True)
plt.show()