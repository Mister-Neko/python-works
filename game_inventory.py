inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inv):
  total_inv = 0
  print('Your inventory items:')
  for k, v in inv.items():
    print(f'\t{v} {k}')
    total_inv += v
  print(f'\tTotal number of items: {total_inv}')

display_inventory(inventory)