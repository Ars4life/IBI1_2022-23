# create a dictionary variable: favourite_movie = {}
# input the data in the table into the dictionary
# print the dictionary
# make a pie plot with the function pyplot in matplotlib.

# import the 'pyplot' from # import the 'matplotlib'
from matplotlib import pyplot as plot
#  create a dictionary that contains the data, the keys are the types of movie genre
#  and the values are the number of students who favourites.
favourite_movie = {'Comedy': 73, 'Action': 42, 'Romance': 38,
                   "Fantasy": 28, "Science-fiction": 22, "Horror": 19,
                   "Crime": 18, "Documentary": 12, 'History': 8, 'War': 7}
print(favourite_movie)
# use the dictionary to make a piechart, define the label, the sizes, and the plots title
types_label = list(list(favourite_movie.keys()))
numbers = list(favourite_movie.values())
plot.pie(numbers, labels=types_label, autopct='%1')
plot.axis('equal')
plot.title('favourite Movie')
plot.show()

