def read_data(filename):
	with open(filename) as fp:
		return {v: 1 for v in fp.readline().strip().split()}

def solve(data_filename, part2=False):
	data = read_data(data_filename)

	for i in range(75 if part2 else 25):
		
		new_data = {}
		for k, v in data.items():
			if k == '0':
				new_data.setdefault('1', 0)
				new_data['1'] += v 
			elif len(k)%2 == 0:
				idx = len(k)//2
				left, right = str(int(k[:idx])), str(int(k[idx:]))
				new_data.setdefault(left, 0)
				new_data[left] += v
				new_data.setdefault(right, 0)
				new_data[right] += v
			else:
				nk = str(int(k)*2024) 
				new_data.setdefault(nk, 0)
				new_data[nk] += v	
		data = new_data

		stones = sum(data.values())
		print(i+1, stones)

	return stones 

if __name__ == "__main__":
	print("Part 1 Test: ", solve('days/11/test_data.txt'))
	print("Part 1: ", solve('days/11/data.txt'))
	
	print("Part 2 Test:", solve('days/11/test_data.txt', part2=True))
	print("Part 2:", solve('days/11/data.txt', part2=True)) 
