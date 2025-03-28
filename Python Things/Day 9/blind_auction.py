logo = """

                         ___________
                                  /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\

"""

print(logo)

def user_input():
  username = str(input("What is your name? ==> "))
  bid_price = int(input("What is your bid price? ==> $"))
  return(username, bid_price)

def user_input_validator():
  response = input("Is there anyone else want to bid?\n Type 'Yes' or 'No' ").lower()

  while response != "yes" and response != "no":
    response = input("Incorrect input, type 'Yes' or 'No' only, please try again: ").lower()

  return response

  
username, bid_price = user_input()

# Add to dictionaries
bid = {username: bid_price}
print(bid)

# Add bidders
still_bidding = True

while still_bidding: 
  response = user_input_validator()

  # Bidding 
  if response == "yes":
    print("\n" * 50)
    username, bid_price = user_input()
    bid[username] = bid_price
    print(bid)
  elif response == "no": 
    print("\n" * 50)
    winner = max(bid, key=bid.get)
    print(f"The winner is {winner} with the bid of {bid[winner]}. Congratulations!")
    still_bidding = False
      
  # else: 
  #   print("Please input the correct command to continue bidding")
  #   response = input("Is there anyone else want to bid?\n Type 'Yes' or 'No' ").lower()
  #   still_bidding = response == "yes"
  #   username, bid_price = user_input()

# user_input = input("Enter yes/no: ")
# still_bidding = user_input.lower() == 'yes'