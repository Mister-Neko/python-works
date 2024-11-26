#! python
# mad_libs.py - Allow user to add own text anywhere ADJECTIVE, NOUN, ADVERB, or VERB appears in a text file. - v0.0.0

import re
from pyinputplus import inputStr
from os import getcwd

speech_parts = re.compile(r'((AD)?VERB)|(NOUN)|(ADJECTIVE)')
word = re.compile(r'(\w*\w[.?!,;:"\']?)')
sp_char = re.compile(r'\w*([.?!,;:"\'])')

def copy_text_file(fn):
  with open(f'{getcwd()}\\{fn}.txt', 'r') as fobj:
    t_text = fobj.read()

  return t_text

def save_text_file(fn, txt):
  with open(f'{getcwd()}\\{fn}.txt', 'w') as fobj:
    fobj.write(txt)
  print('Saved!')

file_name = inputStr(prompt='Enter file name to open: ')
txt = copy_text_file(file_name)

words = word.findall(txt)

for w in words:
  if (sp := speech_parts.match(w)):
    new_sp = inputStr(prompt=f'Enter in a {sp[0]}: ')
    if (punc := sp_char.match(w)):
      words[words.index(w)] = f'{new_sp}{punc[1]}'
    else:
      words[words.index(w)] = new_sp

txt = ' '.join(words)

print(txt)

file_name = inputStr(prompt='Enter file name to save as: ')
save_text_file(file_name, txt)