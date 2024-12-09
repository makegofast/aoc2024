def read_data(filename):
	with open(filename) as fp:
		return [int(c) for l in fp.readlines() for c in l.strip()]

def parse_map(map):
	parsed = []

	id = 0
	is_block_size = True

	while len(map):
		v = map.pop(0)

		if is_block_size:
			parsed += [str(id)] * v
			id += 1
		else:
			parsed += ['.'] * v
		
		is_block_size = not is_block_size
	
	return parsed 

def print_map(map, debug_text = None):
	print(''.join(map), debug_text)

def compact(map):
	#print("compacting...")
	#print_map(map, "start")
	for src in range(len(map)-1, 0, -1):
		changed = False
		char = map[src]
		dst = None
		if char != '.':
			try:
				dst = next(i for i, v in enumerate(map) if v is '.' and i < src)
				map[dst] = char
				map[src] = '.'
				changed = True
			except StopIteration:
				break
		#print_map(map, f"{src}->{dst} {char} {changed}")
	
	#print_map(map, "end")

	return map

def calc_checksum(map):
	sum = 0
	for i, id in enumerate(map):
		sum += i*int(id) if id != '.' else 0
	return sum

def solve(data_filename, part2=False):
	data = read_data(data_filename)
	#print(data)

	map = parse_map(data)
	#print(map)

	map = compact(map)

	return calc_checksum(map)

if __name__ == "__main__":
	print("Part 1 Test: ", solve('days/9/test_data.txt'))
	print("Part 1: ", solve('days/9/data.txt'))
	
	#print("Part 2 Test:", solve('days/9/test_data.txt', part2=True))
	#print("Part 2:", solve('days/9/data.txt', part2=True)) 
