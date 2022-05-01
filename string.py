
def yes_no(question):

  error = "please answer yes /no"

  valid = False
  while not valid:

    # ask question and put response in lowercase
    response = input (question).lower()

    if response == "yes" or response == "y":
      return "yes"
    elif response == "no" or response == "n":
      return "no"
    else:
      print(error)