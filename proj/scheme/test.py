
def part(N, maximum, maximum_partitions, prefix = [], lol =[]):
	if N == 0:
		if len(prefix) <= maximum_partitions:
			print(prefix)
			lol.append(prefix)
		return 
	for i in range(min(maximum, N), 0, -1):
		print(part(N-i, i, maximum_partitions, prefix + [str(i)], lol))

