from decimal import Decimal


def find_limit(n, a, b): #start_values
	curr = n
	converged = 0 # check for convergence
	tries = 0 # count tries until convergence, so we can stop
	while(converged == 0):
		count = a*curr - b*(curr**2)
		if(count < 0):
			return 0.0
		tries += 1
		if(abs(count - curr) <= 0.00000001):
			converged = 1
			return round(count, 4)
		curr = count
		
		if(tries > 1e4): # hasn't converged in 10000 rounds
			return -1


# Read dataset
f = open("dataset.txt", "r")
lines = f.readlines()
with open("results.txt","w") as w:
	for i in range(1, len(lines)):
		numbers = map(Decimal, lines[i].split())
		w.write(str(find_limit(numbers[0], numbers[1], numbers[2])) + "\n")

