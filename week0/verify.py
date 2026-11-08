import torch

x = torch.randn(2, 3)         
w = torch.randn(3, 4)         
y = x @ w                     
print("x.shape     =", x.shape)
print("w.shape     =", w.shape)
print("(x@w).shape =", y.shape)
print("torch       =", torch.__version__)
print("cuda        =", torch.cuda.is_available())