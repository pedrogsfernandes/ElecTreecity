class Branch:
  def __init__(self, level, rotation):
    self.level = level # level determines initial height
    self.rotation = rotation # rotation of the branch axis relative to the tree axis
    self.servo1_rotation = 0 # min 0, max 90
    self.servo2_rotation = 0
    

  def rotate_1(self, rotation):
    if (self.servo1_rotation + rotation > 90):
      self.rotation = 90
    elif (self.servo1_rotation + rotation < 0):
      self.rotation = 0
    else:
      self.rotation += rotation
      

  def rotate_2(self, rotation):
    if (self.servo2_rotation + rotation > 180):
      self.rotation = 180
    elif (self.servo2_rotation + rotation < 0):
      self.rotation = 0
    else:
      self.rotation += rotation

  def get_leaf_relative_pos(self, level_height, arm_size):
    x = arm_size + cos(self.servo1_rotation) * armsize
    y = self.level * level_height + sin(self.servo1_rotation) * arm_size
    return x, y, self.rotation

  def get_leaf_tilt():
    #todo
    #use servo1 and servo2 rotation to calculate x and y tilt
    return None


class Tree:
  def __init__(self):
    self.level_height = 0.5 # interval between each level and between 1st level and ground
    self.arm_size = 0,5 # size in meters (each branch is composed of 2 arms, connected by a servo)

    #level 1
    self.branch_11 = Branch(1, 0)
    self.branch_12 = Branch(1, 120)
    self.branch_13 = Branch(1, 240)

    #level 2
    self.branch_21 = Branch(2, 0)
    self.branch_22 = Branch(2, 120)
    self.branch_23 = Branch(2, 240)

    #level 3
    self.branch_31 = Branch(3, 0)
    self.branch_32 = Branch(3, 120)
    self.branch_33 = Branch(3, 240)



  def get_enersy(self, branch):
    #todo
    #given:
      #branch position and tilt
      #sun position 
      #other branches' positions
      
    #get sun intensity hitting the solar panel

