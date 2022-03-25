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

# initialise loop so that it runs at least once

name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
  print("You have {} seats " "left".format(MAX_TICKETS -count))

  # get details...
 
# get name (cant be blank)
  # get name (cant be blank)
  name = not_blank("Name: ", 
                 "Sorry - this cant be blank,"
                "please enter your name")

  count += 1
  print()

# tells user how many seats are left
if count == MAX_TICKETS:
  print("You have sold all the available tickets!")

# warns user that only one seat is left!
else:
  print("You have sold {} tickets.  \n"
       "There are {} places still available".format(count, MAX_TICKETS - count))

# get age (between 12 and 130)
# calulate ticket price
# loop to ask for snacks
# calculate snack price

# ask for payment method (amd apply surcharge if necessary)

#calculate total sales and profit

#output data to text file



