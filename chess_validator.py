from random import randint
from random import choice
from copy import deepcopy
from time import sleep

'''
Valid chess board positions and pieces
16 pieces total
Each side has a possible piece count:
1 king
9 queen
10 bishops
10 rooks
10 knights
8 pawns

board quadrants are 1 - 8 vertical and a - h horizontal
'''

pieces = ['bKing', 'wKing',
          'bQueen', 'wQueen',
          'bRook', 'wRook',
          'bBishop', 'wBishop',
          'bKnight', 'wKnight',
          'bPawn', 'wPawn']

def isValidChess(piece_pos):
  pp = deepcopy(piece_pos)
  bv_total = 0
  wv_total = 0

  if len(pp) > 32 or len(pp) < 2:
    return False
  elif 'wKing' not in pp.values() or 'bKing' not in pp.values():
    return False
  
  for k in pp.keys():
    if k[0] < '1' or k[0] > '8':
      return False
    elif ord(k[1]) > ord('h') or ord(k[1]) < ord('a'):
      return False

  n_pieces = {}
  
  for k in pieces:
    n_pieces[k] = 0

  for v in pp.values():
    n_pieces[v] += 1

  print()
  print(n_pieces)
  print()

  for k, v in n_pieces.items():
    if k[0] == 'w':
      match k:
        case 'wKing':
          if v > 1:
            return False
        case 'wQueen':
          if v > 9:
            return False
        case 'wBishop':
          if v > 10:
            return False
        case 'wRook':
          if v > 10:
            return False
        case 'wKnight':
          if v > 10:
            return False
        case 'wPawn':
          if v > 8:
            return False
      wv_total += v
      if wv_total > 16:
        return False
    else:
      match k:
        case 'bKing':
          if v > 1:
            return False
        case 'bQueen':
          if v > 9:
            return False
        case 'bBishop':
          if v > 10:
            return False
        case 'bRook':
          if v > 10:
            return False
        case 'bKnight':
          if v > 10:
            return False
        case 'bPawn':
          if v > 8:
            return False
      bv_total += v
      if bv_total > 16:
        return False
  return True

def r_pieces():
  p_pos = {}
  
  for i in range(randint(2,36)):
    r_int_str = str(randint(1, 9))
    r_char = chr(randint(ord('a'), ord('j')))
    p_pos[f'{r_int_str}{r_char}'] = choice(pieces)
  
  return p_pos


state = False
try:
  while state == False:
    # Randomly generate pieces and board locations
    p_pos = deepcopy(r_pieces())
    state = isValidChess(p_pos)
    print()
    print(p_pos)
    print()
    print(state)
    # sleep(1)
except KeyboardInterrupt:
  print("Exiting...")