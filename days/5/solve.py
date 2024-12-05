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

    bad_updates = []
    part1_total = 0
    part2_total = 0

    for update in updates:
        error = False
        for rule in rules:
            if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
                #print(f"Update {update} violates {rule}")
                error = True
                
        if error:
            bad_updates.append(update)
        else:
            #print(f"Update {update} violates no rules")
            part1_total += update[math.ceil(int(len(update)/2))] 
    
    for update in bad_updates:
        print(f"Bad Update: {update}")

        corrected = None
        while not corrected:
            corrected = True 
            for rule in rules:
                if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
                    print(f"Update {update} violates {rule}")
                    update.remove(rule[0])
                    update.insert(update.index(rule[1]), rule[0])
                    corrected = False
        
        print(f"Corrected: {update}")
        part2_total += update[math.ceil(int(len(update)/2))]

    return part2_total if part2 else part1_total 

if __name__ == "__main__":
	print("Part 1 Test: ", solve('days/5/test_data.txt'))
	print("Part 1: ", solve('days/5/data.txt'))
	
	print("Part 2 Test:", solve('days/5/test_data.txt', part2=True))
	print("Part 2:", solve('days/5/data.txt', part2=True)) 
