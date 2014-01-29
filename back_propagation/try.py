from random import *
print('2 5 1')
print(0.5)
print(0.1)
for i in range(10):
	x = int(random()*100)
	flag = random()
	if (flag<=0.5):
		print(str(x) + ' ' + str(x+1) + ' 1')
	else:
		if (flag>=0.75):
			print(str(x) + ' ' + str(int(x + randint(2,100))) + ' 0')
		else:
			print(str(x) + ' ' + str(int(x - randint(0,100))) + ' 0')