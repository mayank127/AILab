import glob
import os
import matplotlib.pyplot as plt
os.chdir("./data")

plt.title("No. of iterations v/s Learnin Rate - ")
for file in glob.glob("*"):
	if(file=="plot"):
		break
	all_data = []
	print (file)
	f = open(file)
	lines = f.readlines()
	x=[]
	y=[]
	for line in lines:
		data = line.split(" ")
		all_data = [float(d) for d in data]
		x.append(all_data[0])
		y.append(all_data[1])
	plt.plot(x,y,label=file)
	plt.legend()
plt.savefig("plot/fig.png")
