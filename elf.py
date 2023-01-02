# Open the file in read mode
f = open('input.txt', 'r')

# Read the lines of the file
lines = f.readlines()

# Close the file
f.close()

#list to hold sum of elf calories
elfs = []
sum = 0
#**************************
# loop through all the lines
# sum all the calories
#***************************
for line in lines:
    if(line == '\n'):
       elfs.append(sum)
       sum = 0
    else: 
       line = line.strip()
       cal = int(line)
       sum = sum + cal 

largest = 0
secLarg = 0
thirdLarg = 0
for e in elfs:
    if(e > largest):
       thirdLarg = secLarg
       secLarg = largest
       largest = e	
    elif (e < largest) and (largest != 0) and (e > secLarg):
       thirdLarg = secLarg
       secLarg = e
    elif (e < largest) and (e < secLarg) and (largest != 0) and (secLarg != 0) and (e > thirdLarg):
       thirdLarg = e	

#*********************
#print out the results
#*********************
print("first largest: " + str(largest))
print("second largest: " + str(secLarg))
print("third largest: " + str(thirdLarg))
calSum = largest + secLarg + thirdLarg
print(calSum)

