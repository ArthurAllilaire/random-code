from inspect import stack


numopen = 0
numclose = 0
input = "()()())" # ((0, 3), (1,2))

# we want a stack for the open brackets
# list1 = [8]
# list1.append(9)
# list1.append(10)

# print(list1.pop())
#get index 
# for open b's and add on the stack
# 
stack = []
for i in range(len(input)):
  char = input[i]
  print(char)
  if char == '(':
    stack.append(i)








# for char in input:
#   if char == ")":
#     numclose += 1
#   if char == "(":
#     numopen += 1
# if numopen == numclose:
#   print("YES")
# else:
#   print("NO")
  