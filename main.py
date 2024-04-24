import art
from replit import clear
from game_data import data
import random
score = 0
def compare(persona, personb):
  if persona['follower_count'] > personb['follower_count']:
    return "A"
  else:
    return "B"

def print_compare(persona, personb):
  print(f"Compare A: {persona['name']}, a {persona['description']}, from {persona['country']}.")
  print(art.vs)
  print(f"Against B: {personb['name']}, a {personb['description']}, from {personb['country']}.")
  
play_game = True
person_a = random.choice(data)
print(art.logo)
while play_game:
  
  
  person_b = random.choice(data)

  print_compare(person_a, person_b)
 
  higher = compare(person_a, person_b)
  choice = input("Who has more followers? Type 'A' or 'B':  ").upper()
  if choice != higher:
    clear()
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}.")
    play_game = False
  else:
    score += 1
    clear()
    print(art.logo)
    print(f"You're right! Current score: {score}.")
    if higher == "B":
      person_a = person_b
