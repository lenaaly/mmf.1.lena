# functions go here


def not_blank(question):
  valid = False
  
  while not valid:
    response = input(question)

    if response != "":
      return response
    
    else:
      print("Sorry - this cant be blank")

# main routine goes here
name = not_blank("Name: ")
      
      