
from replit import clear
from art import logo
import random

def select_card(): 
  """ Returns a random cards """
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)


def calculate_score(cards):
  """Take a list of cards and calculate the score"""
  #check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  # if the score is already over 21, remove the 11 and replace it with a 1.
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw game"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "Win with a blakjack"
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Opponent went over. You win"
  else:
    return "You loose"



print(logo)

def play_game():
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(select_card())
    computer_cards.append(select_card())
  
  while not is_game_over: 
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f" You cards: {user_cards}, current score {user_score}")
    print(f" Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_continue = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_continue == "y":
        user_cards.append(select_card())
      else:
        is_game_over = True
    
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(select_card())
    computer_score = calculate_score(computer_cards)
  
  print(f" Your final hand: {user_cards}, final score: {user_score}")
  print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play game of Blackjack? Type 'y' or 'n' ").lower() == 'y':
  clear()
  print(logo)
  play_game()
  