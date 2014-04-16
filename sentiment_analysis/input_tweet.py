from random import random, shuffle
import numpy

def get_feature_vector(all_words, words):
	feature_vector = [0]*len(all_words)
	j = 0
	for i in range(len(all_words)):
		# print i,j,len(words),len(all_words)
		if(all_words[i] in words):
			feature_vector[i] = 1
	return feature_vector


all_words = input()
print all_words
print len(all_words)
input_weights = [[],[],[]]
input_weights[0] = input()
input_weights[1] = input()
input_weights[2] = input()


tweet = str(input())
feature_vector = get_feature_vector(all_words, tweet)

neurons_per_layer = [len(all_words),3] # first element = number of input lines2

eta = 1
moment = 0
data_sets = [[],[],[],[],[]]
output_sets = [[],[],[],[],[]]
words_set = [[],[],[],[],[]]

# 
# training_data = input_vectors[:10]
# target_output = output_vectors[:10]

n_layers = len(neurons_per_layer) - 1
network = []
Input = [0]*neurons_per_layer[0]
# target_output = [[1,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1]]
# target_output = [[0],[1],[1],[0],[1],[0],[1],[1],[0],[1]]


Output = [0]

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
		self.output = 1/(1+numpy.exp(-1*self.output))

	def init_weights(self):
		for i in range(neurons_per_layer[self.layer-1]+1):
			self.in_weights += [(2*random()-1)]
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

i = 0
for layer in network:
	for neuron in layer:
		neuron.in_weights = input_weights[i]
		print i
		i += 1

Input = feature_vector
for layer in network:
	for neuron in layer:
		neuron.cal_output(Input)
maxVar = network[-1][0].output
for w in network[-1]:
	if(maxVar < w.output):
		maxVar = w.output
	print w.output,
ans = []
for w in network[-1]:
	if(maxVar == w.output):
		ans += [1]
	else:
		ans += [0]
print ans