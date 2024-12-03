import re

def read_data(filename):
    with open(filename) as fp:
        for line in fp.readlines():
            yield line.strip()

def solve(data_filename, part2=False):
    data = read_data(data_filename)

    product = 0

    enable = True

    for line in data:
        print(line)
        matches = re.findall(r'(do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\))', line)

        for match in matches:
            print(match)

            if match[0] == "do()" and part2:
                print("enable")
                enable = True
            
            if match[0] == "don't()" and part2:
                 print("disable")
                 enable = False

            if match[0].startswith('mul(') and enable:
                print(f"mul {match}")
                product += int(match[1]) * int(match[2]) 

    return product

if __name__ == "__main__":
	print("Part 1 Test: ", solve('days/3/test_data.txt'))
	print("Part 1: ", solve('days/3/data.txt'))
	
	print("Part 2 Test:", solve('days/3/test_data.txt', part2=True))
	print("Part 2:", solve('days/3/data.txt', part2=True)) 