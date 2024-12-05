import math

def read_data(filename):
    with open(filename) as fp:
        rules_done = False
        rules = []
        updates = []

        for line in fp.readlines():
            if line.strip() == "":
                rules_done = True
            elif rules_done:
                updates.append([int(s) for s in line.strip().split(',')])
            else:
                rules.append([int(s) for s in line.strip().split('|')])
        
    return rules, updates

def solve(data_filename, part2=False):
    rules, updates = read_data(data_filename)

    part1 = 0

    for update in updates:
        error = False
        for rule in rules:
            if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
                error = True
        if error:
            print(f"Update {update} violates {rule}")
        else:
            #print(f"Update {update} violates no rules")
            part1 += update[math.ceil(int(len(update)/2))] 

    return part1 

if __name__ == "__main__":
	print("Part 1 Test: ", solve('days/5/test_data.txt'))
	print("Part 1: ", solve('days/5/data.txt'))
	
	#print("Part 2 Test:", solve('days/5/test_data.txt', part2=True))
	#print("Part 2:", solve('days/5/data.txt', part2=True)) 
