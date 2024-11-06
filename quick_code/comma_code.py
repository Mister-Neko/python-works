# items = ['apples',  'carrots', 'chicken', 'eggs', 'tissues']

items = ['dogs', 'cats', 'squirals']

def expand_list(items):
  t = type(list())
  if type(items) != t:
    print('error: type list not found')
  elif not items:
    print('List is empty...')
    return ''
  else:
    try:
      new_str = ''
      size = len(items)
      print('List of items:')
      print('  ', end='')
      for i in range(size):
        if i < size - 1:
          new_str += ('%s, ' %(items[i]))
        else:
          new_str += ('and %s.' %(items[i]))
      return new_str
    except IndexError:
      print('error: list empty or out of index range')

print(expand_list(items))