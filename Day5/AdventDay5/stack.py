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
			row = [*line]
			rows.append(row)
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

	rowUnits = []	
	fullUnits = []

	for r in rows:
		unit = int(int(len(r)) / int(len(cols)))
		rowUnits = [r[x:x+unit] for x in range(0,len(r),unit)]
		fullUnits.append(rowUnits)
	
	myStrs = []
	for x in fullUnits: 
		items = ['*']*len(cols) 
		cnt = 0
		for y in x:
			for m in y:
				if m != ' ' and m != '[' and m != ']' and m != '\n':
					items[cnt] = m
			cnt += 1
		myStrs.append(items)
				
	return rules, myStrs
		
def createCols(board):
	myCols = {} 
	cnt = 1
	for x in range(len(board[0])):
		col = []
		for b in board:
			col.append(b[x])	
			if '*' in col:
				col.remove('*')
		myCols[cnt] = col
		cnt += 1
	return myCols

def move(cols, rules):
	for r in rules:
		size = int(r[0])
		froCol = int(r[1])
		toCol = int(r[2])

		f = cols.get(froCol)
		t = cols.get(toCol)
		

rules,board = formatGame(lines)
myCols = createCols(board)
for m,t in myCols.items():
	print(m)
	print(t)
