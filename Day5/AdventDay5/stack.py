#**************************
# Loops through all the lines
#***************************
# Open the file in read mode
f = open('input.txt', 'r')

# Read the lines of the file
lines = f.readlines()

# Close the file
f.close()

for line in lines:
	if 'move' in line:
		l = line.split(' ')
		l[5] = l[5].strip('\n')
		l.pop(0)
		l.pop(1)
		l.pop(2)
		print(l)	
		
