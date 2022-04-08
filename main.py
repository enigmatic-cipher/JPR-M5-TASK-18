"""
Given an array of numbers as input, move the zeros to the end of the array. Note that the order of non-zero numbers should be the same. You cannot use any other array to solve it.
Input-> [2,0,4,0,6,8,0,0,10,12]
Output-> [2,4,6,8,10,12,0,0,0,0]
"""

def zero_to_end(arr, n):
  count = 0

  for i in range(n):
    if (arr[i] != 0):
      arr[count] = arr[i]
      count = count + 1
  while count < n:
    arr[count] = 0
    count = count + 1

ls = [2,0,4,0,6,8,0,0,10,12]
n = len(ls)
zero_to_end(ls, n)
print(ls)


