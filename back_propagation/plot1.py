import glob
import os
import matplotlib.pyplot as plt
os.chdir("./data1")

for file in glob.glob("*"):
	all_data = []
	print (file)
	f = open(file)
	lines = f.readlines()
	for line in lines:
		data = line.split(",")
		all_data += [[float(d) for d in data]]
	eta = 0.1
	x = []
	y = []
	plt.xlabel("Iteration Number")
	plt.ylabel("Error (TSS)")
	for d in all_data:
		if(d[0] == eta):
			x += [d[2]]
			y += [d[3]]
		else:
			plt.plot(x,y, label=("eta="+str(eta)))
			eta = d[0]
			x = [d[2]]
			y = [d[3]]
	plt.plot(x,y, label=("eta="+str(eta)))
	# plt.show()
	plt.legend()
	plt.title("Variation of Error with Learning Rate - " + file)
	plt.savefig("plot/fig_" + file + ".png")
	plt.clf()
