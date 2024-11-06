from random import randint
from copy import deepcopy
from time import sleep
from sys import exit

COLUMN = 60
ROW = 20

next_cell = []

for x in range(COLUMN):
  column = []
  for y in range(ROW):
    if randint(0, 1) == 0:
      column.append('#') # Living
    else:
      column.append(' ') # Dead
  next_cell.append(column)
try:
  while True:
    print('\n\n\n\n\n')
    current_cell = deepcopy(next_cell)
  
    for y in range(ROW):
      for x in range(COLUMN):
        print(current_cell[x][y], end='')
      print()
  
    for x in range(COLUMN):
      for y in range (ROW):
        l_coord = (x - 1) % COLUMN
        r_coord = (x + 1) % COLUMN
        a_coord = (y - 1) % ROW
        b_coord = (y + 1) % ROW
      
        num_neighbor = 0
        if current_cell[l_coord][a_coord] == '#':
          num_neighbor += 1
        if current_cell[x][a_coord] == '#':
          num_neighbor += 1
        if current_cell[r_coord][a_coord] == '#':
          num_neighbor += 1
        if current_cell[l_coord][y] == '#':
          num_neighbor += 1
        if current_cell[r_coord][y] == '#':
          num_neighbor += 1
        if current_cell[l_coord][b_coord] == '#':
          num_neighbor += 1
        if current_cell[x][b_coord] == '#':
          num_neighbor += 1
        if current_cell[r_coord][b_coord] == '#':
          num_neighbor += 1
        
        if current_cell[x][y] == '#' and (num_neighbor == 2 or num_neighbor == 3):
          next_cell[x][y] = '#'
        elif current_cell[x][y] == ' ' and num_neighbor == 3:
          next_cell[x][y] = '#'
        else:
          next_cell[x][y] = ' '
  
    sleep(1)
except KeyboardInterrupt:
  print('Exiting...')
  exit()