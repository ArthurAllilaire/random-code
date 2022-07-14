import re
#Need to add after 100,000 start to lose PA at a rate of £1 for every £2 earned converted to basic rate

class Tax_Bracket:
  def __init__(self, tax_name=""):
    self.brackets = []
    self.tax_name = tax_name

  def add_bracket(self, line):
    # Tax brackets should be added in ascending order
    values = line.split(",")
    name = values[0]
    range = self.get_range(values[1])
    tax = float(str(re.search(r'[0-9]+', values[2]).group()))/100

    self.brackets.append([name,range, tax])

  def get_tax_amount(self, income, bracket):
    """
    Given an income and tax bracket calculates how much should be taxed for that bracket
    If returns False then bracket not applicable
    """
    lower, upper = bracket[1]
    #If no upper limit
    if upper < 0:
      upper = income + 1

    #Okay lets have a think
    taxable = income - upper
    #Larger income than upper limit
    if taxable >= 0:
      #Tax the full amount - range * tax
      return (upper - lower) * bracket[2]
    #income inbetween upper and lower 
    elif (income - lower) > 0:
      return (income - lower) * bracket[2]
    else:
      return False

  def calculate_tax(self, income):
    #Income is annual salary
    total = 0
    #Go through each bracket, calculate tax amount, then add total
    for bracket in self.brackets:
      tax = self.get_tax_amount(income, bracket)
      #If income lower than bracket
      if tax == False and bracket[2] !=0:
        return total
      else:
        total += tax

    return total

  def get_range(self, range):
    #Get all groups of numbers
    pattern = r'[0-9]+'
    nums = re.findall(pattern, range)
    
    #If only one number then other is inf
    if len(nums) == 1:
      return (float(nums[0]),-1)

    else:
      return (float(nums[0]), float(nums[1]))

  def get_marginal_tax(self, income):
    """
    
    """
    pass

  
  def __str__(self):
      return self.tax_name + str(self.brackets)




def get_taxes(filename):
  """
  Takes a filelocation (str) with file that has header as headings for 
  """
  taxes = {}
  with open(filename, 'r') as file:
    
    lines = file.readlines()
    #First line should be Headings for dict
    headings = lines[0].strip().split(",")
    tax_brackets = None
    #Skip the headings line
    for i in range(1,len(lines)):
      line = lines[i].strip()
      #ignore empty lines or comments
      if not line or line[0] == '#':
        continue
      #If not a dataline (shown by ,) 
      elif ',' not in line:
        tax_brackets = Tax_Bracket(line) # line is name of tax
        #Set new instance of Tax_bracket object in dict
        taxes[line] = tax_brackets
      else:
        tax_brackets.add_bracket(line)

  return taxes


def calc_tax(taxes, tax_type, income):
  """
  * @param: taxes -> Dictionary with tax_types as keys leading to Tax Brackets class instances
  * @param: tax_type -> Function assumes valid key for taxes
  * @param: income -> num
  """
  tax_brackets = taxes[tax_type]
  return tax_brackets.calculate_tax(income)


taxes = get_taxes("tax_calculator/tax_brackets.txt")


print(calc_tax(taxes, "INCOME TAX", 70000))
