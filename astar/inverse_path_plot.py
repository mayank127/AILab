import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

## the data
N = 5
opti_path = [170, 3720, 94, 719, 385]
non_opti_path = [16, 382, 25, 211, 130]
h2 = [1115, 26226, 634, 5927, 2894]

## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.25                      # the width of the bars

## the bars
rects1 = ax.bar(ind, h0, width,
                color='grey')

rects3 = ax.bar(ind+2*width, h1, width,
                    color='orange')

# axes and labels
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(0,4000)
ax.set_ylabel('# of Steps')
ax.set_title('Number of Steps in different Heuristics')
xTickMarks = ['heuristic'+str(i) for i in range(1,6)]
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=25, fontsize=10)

## add a legend
ax.legend( (rects1[0], rects2[0], rects3[0]), ('displaced_tiles', 'manhattan', 'inversion_pair') )

plt.show()