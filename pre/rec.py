import torch, torch.nn as nn

net = nn.Linear(4,4)
state = torch.randn(1,4)

for step in range(5):
    state = net(state)
    print(f"{step} : {state}")
