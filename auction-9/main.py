from replit import clear
from art import logo

print(logo)

auctionDict = {}
otherBidders = True

def highestBidd(my_bidds):
  highBidd = 0

  for name in my_bidds: 
    if my_bidds[name] > highBidd: 
      highBidd = my_bidds[name]
      winner = name
  print(f"The winner is {winner} with a bid of ${my_bidds[winner]}")


while otherBidders:

  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  auctionDict[name] = bid

  other = input("Are there any other bidders? Type 'yes' or 'no' ")

  if other != 'yes':
    otherBidders = False
  # clear the cosole 
  clear()
     
highestBidd(my_bidds=auctionDict)