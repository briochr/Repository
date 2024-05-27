import time
import copy

t = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def count(table, i, j):
    count = 0
    rows, cols = len(table), len(table[0])
    
    neighbors = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1),          (0, 1),
                 (1, -1), (1, 0),  (1, 1)]
    
    for di, dj in neighbors:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols and table[ni][nj] == 1:
            count += 1
            
    return count

def show(table):
    for row in table:
        print(' '.join(str(cell) for cell in row))
    print()

while True:
    #next_t = [row[:] for row in t] both are equivalent
    next_t = copy.deepcopy(t)
    
    for i in range(len(t)):
        for j in range(len(t[0])):
            live_neighbors = count(t, i, j)
            if t[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    next_t[i][j] = 0
            elif t[i][j] == 0:
                if live_neighbors == 3:
                    next_t[i][j] = 1
    
    t = next_t
    show(t)
    time.sleep(1)
