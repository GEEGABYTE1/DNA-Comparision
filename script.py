dna_1 = "ACCGTT"
dna_2 = "CCAGCA"

def longest_common_subsequence(string_1, string_2):
  print("Finding longest common subsequence of {0} and {1}".format(string_1, string_2))
  inner_list = len(string_1) + 1
  outer_list = len(string_2) + 1
  grid = [[0 for i in range(inner_list)] for j in range(outer_list)]
  for row in range(1, len(string_2) + 1):
    print("Comparing: {z}".format(z=string_2[row - 1]))
    for col in range(1, len(string_1) + 1):
      print("Against: {z}".format(z=string_1[col - 1]))
      if string_1[col - 1] == string_2[row - 1]:
        grid[row][col] = grid[row - 1][col - 1] + 1
      else:
        grid[row][col] = max(grid[row - 1][col], grid[row][col - 1])
  
  bottom_right_cell = grid[-1][-1]
  result = []
  row = -1 
  col = -1 
  while row != len(grid) and col != len(grid):
      try:
        if string_2[row] == string_1[col]:
            result.append(string_2[row])
            row -= 1
            col -= 1
            
        else:
            if grid[row - 1][row] > grid[row][col - 1]:
                    row -= 1

            else:
                    col -= 1
      except IndexError:
          result.reverse()
          string = "".join(result)
          return string


    
  





print(longest_common_subsequence(dna_1, dna_2))