# pseudocode:
# generation begin as 1, number of rabbit begin as 2
# repeat
# what's the number of rabbit? 
#	if <= 100: number of rabbit double, generation add 
#		store the number of generation
#       if > 100: done
# display the stored generation number


# code:
# create variables:
#gen represents the number of generation,begins at 1.
# 'num' represents the number of rabbit, begins at 2.
gen = 1
num = 2
# create a loop to repeat.
# compare the number of rabbits with 100, if less, move on to the next generation, if more, stop.
for i in range(0, 100):
	if num <= 100:
		num *= 2
		gen +=1
	else:
		break
# display the last generation that have the number of rabbit less than 100
gen_over100 = gen + 1
print('At the', str(gen_over100), 'generation, more than 100 rabbits have been born')
