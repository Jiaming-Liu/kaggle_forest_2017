import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import numpy as np
from   torch.autograd import Variable


# Linear  Model
class simple_net(nn.Module):
    def __init__(self, input_size, output_size):
        super(simple_net, self).__init__()
        self.linear = nn.Linear(input_size, output_size)

    def forward(self, x):
        out = self.linear(x)
        return out



# Toy Dataset
x_train = np.array([[3.3], [4.4], [5.5], [6.71], [6.93], [4.168],
                    [9.779], [6.182], [7.59], [2.167], [7.042],
                    [10.791], [5.313], [7.997], [3.1]], dtype=np.float32)

y_train = np.array([[1.7], [2.76], [2.09], [3.19], [1.694], [1.573],
                    [3.366], [2.596], [2.53], [1.221], [2.827],
                    [3.465], [1.65], [2.904], [1.3]], dtype=np.float32)


#####################################################################
input_size  = 1
output_size = 1
net = simple_net(input_size, output_size)

# Loss and Optimizer
mse = nn.MSELoss()
optimizer = torch.optim.SGD(net.parameters(),lr=0.001)




# Train the Model
num_epochs = 100
for epoch in range(num_epochs):

    inputs  = Variable(torch.from_numpy(x_train))
    targets = Variable(torch.from_numpy(y_train))

    outputs = net(inputs)

    optimizer.zero_grad()
    loss = mse(outputs, targets)
    loss.backward()
    optimizer.step()

    print ('Epoch [%d/%d], Loss: %.4f' %(epoch+1, num_epochs, loss.data[0]))


# Plot the graph
inputs  = Variable(torch.from_numpy(x_train))
predicted = net(inputs).data.numpy()

plt.plot(x_train, y_train, 'ro', label='Original data')
plt.plot(x_train, predicted, label='Fitted line')
plt.legend()
plt.show()