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

# checks for an integer between two variables




# checks for integer more than 0
def int_check(question):

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










# ******************* Main Routine ********************
  
# set up dictionaries / lists needed to hold data

# ask user if they have used the program before and show instructions
      
      
# loop to get ticket details
# start of loop
      
# initialise loop so that it runs at least once

# '''''''''''''''' Main Routine ''''''''''''

# set up dictionaries / lists need to hold data

# ask user if they used the program before & show instructions




MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0



while name != "xxx" and ticket_count < MAX_TICKETS:

  # tells user how many seats are left
  if ticket_count < MAX_TICKETS - 1:
    print("You have {} seats " 
          "left".format(MAX_TICKETS -ticket_count))

  # warns user that only one seat is left!
  else:
    print("*** There us ONE seat left!!***")

    
  # get details...
    
   # get name (cant be blank)
  name = not_blank("Name: ")
  
  # end the loop if the exit code is entered
  if name == "xxx":
    break
  

    
  # get age (between 12 and 130)
  age = int_check("Age: ")

  # check age is valid
  if age < 12:
    print("Sorry you are too young for this movie")
    continue
  elif age > 130:
    print("That is very old - it looks like a mistake")
    continue

  if age < 16:
    ticket_price = 7.5
  elif age < 65:
    ticket_price = 10.5
  else:
    ticket_price = 6.5

  ticket_count += 1
  ticket_sales += ticket_price
    

# end of ticket loop 

# calculate ticket profit...
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))


# tells user how many seats are left
if ticket_count < MAX_TICKETS - 1:
  print("You have sold all the available tickets!")

# warns user that only one seat is left!
else:
  print("You have sold {} tickets.  \n"
       "There are {} places still available".format(ticket_count, MAX_TICKETS - ticket_count))
# calulate ticket price
# loop to ask for snacks
# calculate snack price

# ask for payment method (amd apply surcharge if necessary)

#calculate total sales and profit

#output data to text file



