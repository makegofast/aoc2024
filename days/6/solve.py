def read_data(filename):
    map = []

    with open(filename) as fp:
        for line in fp.readlines():
            map.append([c for c in line.strip()])
    
    return map

def find_start_pos(map):
    for row, cols in enumerate(map):
        if '^' in cols:
            return [row, cols.index('^')]
    
    return None
    
def print_map(map):
    print()
    for row, cols in enumerate(map):
        line = []
        for col, char in enumerate(self.map[row]):
            familiar = self.seems_familiar([row, col])
            if char != '^' and familiar:
                char = familiar 

            line.append(char)
        
        print(''.join(line))
    print()

def solve(data_filename, part2=False):
    map = read_data(data_filename)
    status, visited = run_map(map)

    if not part2:
        return len(visited)
    else:
        candidates = set()
        for pos in visited:
            if map[pos[0]][pos[1]] == '^':
                continue
            status, _ = run_map(map, pos)
            if status == "infinite_loop":
                candidates.add(pos)

        return len(candidates)

def run_map(map, obstruction = None):
    directions = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1]
    ]

    start_pos = find_start_pos(map)
    velocity = directions[0]

    current_pos = start_pos
    status = None
    visited = set()
    path = set() 

    while status not in ["off_screen", "infinite_loop"]:
        nr, nc = [x+y for x, y in zip(current_pos, velocity)]  
        try:
            char = map[nr][nc]
        except:
            char = None

        hash = tuple([nr, nc, tuple(velocity)])
        if hash in path:
            status = "infinite_loop"
        if nr < 0 or nr >= len(map) or nc < 0 or nc >= len(map[0]):
            status = "off_screen"
        elif char == '#' or (nr, nc) == obstruction:
            velocity = directions[(directions.index(velocity)+1)%len(directions)]
        else:
            current_pos = [nr, nc]
            visited.add(tuple([nr, nc]))
            path.add(tuple([nr, nc, tuple(velocity)]))

        #print(status, current_pos, velocity, [nr, nc], char)

    return status, visited

if __name__ == "__main__":
    import time
    start_time = time.time()
	#print("Part 1 Test: ", solve('days/6/test_data.txt'))
	#print("Part 1: ", solve('days/6/data.txt'))
	
    #print("Part 2 Test:", solve('days/6/test_data.txt', part2=True))
    print("Part 2:", solve('days/6/data.txt', part2=True)) 
    end_time = time.time()
    print(f"took {end_time-start_time} seconds")
