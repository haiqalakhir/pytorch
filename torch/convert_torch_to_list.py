import torch

#convert torch to list
this_tensor = torch.tensor([0,1,2,3])
torch_to_list = this_tensor.tolist()
print(torch_to_list)


new_tensor = torch.tensor([5,2,6,1])
print(new_tensor[1])

print(new_tensor[0].item())