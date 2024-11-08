#! python
# p_table_org.py - Prints a list in an organized table manner - v0.0.0

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def find_longest(arr):
  longest = 0
  for l in arr:
    for w in l:
      if len(w) > longest:
        longest = len(w)
  return longest

org = find_longest(tableData)

for r in range(len(tableData[0])):
  for c in range(len(tableData)):
    print(tableData[c][r].rjust(org + 4),  end='')
  print()