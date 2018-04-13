import torch
from torch.autograd import Variable
from torch improt nn
torch.nn.FUnctional as F





#forward()X

#net.cuda() initialize cuda 
#.froward(X.cuda())

#converison to and from numpy
xt = torch.from_numpy(x)

xt.numpy()


#variables have gradients. Also presumably are optimized

xv = Variable(torch.from_numpy(x).type('torch.FloatTensor'))

xt = xv.data


class myFunc(nn.Modukle):
	def forward(self, x):
		output = x ** 2
		return output

net = myFUnc()

net.forward()


lr = 1e-1

num_iteration = 100


xii = Variable(xii.data, requires_grad=True)
output = net.forward(xii)
output.backward()
xii.grad



self.fc1 = nn.Linear(num_input, hiddenout)
self.fc2 = n
x = F.relu(self.fc1(x))


loss_fn = nn.MSELoss()

optimizer = torch.optim.Adam(net.paramerrs(),lr=leanring_rate)


#NO. The way this guy is doing this can't be right.
#loss.backward 
# optimizer.step()
#THAT CANT BE








