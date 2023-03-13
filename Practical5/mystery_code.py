# What does this piece of code do?
# Answer: take random number 10 times and display the greatest one.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

# create 2 variabls, 'progress' represent how many times random number has been draw, 'stored_random_number' stores the greatest random number ever
progress=0
stored_random_number=0
# constrict the 'progress' is less then 10, means that only repeat 10 times.
while progress<10:
# draw a random number. and each time repeat, 'progress' while add 1
	progress+=1
	n = randint(1,100)
# store the random number if it is the biggest ever.
	if n > stored_random_number:
		stored_random_number = n
# display the biggest random number in 10 times draw.
print(stored_random_number)
