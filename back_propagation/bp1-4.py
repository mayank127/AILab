from random import random
import math
import sys
# neurons_per_layer = [0]*n_layers
if(len(sys.argv)<2):
	print "usage " + sys.argv[0] + " filename"
	exit(0)
filename = sys.argv[1]
fin = open(filename)
lines = fin.readlines()
neurons_per_layer = [int(x) for x in lines[0].replace('\n','').split(' ')] # first element = number of input lines

eta = float(lines[1])
moment = float(lines[2])
training_data = []
target_output = []
for i in range(3,len(lines)):
	l = [float(x) for x in lines[i].replace('\n','').split(' ')]
	training_data += [l[0:neurons_per_layer[0]]]
	target_output += [l[neurons_per_layer[0]:]]

n_layers = len(neurons_per_layer) - 1
network = []
Input = [0]*neurons_per_layer[0]
# target_output = [[1,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1]]
# target_output = [[0],[1],[1],[0],[1],[0],[1],[1],[0],[1]]


Output = [0]
# eta = 0.1 # learning rate
# moment = 0.1

data_sets = [[],[],[],[],[]]
output_sets = [[],[],[],[],[]]
for i in range(5):
	data_sets[i] = training_data[int(len(training_data)*0.2*i):int(len(training_data)*0.2*(i+1))]
	output_sets[i] = target_output[int(len(training_data)*0.2*i):int(len(training_data)*0.2*(i+1))]

class Neuron:

	def __init__(self,temp=-1, index=-1):
		self.layer = temp
		self.index = index
		self.in_weights = []
		self.delta = 0
		self.output = 0
		self.moment_weights = []
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
			self.in_weights += [(3*random()-1)]
			self.moment_weights += [0]

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
		change = self.delta * -1
		self.in_weights[0] += (eta * change) + self.moment_weights[0] * moment
		self.moment_weights[0] = change
		if (self.layer==1):
			for i in range(neurons_per_layer[0]):
				change = self.delta * Input[i]
				self.in_weights[i+1] += (eta * change) + self.moment_weights[i+1] * moment
				self.moment_weights[i+1] = change
		else:
			for i in range(neurons_per_layer[self.layer-1]):
				change = self.delta * network[self.layer-2][i].output
				self.in_weights[i+1] += (eta * change) + self.moment_weights[i+1] * moment
				self.moment_weights[i+1] = change

for l in range(n_layers):
	layers = []
	for i in range(neurons_per_layer[l+1]):
		temp = Neuron(l+1, i)
		layers += [temp]
	network += [layers]

# Generating truth table
# n = neurons_per_layer[0]
# x_vector = []
# fill = 0
# temp = 1

# for i in range(pow(2,n)):
# 	x_vector.append([])
# for i in range(n):
# 	count = 0
# 	for j in range(pow(2,n)):
# 		x_vector[j] = [fill] + x_vector[j]
# 		count += 1
# 		if (count==temp):
# 			count = 0
# 			if (fill==0):
# 				fill = 1
# 			else:
# 				fill = 0
# 	temp *= 2
# test_vector = x_vector
# training_data = [[]]
# training_data = [[0,0],[0,1],[1,0],[1,1]]
# training_data = [[3,5],[2,3],[9,10],[12,15],[2.5,3.5],[-9,15],[100,101],[-1,0],[70,95],[-50,-49]]
# training_data[0] = [0,1,1,1,1,1,1]
# training_data[1] = [0,0,0,1,1,0,0]
# training_data[2] = [1,0,1,1,0,1,1]
# training_data[3] = [1,0,1,1,1,1,0]
# training_data[4] = [1,1,0,1,1,0,0]
# training_data[5] = [1,1,1,0,1,1,0]
# training_data[6] = [1,1,1,0,1,1,1]
# training_data[7] = [0,0,1,1,1,0,0]
# training_data[8] = [1,1,1,1,1,1,1]
# training_data[9] = [1,1,1,1,1,1,0]

for dataI in range(5):
	network = []
	training_data = []
	target_output = []
	for i in range(5):
		if not (i==dataI):
			training_data += data_sets[i]
			target_output += output_sets[i]

	for l in range(n_layers):
		layers = []
		for i in range(neurons_per_layer[l+1]):
			temp = Neuron(l+1, i)
			layers += [temp]
		network += [layers]
	x_vector = training_data
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

	def get_output(x_vector, out_vector):
		truecount = 0
		falsecount = 0
		for i in range(len(x_vector)):
			Input = x_vector[i]
			Output = out_vector[i]
			for layer in network:
				for neuron in layer:
					neuron.cal_output(Input)
			print (Input),
			maxVar = network[-1][0].output
			for w in network[-1]:
				if(maxVar < w.output):
					maxVar = w.output
			ans = []
			for w in network[-1]:
				if(maxVar == w.output):
					ans += [1]
				else:
					ans += [0]
			print ans,
			print Output,
			print (ans == Output)
			print('\n')
			print (ans == Output)
			if(ans==Output):
				truecount += 1
			else:
				falsecount += 1
			print('\n')
		return [truecount, falsecount]

	factor = 0;

	cur_error = get_error()
	threshhold = 1 #0.02 * neurons_per_layer[-1]
	count = 0
	iterations=0;
	while True:
		iterations+=1
		if (cur_error < threshhold):
			break
		if(count==100):
			count = 0
			factor += 1
			print (cur_error)
		count+=1

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
		temp = cur_error
		cur_error = get_error()
		# temp -= cur_error
		# if (temp>=0.1):
		# 	eta/=2
		# elif (temp<=0.001):
		# 	eta*=2
		# 	if(eta>1): eta/=2
		# else:
		# 	pass
	test_vector = data_sets[dataI]
	test_output = output_sets[dataI]
	print(cur_error)
	truecount,falsecount = get_output(test_vector, test_output)
	print("true", truecount)
	print("false", falsecount)
	print(iterations)