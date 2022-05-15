def yes_no(question):

  error = "Please answer yes / no"

  valid = False
  while not valid:

    # ask question and put response in lowercase
    response = input(question).lower()

    if response == "yes" or response == "y":
      return "yes"
    elif response == "no" or response == "n":
      return "no"
    else:
      print(error)

# Main routine goes here

for item in range(0, 6):
  want_snacks = yes_no("Do you want snacks? ")
  print("Answer OK, you said:", want_snacks)
  print()


# string checking functions, takes in
# question and list of valid responses
def string_checker(question, to_check):

  valid = False
  while not valid:

    response = input(question).lower()

    if response in to_check:
      return response

    else:
      for item in to_check:
        # checks if response is the first letter of
        # an item in the list
        if response == item[0]:
          # note: returns the entire response
          # rather than just the first letter
          return item 

    print("sorry that is not a valid response")