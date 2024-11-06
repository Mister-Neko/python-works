from time import sleep
from sys import exit

ind = 0
ind_inc = True

try:
  while True:
    print(' ' * ind, end='')
    print('********')
    sleep(0.2) # 1/10 of a second pause

    if ind_inc == True:
      ind += 1
      if ind == 20:
        ind_inc = False
    else:
      ind -= 1
      if ind == 0:
        ind_inc = True

except KeyboardInterrupt:
  print(' ' * ind + 'Exiting...')
  exit()