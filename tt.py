import torch

a = torch.tensor([1., 2., 3.], requires_grad=True)
b = torch.tensor([1., 2., 3.], requires_grad=True)

c = a+b
print(c)
c.backward()
print(a.grad)
