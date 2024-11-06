birthdays = {'Matt': '31Oct', 'Yoshiko': '22Dec', 'Betty': '28Oct'}

while True:
  print('Enter a name: (blank to quit): ', end='')
  name = input()
  if name =='':
    break

  if name in birthdays:
    print(birthdays[name] + " is the birthday of " + name)
  else:
    print("I don not have birthday information for " + name)
    print("What is their birthday?")
    bday = input()
    birthdays[name] = bday
    print("Birthday database updated.")