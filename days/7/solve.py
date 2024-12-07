def read_data(filename):
	data = []
	with open(filename) as fp:
		for line in fp.readlines():
			result, values = line.strip().split(': ')
			result = int(result)
			values = [int(v) for v in values.split()]

			data.append([result, values])
	
	return data

def _product(a, b):
	return a*b

def _sum(a, b):
	return a+b

def _concat(a, b):
	return int(str(a) + str(b))

def gen_permutations(operators, depth, perms, history = None):
	if not history:
		history = ""

	if not depth:
		perms.append(history.strip().split())
		return
	
	for op in operators:
		gen_permutations(operators, depth-1, perms, history + " " + op) 

	return perms 
		
def apply(values, ops, target):
	a = values.pop(0)
	
	for opname in ops:
		oper = globals()[opname]
		a = oper(a, values.pop(0))
		
		if a > target:
			return False
	
	return a
	
def solve(data_filename, part2=False):
	data = read_data(data_filename)

	total = 0
	ops = ['_sum', '_product']

	if part2:
		ops.append('_concat')

	for target, values in data:
		perms = gen_permutations(ops, len(values)-1, [])
		print(target, values, len(perms))

		valid = False

		for perm in perms:
			r = apply(values.copy(), perm, target)
			if r == target:
				valid = True
				break

		if valid:
			total += target 

	return total

if __name__ == "__main__":
	print("Part 1 Test: ", solve('days/7/test_data.txt'))
	print("Part 1: ", solve('days/7/data.txt'))
	
	print("Part 2 Test:", solve('days/7/test_data.txt', part2=True))
	print("Part 2:", solve('days/7/data.txt', part2=True)) 
