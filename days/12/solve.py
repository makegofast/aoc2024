def read_data(filename):
	map = []

	with open(filename) as fp:
		for line in fp.readlines():
			map.append([c for c in line.strip()])

	return map

def flood_find(map, start_pos):
	in_region = []
	checked = []
	psides = 0
	directions = [[-1,0], [1,0], [0,-1], [0,1]]

	start_char = map[start_pos[0]][start_pos[1]]
	to_check = [start_pos]

	while len(to_check):
		print(to_check)
		pos = to_check.pop(0)
		in_region.append(pos)
		checked.append(pos)

		for direction in directions:
			row, col = pos[0] + direction[0], pos[1] + direction[1]

			try:
				char = map[row][col]
			except:
				char = None
			
			if char != start_char:
				psides += 1
			elif [row, col] not in checked + to_check:
				to_check.append([row, col])

			checked.append([row, col])
		

	return start_char, in_region, psides
		
def solve(data_filename, part2=False):
	map = read_data(data_filename)

	checked = []
	regions = [] 

	price = 0

	for row in range(len(map)):
		for col in range(len(map[row])):
			if [row, col] in checked:
				continue

			start_char, in_region, psides = flood_find(map, [row, col])
			checked += in_region
			regions.append({
				'char': start_char,
				'points': in_region,
				'psides': psides
			})
		
			price += len(in_region) * psides

			print(start_char, in_region, psides)

	return price

if __name__ == "__main__":
	print("Part 1 Test: ", solve('days/12/test_data.txt'))
	print("Part 1: ", solve('days/12/data.txt'))
	
	#print("Part 2 Test:", solve('days/12/test_data.txt', part2=True))
	#print("Part 2:", solve('days/12/data.txt', part2=True)) 
