# create a dictionary variable: favourite_movie = {}
# input the data in the table into the dictionary
# print the dictionary
# make a pie plot with the fucntion pyplot in matplotlib


#  create a dictionary that contains the data
favourite_movie = {'Comedy': 73, 'Action': 42, 'Romance': 38,
                   "Fantasy": 28, "Science-fiction": 22, "Horror": 19,
                   "Crime": 18, "Documentary": 12, 'History': 8, 'War': 7}
print(favourite_movie)
# import the 'pyplot' from # import the 'matplotlib'
from matplotlib import pyplot as plot
# use the dictionary to make a piechart
plot.pie(list(favourite_movie.values()), labels=list(list(favourite_movie.keys())))
plot.show()
