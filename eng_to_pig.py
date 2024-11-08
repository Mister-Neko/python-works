#! python
# eng_to_pig - Convert English to Pig Latin - v0.0.0

print('Enter the English message to translate into Pig Latin:')
eng = input()

VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

pig = []

# if starts with vowel add yay to the end
# otherwise move the first letter to the end of the word followed by ay

for word in eng.split():
  i = 0
  while not word[i].isalnum() and i < (len(word) - 1):
    i += 1
  if i == (len(word) - 1):
    pig.append(word)
    continue
  else:
    i = 0

  s_punc = ''
  e_punc = ''

  while not word[0].isalnum() and not word[-1].isalnum() or i != len(word):
    i += 1
    if not word[0].isalnum():
      s_punc += word[0]
      word = word[1:]
        
    if not word[-1].isalnum():
      e_punc += word[-1]
      word = word[0:-1]

  if word[0].lower() in VOWELS:
    if s_punc != '' and e_punc != '':
      pig.append(s_punc + word + 'yay' + e_punc)
    elif s_punc != '':
      pig.append(s_punc + word + 'yay')
    elif e_punc != '':
      pig.append(word + 'yay' + e_punc)
    else:
      pig.append(word + 'yay')
  elif word[0].isalpha():
    w_case = []
    if word[0].isupper() and not word.isupper():
      for i in range(len(word)):
        if word[i].isupper():
          w_case.append(1)
        else:
          w_case.append(0)
    end = word[0]
    word = word[1:] + end
    if len(w_case) > 0:
      for i in range(len(w_case)):
        if w_case[i] == 1:
          if i == 0:
            word = word[i].upper() + word[i + 1:]
          elif i < len(w_case):
            word = word[0:i] + word[i].upper() + word[i + 1:]
          else:
            word = word[0:i] + word[i].upper()
        else:
          if i == 0:
            word = word[i].lower() + word[i + 1:]
          elif i < len(w_case):
            word = word[0:i] + word[i].lower() + word[i + 1:]
          else:
            word = word[0:i] + word[i].lower()
    if s_punc != '' and e_punc != '':
      pig.append(s_punc + word + 'ay' + e_punc)
    elif s_punc != '':
      pig.append(s_punc + word + 'ay')
    elif e_punc != '':
      pig.append(word + 'ay' + e_punc)
    else:
      pig.append(word + 'ay')
  else:
    pig.append()


pig = ' '.join(pig)

print(f'\n{pig}\n')