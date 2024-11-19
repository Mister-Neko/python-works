#! python
# sandwichmaker.py - Make sandwich based on a series of selections and output the price total to make it. - v0.0.0

'''
Write a program that asks users for their sandwich preferences. The program
should use PyInputPlus to ensure that they enter valid input, such as:

* Using inputMenu() for a bread type: wheat, white, or sourdough.
* Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
* Using inputYesNo() to ask if they want cheese.
* If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
* Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
* Using inputInt() to ask how many sandwiches they want. Make sure this number
  is 1 or more.
Come up with prices for each of these options, and have your program display a
total cost after the user enters their selection.
'''

import re
from pyinputplus import inputMenu
from pyinputplus import inputYesNo
from pyinputplus import inputInt

def sandwich_total(num_sandwiches, sandwich, bread, protein, cheese):
  ns = num_sandwiches
  total = 0
  for k in sandwich:
    if k in bread:
      total += bread[k]
    elif k in protein:
      total += protein[k]
    elif k in cheese:
      total += cheese[k]
  total *= ns
  return total

bread = {'wheat': 1.25, 'white': 1.00, 'sourdough': 1.50}
protein = {'chicken': 1.25, 'beef': 1.50, 'pork': 1.00, 'fish': 2.00, 'ham': 1.00, 'turkey': 1.15, 'tofu': 1.75}
cheese = {'cheddar': 0.50, 'Swiss': 0.75, 'mozzarella': 0.85}

print('Welcome!')
binary_choice = inputYesNo('Would you like to purchase a sandwich? ')

if binary_choice[0] == 'n':
  print('Good bye.')
  exit(code=print('\nEnd program.'))
else:
  sandwich = []
  print('\nGreat!')
  sandwich.append(inputMenu(choices=list(bread), numbered=True, prompt='\nWhat type of bread would you like?\n'))
  sandwich.append(inputMenu(choices=list(protein), numbered=True, prompt='\nSelect your preferred protein:\n'))
  binary_choice = inputYesNo('\nDo you desire cheese with your sandwich? ')
  if binary_choice[0] == 'y':
    sandwich.append(inputMenu(choices=list(cheese), numbered=True, prompt='\nSelect your cheese:\n'))
  num_sandwiches = inputInt(prompt='\nHow many sandwiches of this combination would you like? ')
  sandwich_price = sandwich_total(num_sandwiches, sandwich, bread, protein, cheese)

if num_sandwiches < 2:
  if len(sandwich) > 2:
    print(f'Your {sandwich[0]}, {sandwich[1]}, and {sandwich[2]} sandwich will be ${sandwich_price:.2f}')
  else:
    print(f'Your {sandwich[0]} and {sandwich[1]} sandwich will be ${sandwich_price:.2f}')
else:
  if len(sandwich) > 2:
    print(f'Your {sandwich[0]}, {sandwich[1]}, and {sandwich[2]} sandwiches will be ${sandwich_price:.2f}')
  else:
    print(f'Your {sandwich[0]} and {sandwich[1]} will be ${sandwich_price:.2f}')

