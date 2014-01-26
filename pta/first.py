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

for x in x_vector:
	temp = sum(x)
	if (temp>=3):
		print(1)
	else:
		print(0)