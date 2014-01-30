import glob
import os
import matplotlib.pyplot as plt
os.chdir("./data2")

for file in glob.glob("*"):
	all_data = []
	print (file)
	f = open(file)
	lines = f.readlines()
	for line in lines:
		data = line.split(",")
		all_data += [[float(d) for d in data]]
	moment = 0.1
	x = []
	y = []
	plt.xlabel("Iteration Number")
	plt.ylabel("Error (TSS)")
	for d in all_data:
		if(d[1] == moment):
			x += [d[2]]
			y += [d[3]]
		else:
			plt.plot(x,y, label=("moment="+str(moment)))
			moment = d[1]
			x = [d[2]]
			y = [d[3]]
	plt.plot(x,y, label=("moment="+str(moment)))
	# plt.show()
	plt.legend()
	plt.title("Variation of Error with Momentum with Learning Rate = 0.8 - " + file)
	plt.savefig("plot/fig_" + file + ".png")
	plt.clf()
