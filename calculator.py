import re
#calculation = input("Please input your calculation:")
#(7+(10*2))/3
#Parse the string left to right - this is recursive
#First find the deepest inner bracket
#Evaluate it
#Replace bracket with result
#Evaluate larger bracket
#Repeat till no more brackets
#Solve the remaining equations
def convert_to_digit(input):
  if input.isdigit():
    return int(input)
  return float(input)

def bracketer(input):
  stack = []
  # an ordered list of tuples of the smallest pairs
  pairs = []
  for i in range(len(input)):
    char = input[i]
    if char == "(":
      stack.append(i)
    elif char == ")":
      pairs.append((stack.pop(),i))
  return pairs

def get_bracket(input):
  print(input)
  stack = []
  # an ordered list of tuples of the smallest pairs
  for i in range(len(input)):
    char = input[i]
    if char == "(":
      stack.append(i)
    elif char == ")":
      return((stack.pop(),i))

def calculate(calc):
  #Passed in a string without any brackets, calculates the number and returns it
  print(calc)
  nums = re.findall('[0-9.]+', calc)
  operands = re.findall('[*/+-]', calc)

  #If the calc is just a number return it
  if len(operands) == 0:
    return convert_to_digit(calc)

  calcs = []
  for i in range(len(nums)-1):
    calcs.append(convert_to_digit(nums[i]))
    calcs.append(operands[i])
  # Append the last number
  calcs.append(convert_to_digit(nums[-1]))

  new_calcs = []
  skip = False
  for i in range(len(calcs)):
    if skip:
      skip = False
      continue
    num = calcs[i]
    if num == "*":
      #The last number that was appended
      new_calcs.append(new_calcs.pop() * calcs[i+1])
      skip = True
    elif num == "/":
      #The last number that was appended
      new_calcs.append(new_calcs.pop() / calcs[i+1])
      skip = True 
    else:
      new_calcs.append(num)

  result = []
  for i in range(len(new_calcs)):
    if skip:
      skip = False
      continue
    num = new_calcs[i]
    if num == "+":
      #The last number that was appended
      result.append(result.pop() + new_calcs[i+1])
      skip = True
    elif num == "-":
      #The last number that was appended
      result.append(result.pop() - new_calcs[i+1])
      skip = True
    else:
      result.append(num)

  return result[0]

#Calculate tests:


def evaluate(calc):
  #Solve this recursively
  #Have a function that gets the first pair of brackets
  #Solve it and replace in the string
  #Pass new string through evaluate again
  bracket = get_bracket(calc)
  if not bracket:
    return calculate(calc)
  
  num = evaluate(calc[bracket[0]+1:bracket[1]])
  # If in front of the bracket there was a number add a minus sign, unless its the first bracket
  if (calc[bracket[0]-1].isdigit() or calc[bracket[0]-1] == ")") and bracket[0] != 0:
    num = "*"+ str(num)
  new_calc = calc[:bracket[0]] + str(num) + calc[bracket[1]+1:]

  return evaluate(new_calc)

  # for pair in pairs:
  #   # Get the first pair and solve
  #   num = evaluate(calc[pair[0]+1:pair[1]])
  #   new_calc = calc[:pair[0]+1] + str(num) + calc[pair[1]:]
  #   print(new_calc)


  # return pairs
print(calculate("4*1.0"))
print(evaluate("(1+77)*2(4(4/2-1))"))

#For () break them into their own calculations
# calculations = calculation.split("(")
# for i in nums:

#   total += int(i)
# print(total)
