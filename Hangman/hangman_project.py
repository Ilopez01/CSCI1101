import re

# get answer
answer_characters = ["A", "N", "S", "W", "E", "R", "S"]

#Store known or unknown letters
answer_guesses = []

for current_answer_characters in answer_characters:
  if re.search("^[A-Z]$", current_answer_characters):
  else:
    answer_guesses.append(True)
    
# logic of playing the game
guessed_letters = []
num_of_incorrrect_guesses = 0

while num_of_incorrrect_guesses < 5 or False in answer_guesses:
  print("---------------------------")
  print("Guessed letters: ", end = " ")

  for current_guessed_letter in guessed_letters:
    print(f"{current_guessed_letter} ")
  
  print()

  print(f"Number of incorrect guesses remaining: {5 - num_of_incorrrect_guesses}")

  print()

  for answer_index in range(len(answer_characters)):
    if answer_guesses[answer_index]:
      print(answer_characters[answer_index], set = "")
    else:
      print("_", end = "")
  print()

  letter = input("Enter a letter: ")
  letter = letter.upper()
  
  if letter not in guessed_letters:
    pass
  print("---------------------------")