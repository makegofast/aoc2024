from collections import Counter

d_all = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
    "upleft": [-1, -1],
    "upright": [-1, 1],
    "downleft": [1, -1],
    "downright": [1, 1]
}

d_diag = {
    "upleft": [-1, -1],
    "upright": [-1, 1],
    "downleft": [1, -1],
    "downright": [1, 1]
}

def read_data(filename):
    with open(filename) as fp:
        data = []
        for line in fp.readlines():
            data.append([c for c in line.strip()])
        
    return data

def solve(data_filename, part2=False):
    data = read_data(data_filename)

    if not part2:
        matches = []
        token = "XMAS"
        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                matches += search(row, col, data, d_all, token)
            
        return len(matches)
    else: 
        token = "MAS"
        centers = {} 
        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                for match in search(row, col, data, d_diag, token): 
                    center = str(match['indexes'][1])
                    if not center in centers:
                        centers[center] = 0
                    centers[center] += 1

        centers = {p: c for p, c in centers.items() if c>1}
        return len(centers) 


def inbounds(row, col, data):
    return True if row >= 0 and row < len(data) and col >= 0 and col < len(data[row]) else False

def charat(row, col, data):
    try:
        return data[row][col]
    except:
        return False

def search(row, col, data, directions, token):
    matches = []
    for direction in directions.values(): 
        result = icanhastoken(row, col, direction, data, token)
        if result:
            matches.append(result)
    
    return matches

def icanhastoken(start_row, start_col, direction, data, token):
    indexes = []

    for i in range(0, len(token)):
        row = start_row + direction[0] * i
        col = start_col + direction[1] * i

        if not inbounds(row, col, data) or charat(row, col, data) != token[i]:
            return False

        indexes.append([row, col])
    
    return {'start_row': start_row, 'start_col': start_col, 'end_row': row, 'end_col': col, 'indexes': indexes, 'direction': direction, 'token': token}

if __name__ == "__main__":
	print("Part 1 Test: ", solve('days/4/test_data.txt'))
	print("Part 1: ", solve('days/4/data.txt'))
	
	print("Part 2 Test:", solve('days/4/test_data.txt', part2=True))
	print("Part 2:", solve('days/4/data.txt', part2=True)) 
