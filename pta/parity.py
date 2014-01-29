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
for x in x_vector:
	temp = sum(x)
	st = ''
	if (temp%2==0):
		for s in x:
			st += (str(s) + ' ')
		st += str(1)
	else:
		for s in x:
			st += (str(s) + ' ')
		st += str(0)
	print(st)
