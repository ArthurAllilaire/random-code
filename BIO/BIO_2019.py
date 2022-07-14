#Requirements - 
# Contract - the number must be up to 20 digits
import math



def check_pali(pali):
  """
  Pali - is a string of numbers
  """
  i = 0
  j = len(pali) -1
  while i < j:
    if pali[i] != pali[j]:
      return False
    i += 1
    j -= 1
  return True


def pali_gen(number):
  """
  num is a string of numbers
  returns smallest palindromic number that is higher than the input
  """
  # 
  # Take the first half of the string - or 1 + if odd
  j = math.ceil(len(number) / 2)
  first_half = int(number[0:j])

  # increase it by 1
  first_half = str(1 + first_half)
  # Make the other side a palindrome
  j = math.floor(len(number) / 2)
  return first_half + first_half[j-1::-1]
  # REturn palindrome


"""
1b. 99999999999999999999 - 99999999998999999999 = 1000000000

1c. 


"""