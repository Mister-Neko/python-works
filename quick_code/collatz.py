from sys import exit

def collatz():
  print('Enter a number: ', end='')
  num = int(input())
  
  try:
    while num > 1:
      if(num % 2 == 0):
        num //= 2
      else:
        num *= 3
        num += 1
      
      print(num)
  
  except KeyboardInterrupt:
    print('Exiting...')
    exit()

collatz()