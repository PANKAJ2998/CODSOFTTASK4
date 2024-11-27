


import random as r

while True:
    print("\nWelcome to the Rock, Paper, Scissors game!\n")
    
  
    a = input("Choose one (Rock, Paper, Scissors): ").capitalize()
    b = ["Rock", "Paper", "Scissors"]
    

    c = r.randint(0, 2) 
    print("Computer chooses:", b[c])
    
    if a not in b:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
    elif (b[c] == 'Rock' and a == 'Scissors') or \
         (b[c] == 'Scissors' and a == 'Paper') or \
         (b[c] == 'Paper' and a == 'Rock'):
        print("Computer Won\n")
    elif b[c] == a:
        print("It's a Draw!")
    else:
        print("You Won!\n")
    
    d = input("Do you want to continue? (y/n): ").lower()
    if d == 'n':
        print("Thanks for playing! Goodbye!")
        break


