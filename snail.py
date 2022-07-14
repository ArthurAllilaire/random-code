import numpy as np
class Directions:
  # It needs to be able to keep track of the current direction, then swith to the next direction
  def __init__(self, directions = [
      np.array([[1],[0]]),
      np.array([[0],[1]]),
      np.array([[-1],[0]]),
      np.array([[0],[-1]])
    ], start = 0):
    """The directions optional parameter is list of direction vectors, start is parameter to specify the index of the starting directions"""
    self.index = start
    self.directions = directions
    self.current = self.directions[self.index]
  def turn(self, diff = 1):
    self.index += diff
    self.current = self.directions[self.index%(len(self.directions))]
    print(self.current)

  def get_d(self):
    return self.current

class Snail:
  def __init__(self, x, y, grid, start_d = 0):
    #In a 3x3 grid bottom right has coords: (2,2)
    # have a vector position
    self.pos = np.array([[x],[y]])
    self.grid = grid
    self.visited = []
    self.bounds = {
      "x": [0,len(self.grid[0])], 
      "y":[0,len(self.grid)]
    }
    
    #Vector displacement - starts by going right by default
    self.d = Directions(start = start_d)

  def out_of_bounds(self, pos):
    """Pos is position vector of proposed new position"""
    #If out of any of the bounds return true
    var = pos[0] < self.bounds["x"][0] or pos[0] >= self.bounds["x"][1] or pos[1] < self.bounds["y"][0] or pos[1] >= self.bounds["y"][1]
    print("Out of bounds: ", var)
    print(self.bounds)
    return var

  def update_bounds(self, pos):
    # We should be at one of the boundaries - that one needs to be reduced by 1 or increased by 1 to make it smaller.
    # could have more than one to change
    #The problem is that the bounds should  
    if pos[0] == self.bounds["x"][0]:
      self.bounds["x"][0] += 1
    if pos[0] == self.bounds["x"][1]:
      self.bounds["x"][1] -= 1
    if pos[1] == self.bounds["y"][0]:
      self.bounds["y"][0] += 1
    if pos[1] == self.bounds["y"][1]:
      self.bounds["y"][1] -= 1

  
  def forward(self):
    """Return True if the action is successful otherwise false"""
    print("proposed", self.pos + self.d.get_d())
    if not self.out_of_bounds(self.pos + self.d.get_d()):
      self.pos += self.d.get_d()
      self.visited.append(self.get_square(self.pos))
      print(True)
      return True   
    else:
      self.d.turn()
      self.update_bounds(self.pos)
      print(False)
      return False
  
  def get_visited(self):
    return self.visited

  def get_square(self, pos):
    print(pos, self.bounds)
    return self.grid[pos[1][0]][pos[0][0]]

  def go_explore(self):
    #Add starting square to visited
    self.visited.append(self.get_square(self.pos))
    while True:
      #If the snail tries to turn more than once unsuccessfully it has run out of options
      if self.forward() == False and self.forward() == False:
        break

def snail(snail_map):
    mo = Snail(0,0,snail_map)
    mo.go_explore()
    return mo.get_visited()


array = [[1,2,3],
            [4,5,6],
            [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
print(snail(array), expected)