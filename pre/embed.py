import torch, torch.nn as nn

embed = nn.Embedding(10, 4)
print(embed)
tokens = torch.tensor([[1,2,3]])
#print(tokens.shape)
vec = embed(tokens)
#print(vec)
#print(vec.shape)
