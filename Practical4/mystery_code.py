# What does this piece of code do?
# Answer:Each time the loop runs, it draws a random number between 1 and 10, adds it to the total, and increases the progress by 1. The loop runs until progress is greater than 10, which means it will run 11 times (from progress=0 to progress=10). After the loop finishes, it prints the total of the random numbers drawn.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0
progress=0
while progress<=10:
	progress+=1
	n = randint(1,10)
	total_rand+=n

print(total_rand)

