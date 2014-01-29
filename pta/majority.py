import math

n = int(input('')) # no of input lines

# Taking function input

x_vector = []
max_iterations = 10000
for i in range(pow(2,n)):
	x_vector.append([])

temp = 1
fill = 0
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

print(n)

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
for x in x_vector:
	ans = [0]*10
	if x in training_data:
		ans[training_data.index(x)] = 1
	for a in x:
		print str(a) + " ",
	for a in ans:
		print str(a) + " ",
	print " "