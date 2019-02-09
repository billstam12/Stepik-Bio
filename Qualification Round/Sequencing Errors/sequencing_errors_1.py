from scipy.special import binom
from decimal import Decimal
import math

def count_expected_number(L, k, n, p):
	return (L - n -k)*(0.75)

def bionomial(L, n, k):
	coeffs = []
	for i in range(k+1):
		coeffs.append((binom(k,i))*((n/L)**i)*((1-n/L)**(k-i)))
	return coeffs

def pbinom(x, n, p):
	coeffs = []
	for i in range(x+1):
		coeffs.append((binom(n,i))*((p)**i)*((1-p)**(n-i)))
	return sum(coeffs)

def expected_nums(n, k, length):
	expecs = []
	for i in range(length):
		if(i == 0):
			expecs.append(0.75)
		else:
			lim = int(math.floor((i - 1)/2))
			out = (pbinom(lim, i, 1-p))
			if (( i % 2) == 0):
				i/2, i, p
				out += (binom(i, i/2))*((p)**(i/2))*((1-n/L)**(i/2))
			expecs.append(out)
	return expecs

# Read dataset
f = open("dataset.txt", "r")
lines = f.readlines()
with open("results.txt","w") as w:
	for i in range(1, len(lines)):
		numbers = map(float, lines[i].split())
		L = (numbers[0])
		n = (numbers[1])
		p = (numbers[2])
		k = int(numbers[3])
		coeffs = bionomial(L, n, k)
		expecs = expected_nums(n, k, len(coeffs))

		summ = 0
		for i in range(len(coeffs)):
			summ += coeffs[i]*expecs[i]

		w.write(str(L*summ) + "\n")
