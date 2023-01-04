#**************************
# Loops through all the lines
#***************************
# Open the file in read mode
f = open('input.txt', 'r')

# Read the lines of the file
lines = f.readlines()

# Close the file
f.close()

def devPairs(myLines):
	pairs = []
	for line in myLines:
		#split the pairs
		p = line.split(',')
		
		#split each pair lower and high limit
		pair = [[int(x) for x in p[0].split('-')], [int(y) for y in p[1].split('-')]]
	
		pairs.append(pair)
	return pairs

def insideLap(myPairs):
	cnt = 0
	for p in pairs:

		if p[0][0] <= p[1][0] and p[1][1] <= p[0][1]:
			cnt += 1
		elif p[1][0] <= p[0][0] and p[0][1] <= p[1][1]:
			cnt += 1
	return cnt		

def allLaps(myPairs):
	cnt = 0
	for p in pairs:
		#check if second pair is inside first
		if p[0][0] <= p[1][0] and p[1][1] <= p[0][1]:
			cnt += 1
		
		#check if first pair is inside second 
		elif p[1][0] <= p[0][0] and p[0][1] <= p[1][1]:
			cnt += 1

		#check if second pair overlaps neg
		elif p[0][0] <= p[1][0] and p[0][1] <= p[1][1] and p[0][1] >= p[1][0]:
			cnt += 1

		#check if second pair overlaps pos
		elif p[0][0] >= p[1][0] and p[0][1] >= p[1][1] and p[0][0] <= p[1][1]:
			cnt += 1

		#check if first pair overlaps neg
		elif p[1][0] <= p[0][0] and p[1][1] <= p[0][1] and p[1][1] >= p[0][0]:
			cnt += 1

		#check if second pair overlaps pos
		elif p[1][0] >= p[0][0] and p[1][1] >= p[0][1] and p[1][0] <= p[0][1]:
			cnt += 1
	
	return cnt



pairs = devPairs(lines)
count = insideLap(pairs)
print(count)
print(allLaps(pairs))
