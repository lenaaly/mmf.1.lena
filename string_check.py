def string_checker(question, choice):

  error = "please answer yes /no"

  valid = False
  while not valid:

    # ask question and put response in lowercase
    response = input (question).lower()

    if response in to_check:
      return response
    
    else:
      for item in to_check:
        if response == item[0]:
          return item
    print("please enter a valid option")