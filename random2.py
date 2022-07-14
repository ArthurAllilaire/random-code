import re
def convert_to_digit(input):
  if input.isdigit():
    return int(input)
  return float(input)

calc = "1+77*2*4/2-4"
nums = re.findall('[0-9]+', calc)
operands = re.findall('[*/+-]', calc)
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

print(nums, operands, calcs, new_calcs, result[0])