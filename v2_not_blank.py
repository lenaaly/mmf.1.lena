# functions go here


def not_blank(question, error_message):
  valid = False
  
  while not valid:
    response = input(question)

    if response != "":
      return response
    
    else:
      print(error_message)

# main routine goes here
name = not_blank("Name: ", 
                 "Sorry - this cant be blank,"
                "please enter your name")

      