# Perceptron Training Algorithm Implementation

import math

# Function to find dot product of vectors
def dot_product(x,w):
	return sum([a*b for a,b in zip(x,w)])

# Fucntion to check convergence reached
def check(w):
	for x in x_vector:
		if (dot_product(x,w)<=0):
			return x
	return []

n = int(input('')) # no of input lines

# Initializations
max_iterations = 1000000
x_vector = []
zero_class = []
one_class = []
temp = 1
fill = 0
w = [0]*(n+1)

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

# Taking function input
print('Enter function :')
for x in x_vector:
	temp = int(input(str(x) + ' '))
	x = [-1] + x
	if (temp==0):
		x = [-y for y in x]
		zero_class += [x]
	else:
		one_class += [x]
x_vector = zero_class + one_class

# Looping for convergence
w1 = w
w2 = w
print('\n')
for i in range(max_iterations):
	temp = check(w1)
	if (temp==[]):
		print('convergence reached for ' + str(w1) + ' in ' + str(i+1) + ' steps')
		exit(0)
	else:
		w1 = [a+b for a,b in zip(w1,temp)]
		temp = check(w2)
		if (temp==[]):
			w2 = []
		else:
			w2 = [a+b for a,b in zip(w2,temp)]
			temp = check(w2)
			if (temp==[]):
				w2 = []
			else:
				w2 = [a+b for a,b in zip(w2,temp)]
		if (w1==w2):
			print('cycle observed')
			z, w = w1, w1
			for i in range(max_iterations):
				print(w)
				temp = check(w)
				if (temp==[]):
					print('convergence reached for ' + str(w) + ' in ' + str(i+1) + ' steps')
					exit(0)
				else:
					w = [a+b for a,b in zip(w,temp)]
					if (z==w):
						print(w)
						print('cycle detected of length ' + str(i+1))
						exit(0)
			exit(0)
print("cycle didn't appear in " + str(max_iterations) + ' steps')