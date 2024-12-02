import re

def read_data(filename):
	with open(filename) as fp:
		return zip(*(re.split(r'\s+', l.strip()) for l in fp.readlines()))

def solve(data_filename, part2=False):
	list1, list2 = read_data(data_filename)

	if not part2:
		return calc_dist(list1, list2)
	else:
		return calc_sim(list1, list2)

def calc_dist(list1, list2):
	dist = 0
	for a, b in zip(sorted(list1), sorted(list2)):
		dist += abs(int(a)-int(b))

	return dist

def calc_sim(list1, list2):
	sim = 0
	for a in sorted(list1):
		occ = sum([1 for b in list2 if b==a])
		sim += int(a)*occ

	return sim

if __name__ == "__main__":
	print("Part 1 Test: ", solve('days/1/test_data.txt'))
	print("Part 1: ", solve('days/1/data.txt'))
	
	print("Part 2 Test:", solve('days/1/test_data.txt', part2=True))
	print("Part 2:", solve('days/1/data.txt', part2=True)) 