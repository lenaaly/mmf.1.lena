# function goes here

def int_check(question):

  error = "Please enter a whole number between {} " \
  "and {}".format(low_num, high_num)
  
  valid = False
  while not valid:

    # ask user for number and check it is valid
    try:
      response = int(input(question))

      if response <= 0:
        print(error)
      else:
        return response

    except ValueError:
      print(error)

# main routine goes here
age = int_check("Age: ", 12, 130)