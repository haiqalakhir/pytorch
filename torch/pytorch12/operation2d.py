import torch  # 2D operation

X = torch.tensor([[1,0],[0,1]])
Y = torch.tensor([[2,1],[1,2]])

print(X + Y)  # addition

print(2 * Y)  # multiply


# multiply 2 tensor of same dimension
print(X * Y)  # result is identical to Hadamard product (matrix)



# #matrix multiplication shape(2,3) x shape(3,2)
A = torch.tensor([[0,1,1],[1,0,1]])    # dlm [] biru column  # dlm [] ungu row
B = torch.tensor([[1,1],[1,1],[-1,1]])
C = torch.mm(A, B)
print(C)
