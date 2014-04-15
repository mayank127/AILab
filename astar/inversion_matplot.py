import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

## the data
N = 4

inv1 = [15, 13, 17, 15]
inv2 = [15,13,17,15]

# h0 = [170 , 94, 719, 385]
# h1 = [16, 25, 211, 130]
# h2 = [1115, 634, 5927, 2894]
# h3 = [3487 , 1933 , 13144 , 5250]


## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.15                      # the width of the bars

## the bars
rects1 = ax.bar(ind, inv1, width,
                color='#f7819f')

rects2 = ax.bar(ind+width, inv2, width,
                    color='#8258fa')

# axes and labels
# ax.set_xlim(-width,len(ind)+width)
# ax.set_ylim(0,6000)
ax.set_ylabel('Path Length')
ax.set_title('Path Length Comparison in invers')
xTickMarks = ['sample'+str(i) for i in range(1,6)]
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=25, fontsize=10)

## add a legend
ax.legend((rects1[0],rects2[0]), ('optimised','non-optimised'))

plt.show()