import copy

map = [] 

class LabMapper(object):
    dorder = ['^', '>', 'v', '<']

    dmap = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1]
    ]

    def __init__(self, map_filename):
        self.orig_map = []

        with open(map_filename) as fp:
            for row, line in enumerate(fp.readlines()):
                self.orig_map.append([c for c in line.strip()])

        self.reset()
    
    def reset(self):
        self.map = copy.deepcopy(self.orig_map)
        self.find_start_pos()
        self.pos, self.dir = self.starting_pos, self.starting_dir
        self.visited = []
        self.path = [
            {'pos': self.pos, 'dir': self.dir}
        ]

    def char_at(self, pos):
        row, col = pos

        try:
            return self.map[row][col]
        except:
            return None

    def find_start_pos(self):
        for row, cols in enumerate(self.orig_map):
            for col, char in enumerate(cols):
                if char == "^":
                    self.starting_pos = [row, col]
                    self.starting_dir = self.dorder.index(char)
    
    def seems_familiar(self, pos, dir = None):
        updown = leftright = False 

        matches = [(i, p) for i, p in enumerate(self.path) if p['pos'] == pos and (p['dir'] == dir or dir == None)]

        if not matches:
            return None

        for i, p in matches:
            if p['dir'] in [0, 2]:
                updown = True
            else:
                leftright = True

        if updown and leftright:
            return '+'
        elif updown:
            return '|'
        else:
            return '-'

    def turn_right(self):
        self.dir = (self.dir+1) % len(self.dorder)
    
    def take_step(self):
        new_pos = [x + y for x, y in zip(self.pos, self.dmap[self.dir])]

        target_char = self.char_at(new_pos)

        if not target_char:
            result = "off screen"
        elif target_char in("#", "O"):
            self.turn_right()
            result = "turned right"
        else:
            self.pos = new_pos
            self.path.append({'pos': self.pos, 'dir': self.dir})
            result = "took step"

        if new_pos not in self.visited:
            self.visited.append(new_pos)

        if {'pos': self.pos, 'dir': self.dir} in self.path:
            return "infinite loop"

        self.path.append({'pos': self.pos, 'dir': self.dir})

        return result

    def walk(self):
        breadcrumbs = []

        while True:
            result = self.take_step()

            if result in ["off screen", "infinite loop"]:
                return result
       
    def print_path(self):
        print()
        for row, cols in enumerate(self.map):
            line = []
            for col, char in enumerate(self.map[row]):
                familiar = self.seems_familiar([row, col])
                if char != '^' and familiar:
                    char = familiar 

                line.append(char)
            
            print(''.join(line))
        print()

def solve(data_filename, part2=False):
    lm = LabMapper(data_filename)

    result = lm.walk()
    print(result, "visited: ", len(lm.visited))
    if not part2:
        return len(lm.visited)

    lm.print_path()

    if part2:
        candidates = []
        to_check = lm.path[1:]
        for i, p in enumerate(to_check):
            old_char = lm.char_at(p['pos'])
            lm.map[p['pos'][0]][p['pos'][1]] = "O"
            lm.pos = lm.path[i-1]['pos']
            lm.dir = lm.path[i-1]['dir']
            lm.path = to_check[:i-1]
            result = lm.walk()
            print(f"part2 test {i}, {p} {result} (candidates {len(candidates)})")
            if result == "infinite loop" and p['pos'] not in candidates:
                candidates.append(p['pos'])
            lm.map[p['pos'][0]][p['pos'][1]] = old_char 

        return len(candidates)

if __name__ == "__main__":
	print("Part 1 Test: ", solve('days/6/test_data.txt'))
	#print("Part 1: ", solve('days/6/data.txt'))
	
	print("Part 2 Test:", solve('days/6/test_data.txt', part2=True))
	#print("Part 2:", solve('days/6/data.txt', part2=True)) 
