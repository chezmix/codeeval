import sys
file = sys.argv[1]
f = open(file, 'r')

for line in f:
	inputs = line.split(' ')
	a = int(inputs[0])
	b = int(inputs[1])
	n = int(inputs[2])

	result = []
	for x in range(1,n+1):
		if (x % a == 0 and x % b == 0):
			result.append('FB')
		elif (x % a == 0):
			result.append('F')
		elif (x % b == 0):
			result.append('B')
		else:
			result.append(str(x))
		
	print ' '.join(result)