from Day4passports import passports_raw

import re

# using regex to split by newline OR by space
passports = [re.split("[\s\n]", p) for p in passports_raw.split("\n\n")]

def first_problem(passports):
  '''check if passports are valid
  a passport is valid if it has either 8 elements OR
  it has 7 elements AND the field missing is CID
  return number of VALID passports
  '''
  valid_passports_number = 0
  
  for passport in passports:

    passport_dict = {}

    for field in passport:
      key, value = field.split(":")
      passport_dict[key] = value

    if len(passport) == 8:
      valid_passports_number += 1
    elif len(passport) == 7 and "cid" not in passport_dict:
      valid_passports_number += 1

  return (valid_passports_number) 


def field_checker(key, value):
  '''receive a key and value
    and check if they are valid according to the rules
    initial check made via regex, then extra rules with if
    returns boolean
  '''
  # dictionary with the key, regex pattern to apply to it
  rules = {
    'byr': "^\d{4}$",
    'iyr': "^\d{4}$",
    'eyr': "^\d{4}$",
    'hgt': "^\d{2,3}(in|cm)$",
    'hcl': "^#[0-9a-f]{6}$",
    'ecl' : "^(amb|blu|brn|gry|grn|hzl|oth)$",
    'pid': "^\d{9}$",
    'cid': ".*"
  }

  is_valid = False

  if re.match(rules[key], value):
    # apply extra rules if field is one of the below
    if key in ['byr', 'iyr', 'eyr', 'hgt']:
      if key == 'byr' and int(value) >= 1920 and int(value) <= 2002:
        is_valid = True
      elif key == "iyr" and int(value) >= 2010 and int(value) <= 2020:
        is_valid = True
      elif key == "eyr" and int(value) >= 2020 and int(value) <= 2030:
        is_valid = True
      elif key == "hgt":
        if value[-2:] == "cm" and int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
          is_valid = True
        elif value[-2:] == "in" and int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
          is_valid = True
    else:
      is_valid = True

  return is_valid

def second_problem(passports):

  valid_passports_number = 0
  
  for passport in passports:

    passport_dict = {}

    valid_fields = 0

    for field in passport:
      key, value = field.split(":")
      passport_dict[key] = value
      if field_checker(key, value):
        valid_fields += 1

    if len(passport) == 8 & valid_fields == 8:
      valid_passports_number += 1
    elif len(passport) == 7 and "cid" not in passport_dict and valid_fields == 7:
      valid_passports_number += 1

  return (valid_passports_number)