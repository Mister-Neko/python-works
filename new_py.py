#! python
# new_py.py - Quickly create new Python files. - v0.0.0

def new_py():
  print('What is the name of the program: ', end='')
  new_file_name = input()
  print('Describe what the program will do: ')
  program_des = input()
  new_py_txt = f'''#! python
# {new_file_name}.py - {program_des} - v0.0.0
'''
  f_obj = open(f'{new_file_name}.py', 'w')
  f_obj.write(f'{new_py_txt}')
  f_obj.close()

new_py()