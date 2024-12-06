import math

def read_data(filename):
    with open(filename) as fp:
        map = []

        for row, line in enumerate(fp.readlines()):
            for col, char in enumerate(line.strip()):
                print(row, col, char)
        
    return map

def solve(data_filename, part2=False):
    map = read_data(data_filename)

if __name__ == "__main__":
	print("Part 1 Test: ", solve('days/6/test_data.txt'))
	#print("Part 1: ", solve('days/6/data.txt'))
	
	#print("Part 2 Test:", solve('days/6/test_data.txt', part2=True))
	#print("Part 2:", solve('days/6/data.txt', part2=True)) 
