# import statements

# functions go here

# checks that ticket name not blank
def not_blank(question, error_message):
  valid = False
  
  while not valid:
    response = input(question)

    #if name not blank continue
    if response != "":
      return response

    #if name blank show error 
    else:
      print(error_message)


#''''''''''''' Main Routine ''''''''''''

# set up dictionaries / lists needed to hold data
# Ask user if they have used the program before and show instructions if nessesary
#loop to get ticket details

# get name (cant be blank)
name = not_blank("Name: ", 
                 "Sorry - this cant be blank,"
                "please enter your name")

# get age (between 12 and 130)
# calulate ticket price
# loop to ask for snacks
# calculate snack price

# ask for payment method (amd apply surcharge if necessary)

#calculate total sales and profit

#output data to text file



