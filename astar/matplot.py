import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

## the data
N = 4
h0 = [170 , 94, 719, 385]
h1 = [16, 25, 211, 130]
h2 = [1115, 634, 5927, 2894]
h3 = [3487 , 1933 , 13144 , 5250]

sample2 = [3720,382,26226]

## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.15                      # the width of the bars

## the bars
rects1 = ax.bar(ind, h1, width,
                color='#f7819f')

rects2 = ax.bar(ind+width, h0, width,
                    color='#8258fa')

rects3 = ax.bar(ind+2*width, h2, width,
                    color='#2efe9a')

rects4 = ax.bar(ind+3*width, h3, width,
                    color='#fe2e2e')

# axes and labels
# ax.set_xlim(-width,len(ind)+width)
# ax.set_ylim(0,6000)
ax.set_ylabel('# of Steps')
ax.set_title('Number of Steps in different Heuristics')
xTickMarks = ['sample'+str(i) for i in range(1,6)]
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=25, fontsize=10)

## add a legend
ax.legend((rects1[0],rects2[0],rects3[0],rects4[0]), ('manhattan','displaced_tiles','inversion_pair/2','trivial'))

plt.show()