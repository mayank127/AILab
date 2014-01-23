from random import random
import math

n_layers = 2
# neurons_per_layer = [0]*n_layers
neurons_per_layer = [2,2,1] # first element = number of input lines
network = []
Input = [0]*neurons_per_layer[0]
target_output = [[0],[1],[1],[0]]
Output = [0]
eta = 0.01 # learning rate

class Neuron:

	def __init__(self,temp=-1, index=-1):
		self.layer = temp
		self.index = index
		self.in_weights = []
		self.delta = 0
		self.output = 0
		self.init_weights()

	def cal_output(self, Input):
		self.output = 0
		self.output += self.in_weights[0]*-1
		if (self.layer==1):
			for i in range(neurons_per_layer[0]):
				self.output += self.in_weights[i+1]*Input[i]
		else:
			for i in range(neurons_per_layer[self.layer-1]):
				self.output += self.in_weights[i+1]*network[self.layer-2][i].output
		self.output = 1/(1+math.exp(-1*self.output))

	def init_weights(self):
		for i in range(neurons_per_layer[self.layer-1]+1):
			self.in_weights += [(2*random()-1)]

	def cal_delta(self, Output):
		oj = self.output
		if (self.layer==n_layers):
			self.delta = (Output[self.index]-oj)*oj*(1-oj)		#Outer Layer delta = (tj-oj)oj(1-oj)
		else:
			self.delta = 0
			for n in network[self.layer]:
				self.delta += n.in_weights[self.index+1]*n.delta 		#Hidden Layer = sigma Wkj*deltak * oj(1-oj)
			self.delta *= oj*(1-oj)

	def update_weight(self, Input):
		self.in_weights[0] += (eta * self.delta * -1)
		if (self.layer==1):
			for i in range(neurons_per_layer[0]):
				self.in_weights[i+1] += (eta * self.delta * Input[i])
		else:
			for i in range(neurons_per_layer[self.layer-1]):
				self.in_weights[i+1] += (eta * self.delta * network[self.layer-2][i].output)

for l in range(n_layers):
	layers = []
	for i in range(neurons_per_layer[l+1]):
		temp = Neuron(l+1, i)
		layers += [temp]
	network += [layers]

# Generating truth table
n = neurons_per_layer[0]
x_vector = []
fill = 0
temp = 1

for i in range(pow(2,n)):
	x_vector.append([])
for i in range(n):
	count = 0
	for j in range(pow(2,n)):
		x_vector[j] = [fill] + x_vector[j]
		count += 1
		if (count==temp):
			count = 0
			if (fill==0):
				fill = 1
			else:
				fill = 0
	temp *= 2

def update_neurons():
	for x in x_vector:
		Input = x
		Output = target_output[x_vector.index(x)]
		for layer in network:
			for neuron in layer:
				neuron.cal_output(Input)
		for layer in reversed(network):
			for neuron in layer:
				neuron.cal_delta(Output)
		for layer in network:
			for neuron in layer:
				neuron.update_weight(Input)

def get_error():
	error = 0
	for x in x_vector:
		Input = x
		Output = target_output[x_vector.index(x)]
		for layer in network:
			for neuron in layer:
				neuron.cal_output(Input)
		error += sum([(x-y.output)*(x-y.output) for x,y in zip(Output,network[-1])])
	return error*0.5

def get_output():
	for x in x_vector:
		Input = x
		Output = target_output[x_vector.index(x)]
		for layer in network:
			for neuron in layer:
				neuron.cal_output(Input)
		print (Input, [w.output for w in network[-1]], Output)
	print('')
	print(get_error())

cur_error = get_error()
threshhold = 0.005
while True:
	if (cur_error < threshhold):
		break
	# print(cur_error)
	# print(prev_error)
	# for layer in network:
	# 	for neuron in layer:
	# 		print(neuron.in_weights)
	# 		print('')
	# 		print(neuron.layer,neuron.index)
	# 		print('')
	# print('\n')
	update_neurons()
	# for layer in network:
	# 	for neuron in layer:
	# 		print(neuron.in_weights)
	cur_error = get_error()

print(cur_error)
get_output()