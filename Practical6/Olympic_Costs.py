# make a list that contains these values
# sort the list
# make a barchart with the pyplot

# import the pyplot
from matplotlib import pyplot as plot
import numpy as np
#  create a list that contains the data
costs = [1, 8, 15, 7, 5, 14, 43, 40]
# sort it and print it
cost_sorted = sorted(costs)
print(cost_sorted)
# make a barchart with the data
N = len(cost_sorted)
width = 0.35
top_cost = cost_sorted[N-1]
ind = np.arange(N)
p1 = plot.bar(ind, cost_sorted, width)
plot.ylabel('cost')
plot.yticks(np.arange(0, top_cost, 5))
plot.title('the coast range of Olympics')
plot.show()
