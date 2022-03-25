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








name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
  print("You have {} seats " "left".format(MAX_TICKETS -count))

  # get details...
# get name (cant be blank)
   # get name (cant be blank)
  name = not_blank("Name: ", 
                    "sorry - this cant be blank."
                   "Please enter your name")
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

  count += 1
    
# tells user how many seats are left
if count == MAX_TICKETS:
  print("You have sold all the available tickets!")

# warns user that only one seat is left!
else:
  print("You have sold {} tickets.  \n"
       "There are {} places still available".format(count, MAX_TICKETS - count))


  
  
# calulate ticket price
# loop to ask for snacks
# calculate snack price

# ask for payment method (amd apply surcharge if necessary)

#calculate total sales and profit

#output data to text file



