def read_data(filename):
	with open(filename) as fp:
		return [int(c) for l in fp.readlines() for c in l.strip()]

def parse_map(map):
	parsed = []

	id = 0
	is_block_size = True

	while len(map):
		v = map.pop(0)

		parsed.append({'size': v, 'id': id if is_block_size else None})
		if is_block_size:
			id += 1
		
		is_block_size = not is_block_size
	
	return parsed 

def calc_checksum(map):
	sum = 0
	pos = 0
	for n in map:
		for i in range(0, n['size']):
			if n['id'] is not None:
				sum += pos * n['id']
			pos += 1
	
	return sum

def expand_map(map):
	line = ""
	for node in map:
		char = '.' if node['id'] is None else str(node['id'])
		line += char * node['size']

	return ''.join(line)

def print_map(map, debug_text = None):
	print(expand_map(map), debug_text or "")

def repack_nodes(map, current_index):
	removed = 0
	i = 0
	while True:
		if not i < len(map):
			break
		elif map[i]['size'] == 0:
			#print(f"removed one empty node at {i} for {map[i]['id']}")
			#print(map[i])
			del(map[i])
			if i <= current_index:
				removed += 1
		elif i+1 < len(map) and map[i]['id'] == map[i+1]['id']:
			#print(f"consolidated two nodes at {i} and {i+1} for id {map[i]['id']} {map[i]['size']} + {map[i+1]['size']}")
			#print(map[i], map[i+1])
			map[i]['size'] += map[i+1]['size']
			del(map[i+1])
			if i+1 <= current_index:
				removed += 1
		else:
			i += 1

	return removed

def compact(map, part2):
	print("compacting...")
	#print(map)
	#print_map(map, "start")

	current_id = max([n['id'] for n in map if n['id'] is not None])

	while True and current_id >= 0:
		target_index = None
		source_index = max([i for i, n in enumerate(map) if n['id'] == current_id])

		source_node = map[source_index]
		src_id = source_node['id']
		#print(source_index, source_node)

		block_size = source_node['size'] if part2 else 1

		try:
			target_index = next(i for i, v in enumerate(map) if v['size'] >= block_size and v['id'] is None and i < source_index)
		except StopIteration:
			#print(f"no space to fit {block_size} blocks for {source_node}")
			current_id -= 1
			continue

		if target_index:
			debug = f"move {block_size} block(s) for {src_id} from {source_index} -> {target_index}" 
			print(debug)

			map[target_index]['size'] -= block_size

			map.insert(target_index, {'size': block_size, 'id': source_node['id']})

			source_node['size'] -= block_size

			map.insert(source_index+1, {'id': None, 'size': block_size})
		
			repack_nodes(map, source_index)

		#print_map(map, debug) 
		#print(debug)

	print_map(map, "end")

	return map

def solve(data_filename, part2=False):
	data = read_data(data_filename)
	map = parse_map(data)
	map = compact(map, part2)

	return calc_checksum(map)

if __name__ == "__main__":
	print("Part 1 Test: ", solve('days/9/test_data.txt'))
	#print("Part 1: ", solve('days/9/data.txt'))
	
	print("Part 2 Test:", solve('days/9/test_data.txt', part2=True))
	print("Part 2:", solve('days/9/data.txt', part2=True)) 
