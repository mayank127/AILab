# Seven segment display using PTA

import math

# Function to find dot product of vectors
def dot_product(x,w):
	return sum([a*b for a,b in zip(x,w)])

# Fucntion to check convergence reached
def check(truth_table,w):
	for x in truth_table:
		if (dot_product(x,w)<=0):
			return x
	return []

# Initializations
max_iterations = 1000000
x_vector = []
zero_class = []
one_class = []
temp = 1
fill = 0
w = [0]*(7+1)

n = 7

# Generating truth table
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

# Training data
training_data = [[]]*10
training_data[0] = [0,1,1,1,1,1,1]
training_data[1] = [0,0,0,1,1,0,0]
training_data[2] = [1,0,1,1,0,1,1]
training_data[3] = [1,0,1,1,1,1,0]
training_data[4] = [1,1,0,1,1,0,0]
training_data[5] = [1,1,1,0,1,1,0]
training_data[6] = [1,1,1,0,1,1,1]
training_data[7] = [0,0,1,1,1,0,0]
training_data[8] = [1,1,1,1,1,1,1]
training_data[9] = [1,1,1,1,1,1,0]

def getWeights(digit):
	truth_table = []
	for x in x_vector:
		if (training_data[digit]==x):
			x = [-1] + x
			truth_table += [x]
		else:
			x = [-1] + x
			x = [-y for y in x]
			truth_table += [x]
	w = [0,0,0,0,0,0,0,0]	
	# Looping for convergence
	while True:
		temp = check(truth_table,w)
		if (temp==[]):
			return w
		else:
			w = [a+b for a,b in zip(w,temp)]

def init():
	weights = []
	for i in range(10):
		w = getWeights(i)
		weights += [w]
	return weights

def main():
	weights = init()
	input_sequence = raw_input('Give input sequence : ')
	if (len(input_sequence)!=7):
		return 'Error : Invalid input length'
	input_sequence = list(input_sequence)
	input_sequence = [int(y) for y in input_sequence]
	input_sequence = [-1] + input_sequence
	for w in weights:
		if (dot_product(w,input_sequence)>0):
			return weights.index(w)

print(main())
