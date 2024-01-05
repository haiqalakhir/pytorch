import torch
import numpy as np

#convert torch to numpy
numpy_array = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
torch_tensor = torch.from_numpy(numpy_array)
print(torch_tensor)
back_to_numpy = torch_tensor.numpy()
print(back_to_numpy)


# #convert torch to list
# this_tensor = torch.tensor([0,1,2,3])
# torch_to_list = this_tensor.tolist()
# print(torch_to_list)


# new_tensor = torch.tensor([5,2,6,1])
# print(new_tensor[1])

# print(new_tensor[0].item())