profit = 0

name = ""
while name != "xxx":

  name = input("Name: ")
  # replace with function call


  if name == "xxx":
    break

  age = int(input("Age:  ")) # replace with function

  if age < 16:
    ticket_price = 7.5
  elif age < 65:
    ticket_price = 10.5
  else:
    ticket_price = 6.5

  profit_made = ticket_price -5
  profit += profit_made

  print("{} : ${:.2f}".format(name, ticket_price))

print("Profit from tickets: ${:.2f}".format(profit))