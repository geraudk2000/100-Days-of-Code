#Step 1 
import random
from hangman_word import word_list
from hangman_art import stages, logo


print(logo)

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

lives = 6 
stopGame = False
display = []
letter_guess_before = ""
word = random.choice(word_list)
print(f"the chosen word is {word}") 

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
for x in range(len(word)):
    display.append("_")

while not stopGame:
  guess_letter = input("Guess a letter: ").lower()
  
  if guess_letter in letter_guess_before: 
    print("This letter was use before.")
  else:
    letter_guess_before += guess_letter
    print(f"You gess {guess_letter}")
    if guess_letter not in word:
      lives -= 1 


  #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in     the chosen_word.
  print(lives)
  print(stages[lives])
  
  for position in range(len(word)): 
    if word[position] == guess_letter:
      display[position] = guess_letter
  
  print(display)
  # if "_" in display and lives available then continue the game
  if "_" in display and lives > 0:
    stopGame = False
  else:  
    stopGame = True



if "_" in display:
  print("You loose, try again.")
else: 
  print("You win, Congratulations !!")
