from sys import exit

'''
Future challenge is to add a simple AI.

1. Create a two player game
2. Create a one player game
'''

b_pos = {
  "tl": " 1 ", "tm": " 2 ", "tr": " 3 ",
  "ml": " 4 ", "m": " 5 ", "mr": " 6 ",
  "bl": " 7 ", "bm": " 8 ", "br": " 9 "}

def p_board():
  print("\n{}|{}|{}".format(b_pos["tl"], b_pos["tm"], b_pos["tr"]))
  print("---|---|---")
  print("{}|{}|{}".format(b_pos["ml"], b_pos["m"], b_pos["mr"]))
  print("---|---|---")
  print("{}|{}|{}".format(b_pos["bl"], b_pos["bm"], b_pos["br"]))

def mod_board(piece):
  pos = None
  placed = False
  while placed == False:
    p_board()
    print(f"\n{piece}Select Board Position: ", end='')
    while pos == None:
      try:
        pos = int(input())
      except ValueError:
        print("\nNot a number...")
        pos = None
    match pos:
        case 1:
          b_pos["tl"] = piece
          placed = True
        case 2:
          b_pos["tm"] = piece
          placed = True
        case 3:
          b_pos["tr"] = piece
          placed = True
        case 4:
          b_pos["ml"] = piece
          placed = True
        case 5:
          b_pos["m"] = piece
          placed = True
        case 6:
          b_pos["mr"] = piece
          placed = True
        case 7:
          b_pos["bl"] = piece
          placed = True
        case 8:
          b_pos["bm"] = piece
          placed = True
        case 9:
          b_pos["br"] = piece
          placed = True
        case default:
          print("Not a board position")
  p_board()

def check_win(b_pos, peice):
  b = list(b_pos)
  for i in b:
    match i:
      case "tl":
        if b_pos[i] == peice:
          if b_pos["tm"] == peice and b_pos["tr"] == peice:
            return 0
          if b_pos["ml"] == peice and b_pos["bl"] == peice:
            return 0
          if b_pos["m"] == peice and b_pos["br"] == peice:
            return 0
      case "tm":
        if b_pos[i] == peice:
          if b_pos["m"] == peice and b_pos["bm"] == peice:
            return 0
      case "tr":
        if b_pos[i] == peice:
          if b_pos["mr"] == peice and b_pos["br"] == peice:
            return 0
          if b_pos["m"] == peice and b_pos["bl"] == peice:
            return 0
      case "ml":
        if b_pos[i] == peice:
          if b_pos["m"] == peice and b_pos["mr"] == peice:
            return 0
      case "bl":
        if b_pos[i] == peice:
          if b_pos["bm"] == peice and b_pos["br"] == peice:
            return 0
      case default:
        return 1

def game():
  move = 0
  piece = ' X '
  while move != 9:
    if piece == ' X ':
      mod_board(piece)
      if check_win(b_pos, piece) == 0:
        print("\nX Wins!!!")
        exit()
      piece = ' O '
    else:
      mod_board(piece)
      if check_win(b_pos, piece) == 0:
        print("\nO Wins!!!")
        exit()
      piece = ' X '
    move += 1

try:
  game()
except KeyboardInterrupt:
  print("Exiting...")
