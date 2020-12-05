from Day3path import path

slopes = path.split("\n")

def down_ski(slopes, down, right):
  '''gets a list of slopes (strings made up of . and #) 
  Move through in a consistent pattern
  and count how many # you encounter.
  if you reach the end of the string, reset position
  '''
  current_location = 0
  current_height = 0
  tree_counter = 0

  while current_height < len(slopes) - 1:
    # stop counting when you reach the end
    current_height += down

    slope = list(slopes[current_height])

    for i in range(right):
      # reset if you reach end of slope
      if current_location >= len(slope) - 1:
        current_location = 0
      else:
        current_location += 1
    
    tree_checker = slope[current_location] == "#"

    if tree_checker:
      tree_counter += 1

    # # sanity check
    # slope[current_location] = "O"

    # slopes[current_height] = ''.join(slope)


  return (tree_counter)

  

def first_problem(slopes):

  return down_ski(slopes, 1, 3)

def second_problem(slopes):

  scenario_1 = down_ski(slopes, 1,1)
  scenario_2 = down_ski(slopes, 1,3)
  scenario_3 = down_ski(slopes, 1,5)
  scenario_4 = down_ski(slopes, 1,7)
  scenario_5 = down_ski(slopes, 2,1)

  return ( scenario_1 * scenario_2 * scenario_3 * scenario_4 * scenario_5 )