import itertools

def read_data(filename):
	map = []
	antennas = {}

	with open(filename) as fp:
		for row, cols in enumerate(fp.readlines()):
			map.append([])

			for col, char in enumerate(cols.strip()):
				if char != '.':
					if not char in antennas:
						antennas[char] = [] 
					antennas[char].append([row, col])

				map[row].append(char)
	
	dimensions = [len(map), len(map[0])]
	return map, antennas, dimensions

def print_map(map, antennas, antinodes, part2):
	antinode_count = set() 

	for row, cols in enumerate(map):
		line = []
		for col, char in enumerate(cols):
			has_antinode = [c for c in antinodes if [row, col] in antinodes[c]]
			if has_antinode: 
				antinode_count.add(f"{row}:{col}")
				char = "#"
			
			if part2 and [c for c in antennas if [row, col] in antennas[c]]:
				antinode_count.add(f"{row}:{col}")
			
			line.append(char)

		print(''.join(line))

	print(antinodes)

	return len(antinode_count)

def in_bounds(pos, dimensions):
	if min(pos) >= 0 and pos[0] < dimensions[0] and pos[1] < dimensions[1]:
		return True

def solve(data_filename, part2=False):
	map, antennas, dimensions = read_data(data_filename)
	antinodes = {}

	for char, locations in antennas.items():
		pairs = itertools.product(locations, locations)
		antinodes[char] = []

		for a, b in pairs:
			if a == b:
				continue
			
			m = 0
			while True:
				m += 1
				delta = ((a[0] - b[0]) * m, (a[1] - b[1]) * m)
				aa = [x + y for x, y in zip(a, delta)]
				ab = [x - y for x, y in zip(b, delta)]

				if in_bounds(aa, dimensions):
					antinodes[char].append(aa) 
				
				if in_bounds(ab, dimensions):
					antinodes[char].append(ab)
				
				if not part2 or (not in_bounds(aa, dimensions) and not in_bounds(ab, dimensions)):
					break
	
	return print_map(map, antennas, antinodes, part2)

if __name__ == "__main__":
	print("Part 1 Test: ", solve('days/8/test_data.txt'))
	print("Part 1: ", solve('days/8/data.txt'))
	
	print("Part 2 Test:", solve('days/8/test_data.txt', part2=True))
	print("Part 2:", solve('days/8/data.txt', part2=True)) 
