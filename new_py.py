#! python
# new_py.py - Quickly create new Python files. - v0.0.0
from pyinputplus import inputInt

def new_py():
  print('What is the name of the program: ')
  new_file_name = input()
 
  file_ext = inputInt(prompt=f'Select file extension\n{' ' * 4}[1] .py\n{' ' * 4}[2] .pyw\n', blockRegexes=['[03-9]'])
  if file_ext == 1:
    ext = '.py'
  elif file_ext == 2:
    ext = '.pyw'
 
  print('Describe what the program will do: ')
  program_des = input()
  new_py_txt = f'''#! python
# {new_file_name}{ext} - {program_des} - v0.0.0
'''
  f_obj = open(f'{new_file_name}{ext}', 'w')
  f_obj.write(f'{new_py_txt}')
  f_obj.close()

new_py()