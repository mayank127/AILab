import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

## the data
N = 4
h0 = [170 , 94, 719, 385] #displaced
h1 = [90 , 53 , 242 , 163 ]  #bidirectional displaced
# h1 = [16, 25, 211, 130]		#manhattan
# h1 = []  #bidirectional manhattan

sample2 = [3720,382,26226]

## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.2                      # the width of the bars

## the bars
rects1 = ax.bar(ind, h0, width,
                color='#f7819f')

rects2 = ax.bar(ind+width, h1, width,
                    color='#8258fa')

# axes and labels
ax.set_xlim(-width,len(ind)+width)
# ax.set_ylim(0,6000)
ax.set_ylabel('# of Steps')
ax.set_title('Bidirectional vs Normal Displaced Tiles Comparison')
xTickMarks = ['sample'+str(i) for i in range(1,5)]
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=25, fontsize=10)

## add a legend
ax.legend((rects1[0],rects2[0]), ('normal','bidirectional'))

plt.show()