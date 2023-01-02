# Open the file in read mode
with open("input.txt", "r") as file:
	totSum = 0
	for line in file:
					
		#keep track of round score
		roundSum = 0


		#choose Loss 
		if line[2] == 'X':
			if line[0] == 'A':
				roundSum += 3
			elif line[0] == 'B':
				roundSum += 1 
			else:   
				roundSum += 2

		#choose Draw 
		elif line[2] == 'Y':
			roundSum += 3
			if line[0] == 'A':
				roundSum += 1
			elif line[0] == 'B':
				roundSum += 2 
			else:   
				roundSum += 3
				
		#choose Win 
		else:
			roundSum += 6
			if line[0] == 'A':
				roundSum += 2
			elif line[0] == 'B':
				roundSum += 3 
			else:   
				roundSum += 1

		totSum += roundSum	
	print('Sum: ' + str(totSum))
