def read_data(filename):
    with open(filename) as fp:
        for line in fp.readlines():
            yield [int(i) for i in line.strip().split()]

def is_safe_report(orig_values):
    #print()
    #print(f"Checking {values}")

    values = orig_values.copy()
    first_direction = None
    last_value = None

    last_value = values.pop(0)

    for value in values:
        direction = 'inc' if last_value > value else 'dec'

        if not first_direction:
            first_direction = direction

        distance = abs(value - last_value)

        #print(f"Comparing last_value = {last_value} to value = {value} distance = {distance} direction = {direction}")

        if distance < 1 or distance > 3 or direction != first_direction:
            #print(f"Violation")
            return False
        
        last_value = value
    
    #print(f"{values} seems like a safe report")

    return True

def solve(data_filename, part2=False):
    data = read_data(data_filename)

    safe_count = 0 

    for d in data:
        print(f"Checking {d}")

        test_d = d.copy()
        is_safe = is_safe_report(test_d)

        if not is_safe and part2:
            print("Part 2 Tests...")
            for i in range(0, len(d)):
                test_d = d.copy()
                test_d.pop(i)
                #print(f"Permutation {i}\n{d}\n{test_d}")

                if is_safe_report(test_d):
                    print(f"Solution with permutation {i}: {test_d}")
                    is_safe = True
                    break
            
            if not is_safe:
                print(f"No solution found in {i} permutations for {d}")

        safe_count += 1 if is_safe else 0
        #print(f"Safe count: {safe_count}")

    return safe_count 

if __name__ == "__main__":
	print("Part 1 Test: ", solve('days/2/test_data.txt'))
	print("Part 1: ", solve('days/2/data.txt'))
	
	print("Part 2 Test:", solve('days/2/test_data.txt', part2=True))
	print("Part 2:", solve('days/2/data.txt', part2=True)) 