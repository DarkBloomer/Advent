#read data from file and return a string of data
def readFile(input):
	data = ""
	with open(input, "r") as file:
	    data = file.read()
	    return data

def first_unique_four(s):
    for i in range(len(s) - 13):
        if len(set(s[i:i+14])) == 14:
            return (i + 14) 
    return None

rawSig = readFile("input.txt")
start = first_unique_four(rawSig)
print(start)
