
import imp
bio = imp.load_source('bioLibrary', '/home/bill/Documents/ML_Projects/Rosalind/bioLibrary.py')
import numpy as np 
from collections import Counter

def check_zero(possible_strings, times):
	poss_strings = []
	for p in possible_strings:
		poss_strings.append(p[0])

	cnt = Counter()
	for word in poss_strings:
		cnt[word] += 1
	return cnt


def possible(times, length, error, string):
	possible_strings = [] #all possible strings you can find the substring
	for i in range(len(string) +1 - length):
		possible_strings.append((string[i:i+length],i+1))

	return possible_strings
	
import re
def transpose(times, length, error, string):
	possible_strings = possible(times, length, error, string)
	if(error == 0):
		cnt = check_zero(possible_strings, times)
		cnt = cnt.most_common()
		if(cnt[0][1] >= times):
			return (cnt[0][0], [m.start()+1 for m in re.finditer('(?=' + cnt[0][0] + ')', string)])
	else:
		# Find the hamming distance between the strings and
		# put it in a length x length matrix
		hammingsMat = []
	 	for i in range(len(possible_strings)):
			hammings = np.zeros(len(possible_strings))
			for j in range(len(possible_strings)):
				hammings[j] = (bio.hammingDistance(possible_strings[i][0],possible_strings[j][0]))
			hammingsMat.append(hammings)
		# Get possible pairs
		hamming_sum = [] # hamming sum
		for i in range(len(hammingsMat)):
			hamming_sum.append(sum(np.sort(hammingsMat[i])))
		index = np.argmin(hamming_sum)
		indexes = np.argsort(hammingsMat[np.argmin(hamming_sum)])[1:(times)] # first is always zero
		poss_strings = []
		poss_strings.append(possible_strings[index-1])
		for ix in indexes:
			poss_strings.append(possible_strings[ix-1])

		only_strs = []
		positions = []
		for p in possible_strings:
			only_strs.append(p[0])
			positions.append(p[1])
		p_list = [list(x) for x in only_strs]
		final_s = p_list[0]
		for i in range(0,len(only_strs)-1,1):
			ham = bio.hammingDistance(only_strs[i], only_strs[i+1])
			j = 0
			print ham
			while(ham > error):
				if(p_list[i][j] == p_list[i+1][j]):	
					final_s[i] = (p_list[i][j])
				else:
					final_s[i+1] = (p_list[i+1][j])
					ham -=1
				j+=1
			#for k in range(j, len(p_list[i])):
			#	final_s.append(p_list[i][k])
			only_strs[i+1] = "".join(x for x in final_s)
			p_list[i+1] = final_s
	return (final_s, 1)
	
def evaluate(trans, string, positions):
	trans = list(trans)
	string = list(string)

f = open("dataset", "r")
lines = f.readlines()
with open("results.txt","w") as w:
	for i in range(1, len(lines)):
		numbers = map(int, lines[0].split())
		string = lines[1].split()
		trans_string , positions =  transpose(numbers[0], numbers[1], numbers[2], string[0])
		evaluate(trans_string, string, positions)


"""
6 23 0
AATGGGACACATGCGCTGGGAGCCTGGTAATAAGCTGATTGAACTACAGATGACCCGCAAATGGAGACCTTTAGGAAAGAGTATCAAGGAAGTTAGGCGACACACGTACGAAGTGCGCCCAGATCTGACTTAAGAAACGTCGGGGTCATTTGGATACTAAGTCAAGCGAGAGCACGACACCCGCATTCGACCAGTGACCGAATGGGACACATGCGCTGGGAGCCTGCGACGTTCGCCGGCGGTAACGGCTTAACGGGGCTTGTTGCTGCTAGTCGGCGATATAGGTCTTCAGTAAAGCCATCTACTGGCCGCTTTTGAATGGTACCGAAGAGCAAAGCAAGTTCATTTGATTATTCTACTGTGGCGATTTCTATTCGTCGTGTTATAACATTGATTGCTCGCGATCGGGCCCGTTAGGCTTACTTCTGCGGAACGTGTTCTCGAAGGGATAGGTGCGAGGTGCGGGGCATGGAATTTTAGTCCTCCCTCTCCAAGCTGGCCGCTCTTCATGTTGTCATTTTTAGAATTTGGGTTGAGGTCCCCGCATAACAAACACTTTGGGACACATGCGCTGGGAGCCTCCAAAGGCAGTAGGCTTGGGGCACATGGGACACATGCGCTGGGAGCCTACAGGAACCGCTCTCACACGGTCCCGAAATTTGCCCGTGTGACCAACAACATCCTTTTATTTGTCGGCTGAAGTCATTGGTAGCGTGTTCACCCTTACGTGCGTAACCCCAGCGCGAATCTTCACCCCTAATAGTGCCGAGTACAGCTGGGTACCCGCTGCCAGATGAATGTACTAAGTCGGAAGGCATCTGTTTATCTGAGGAGCATTGCCTGCGGGCATAAAAATGGGACACATGCGCTGGGAGCCTCTGTTAGTTGCGAACTACGGACATGGTCCGACACTAGAAAGATTTGTATGGAAGCGGATCGAAGCCCCTGCTTCGACTGTACACCCCATGTCCCGTTCTGAACGATGGGACACATGCGCTGGGAGCCTCCGGGCAATTATGACCACAACTTCGGAGGGTTGTAGATCGGATTATTGCGTATCGTCGCAGTTTTTCCACACGGACTATCGTCGTCTAAACTAACCGGGGGGGCTCAGGTGGGACACATGCGCTGGGAGCCTCTG
"""