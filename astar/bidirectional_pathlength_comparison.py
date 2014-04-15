import numpy as np
import matplotlib.pyplot as plt
import math

fig = plt.figure()
ax = fig.add_subplot(111)

## the data
N = 2
h0 = [31,math.log(3837,1.2)]		#manhattan , #bidirectional manhattan
h1 = [35,math.log(2925,1.2)]  	#path , #steps

sample2 = [3720,382,26226]

## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.2                     # the width of the bars

## the bars
rects1 = ax.bar(ind, h0, width,
                color='#f7819f')

rects2 = ax.bar(ind+width, h1, width,
                    color='#8258fa')

# axes and labels
ax.set_xlim(-width,len(ind)+width)
# ax.set_ylim(0,40)
ax.set_ylabel('# of Steps')
ax.set_title('Bidirectional vs Normal Manhattan Steps an Path Length Comparison')
# xTickMarks = ['sample'+str(i) for i in range(1,5)]
xTickMarks = ['Path Length','Log(Steps)']
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=25, fontsize=10)

## add a legend
ax.legend((rects1[0],rects2[0]), ('Uni-directional','Bi-directional'))

plt.show()