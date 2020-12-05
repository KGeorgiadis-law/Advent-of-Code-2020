from Day5boardingpasses import boarding_passes_raw

boarding_passes = boarding_passes_raw.split("\n")

def get_boarding_pass_id(boarding_pass):
  boarding_pass_chars = list(boarding_pass)

  # row calculation

  row = [0, 127]

  row_chars = boarding_pass_chars[:7]
  col_chars = boarding_pass_chars[-3:]

  for c in row_chars:

    mid_way = (row[0] + row[1]) / 2
    
    if c == 'F':
      row[1] = int(mid_way)
    if c == 'B':
      row[0] = round(mid_way)

    # # sanity check
    # print(c, row)

  row_id = row[0] if row_chars[-1] == "F" else row[1]

  # column calculation

  column = [0, 7]

  for c in col_chars:
    
    mid_way = (column[0] + column[1]) / 2
    
    if c == 'L':
      column[1] = int(mid_way)
    if c == 'R':
      column[0] = round(mid_way)

    # # sanity check
    # print(c, column)

  col_id = column[1] if col_chars[-1] == "R" else column[0]

  return row_id * 8 + col_id


def first_problem(boarding_passes):
  highest_id = 0
  for boarding_pass in boarding_passes:
    boarding_pass_id = get_boarding_pass_id(boarding_pass)
    if boarding_pass_id > highest_id:
      highest_id = boarding_pass_id

  return highest_id

def second_problem(boarding_passes):
  missing_ids = []
  
  all_ids = [get_boarding_pass_id(b) for b in boarding_passes]

  all_ids.sort()

  # sanity check
  # print(all_ids)

  for potential_id in range(all_ids[0], all_ids[-1]):
    if potential_id not in all_ids:
      if potential_id - 1 in all_ids and potential_id + 1 in all_ids:
        missing_ids.append(potential_id)
      # else:
      #   print(potential_id, potential_id + 1, potential_id - 1)

  return missing_ids

