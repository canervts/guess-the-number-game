from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess,answer,turns):
  if turns == 0:
    return "You lose"
  elif guess == answer:
    return "You win"
  elif guess > answer:
    return "Too high"
  elif answer > guess:
    return "Too low"

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'am thinking of a number between 1 and 100.")
answer = randint(1, 100)
guess = -1
print(f"Pssst, the correct answer is {answer}") 
level=input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == "easy":
  turns = EASY_LEVEL_TURNS
elif level == "hard":
  turns = HARD_LEVEL_TURNS

while guess != answer and turns != 0:
  print(f"You have {turns} attempts remaining to guess the number")
  turns -= 1
  guess=int(input("Make a guess: "))
  print(check_answer(guess,answer,turns))