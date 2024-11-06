from random import randint

check_i = type(int())
flips = None

while check_i != type(flips):
  try:
    print('Enter number of flips: ', end='')
    flips = int(input())
    if flips < 1:
      print('Number must be greater than 0...')
      flips = None
  except ValueError:
    print("Not a number...")

def streak_check(num_flips):
  heads = 0
  tails = 0
  h_streak = 0
  t_streak = 0
  f = num_flips

  if f == 0:
    print('Flips must be greater than 0')
    return None
  
  for i in range(f):
    coin = randint(0, 1)
    if coin == 0:
      heads += 1
      streak = 0
      while coin == 0:
        streak += 1
        if streak == 6:
          h_streak += 1
        i += 1
        coin = randint(0, 1)
    else:
      tails += 1
      streak = 0
      while coin == 1:
        streak += 1
        if streak == 6:
          t_streak += 1
        i += 1
        coin = randint(0, 1)
  
  print(f'Coin flipped {f} times.\n\
Number of heads is {heads}.\n\
Percentage of heads with streak of six is {100 * h_streak * 6 / f}%.\n\
Number of tails is {tails}.\n\
Percentage of tails with a streak of six is {100 * t_streak * 6 / f}%\n')

streak_check(flips)