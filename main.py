from art import logo
print(logo)

from replit import clear
bid_log = {}

another_bidder = "yes" #to allow a continuation of code until there are no more bidders (with while loop)
while another_bidder == "yes": 
  name = input("What is your name?: ") #key
  bid = int(input("What is your bid?: £")) #value as a int
  another_bidder = input("Are there any other bidders? Type 'yes' or 'no'.")

#adding names and bids to bid_log (dictionary)
  bid_log[name] = bid
  print(bid_log)

if another_bidder == "yes":
  clear()
else:
  clear()

#checking the bid_log for the highest bid
def highest_bidder(bid_log):
  highest_bid = 0
  for bidder in bid_log:
    bid_amount = bid_log[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner}, they won with a bid of £{highest_bid}")
highest_bidder(bid_log)