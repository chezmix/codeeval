import sys
file = sys.argv[1]
f = open(file, 'r')

for line in f:
	inputs = line.split(',')
	x = int(inputs[0])
	n = int(inputs[1])

	i = n
	while (x > i):
		i = i + n

	print i