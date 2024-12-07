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


def gen_permutations(operators, depth, perms, history = None):
	if not history:
		history = ""

	if not depth:
		perms.append(history.strip().split())
		return
	
	for op in operators:
		gen_permutations(operators, depth-1, perms, history + " " + op) 

	return perms 
		
def apply(values, ops):
	for opname in ops:
		oper = globals()[opname]
		a = values.pop(0)
		b = values.pop(0)
		r = oper(a, b)
		values.insert(0, r)
	
	return values[0]
	
def solve(data_filename, part2=False):
	data = read_data(data_filename)

	total = 0
	ops = ['_sum', '_product']

	if part2:
		ops.append('_concat')

	for target, values in data:
		#print(target, "values: ", values)
		perms = gen_permutations(ops, len(values)-1, [])
		#print(f"perms: {perms}")

		valid = False

		for perm in perms:
			r = apply(values.copy(), perm)
			#print(target, values, perm, r)
			if r == target:
				valid = True

		if valid:
			total += target 

	return total

if __name__ == "__main__":
	print("Part 1 Test: ", solve('days/7/test_data.txt'))
	print("Part 1: ", solve('days/7/data.txt'))
	
	#print("Part 2 Test:", solve('days/7/test_data.txt', part2=True))
	#print("Part 2:", solve('days/7/data.txt', part2=True)) 
