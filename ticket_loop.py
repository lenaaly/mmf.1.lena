# start of loop

# initialise loop so that it runs at least once

name = ""
count = 0
MAX_TICKETS = 5
seats_left = MAX_TICKETS

while name != "xxx" and count < MAX_TICKETS:

  # get details...
  name = input("Name: ")
  count += 1
  seats_left -= 1
  print ("You have ", seats_left, "tickets left")
