# make a list that contains these values
# sort the list
# make a barchart with the pyplot

#  create a list that contains the data
costs = [1, 8, 15, 7, 5, 14, 43, 40]
# sort it and print it
cost_sorted = sorted(costs)
print(cost_sorted)
# import the pyplot and make a barchart
from matplotlib import pyplot as plot
for i in range(len(cost_sorted)):
    plot.bar(i, cost_sorted[i])
plot.show()
