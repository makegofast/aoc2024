def read_data(filename):
	with open(filename) as fp:
		return [l.strip() for l in fp.readlines()]

def solve(data_filename, part2=False):
	data = read_data(data_filename)

if __name__ == "__main__":
	print("Part 1 Test: ", solve('days/5/test_data.txt'))
	#print("Part 1: ", solve('days/5/data.txt'))
	
	#print("Part 2 Test:", solve('days/5/test_data.txt', part2=True))
	#print("Part 2:", solve('days/5/data.txt', part2=True)) 
