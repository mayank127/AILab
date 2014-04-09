import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

## the data
N = 3
h0 = [12,12,12]
h1 = [24,24,14]

sample2 = [3720,382,26226]

## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.25                      # the width of the bars

## the bars
rects1 = ax.bar(ind, h1, width,
                color='#f7819f')

rects2 = ax.bar(ind+width, h0, width,
                    color='#8258fa')

# axes and labels
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(0,30)
# ax.set_ylabel('# of Steps')
ax.set_xlabel('Heuristic')
ax.set_title('Number of Steps and Path Length in different Missionary Cannibal Heuristics')
# xTickMarks = ['sample'+str(i) for i in range(1,6)]
xTickMarks = ['trivial','(#M+#C)/2','(#M+#C)']
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=0, fontsize=10)

## add a legend
ax.legend((rects1[0],rects2[0]), ('# of Steps','path_length'))

plt.show()