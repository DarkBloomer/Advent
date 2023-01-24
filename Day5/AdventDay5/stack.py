#**************************
# Loops through all the lines
#***************************
# Open the file in read mode
f = open('input.txt', 'r')

# Read the lines of the file
lines = f.readlines()

# Close the file
f.close()

def formatGame(gameLines):
	rowCnt = 0
	rows = []
	rules = []

	for line in gameLines:
		if line == '\n':
			continue

		elif '[' in line:
			rows.append(line)
			rowCnt += 1

		elif line[1] == '1':
			cols = line.split('   ')
			cols[0] = '1'
			cols[len(cols) - 1] = cols[len(cols) - 1].replace(' \n', '')
			print(cols)

		elif 'move' in line:
			l = line.split(' ')
			l[5] = l[5].strip('\n')
			l.pop(0)
			l.pop(1)
			l.pop(2)
			rules.append(l)

		print("RULES")
		for rule in rules:
			print(rule)
		
		print("ROWS")
		for r in rows:
			print(r)
formatGame(lines)
