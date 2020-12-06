from Day6customsAnswers import customs_answers_raw

customs_answers = customs_answers_raw.split("\n\n")

def first_problem(customs_answers):

  customs_answers = [set(c.replace("\n", "")) for c in customs_answers]

  sum = 0
  for group in customs_answers:
    sum += len(group)
  return sum

def second_problem(customs_answers):

  group_answers =[c.split("\n") for c in customs_answers]

  # with thanks to https://stackoverflow.com/a/17182670
  from string import ascii_lowercase

  total_sum = 0

  for group in group_answers:  
    sum = 0
    for char in ascii_lowercase:
      relevant_answers = [p for p in group if char in p]

      # print(group, char, relevant_answers)

      if len(relevant_answers) == len(group):
        sum += 1

    total_sum += sum

    # print(total_sum)

  return total_sum