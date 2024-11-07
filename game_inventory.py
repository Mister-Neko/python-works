inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
orc_loot = ['gold coin', 'short sword', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inv):
  total_inv = 0
  print('Your inventory items:')
  for k, v in inv.items():
    print(f'\t{v} {k}')
    total_inv += v
  print()
  print(f'\tTotal number of items: {total_inv}')

def add_to_inv(inv, loot):
  for k in loot:
    if k in inv:
      inv[k] += 1
    else:
      inv[k] = 1

add_to_inv(inventory, orc_loot)
display_inventory(inventory)

