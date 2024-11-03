if __name__ == "__main__":

 import random
while True:
     print("SELECT YOUR WEAPON (1-3)")
     print("--------------------------")
     print("\n 1. Rock \n 2. Paper \n 3. Scissors")
     weapon = int(input("Enter your Weapon: "))
     
     if weapon == 1:
          weapon_name = 'Rock'
     elif weapon == 2:
          weapon_name = 'Paper'
     else:
          weapon_name = 'Scissors'
    
     comp_weapon = random.randint(1,3)

     if comp_weapon == 1: 
            comp_weapon_name = 'Rock'
     elif comp_weapon == 2:
         comp_weapon_name = 'Paper'
     else:
         comp_weapon_name = 'Scissors'
     if weapon == comp_weapon:
          result = "DRAW"
     elif (weapon == 1 and comp_weapon ==2) or (weapon ==1 and comp_weapon == 2):
          result = 'Paper covers rock'
     elif (weapon == 1 and comp_weapon ==3) or (weapon ==1 and comp_weapon == 3): 
          result = 'Rock crushes scissors'
     elif (weapon == 2 and comp_weapon ==3) or (weapon ==2 and comp_weapon == 3):
          result = 'Scissors slices paper'

     if result == "DRAW":
          print("It's a tie!")
     elif result == weapon_name:
          print(("You win,"),result,('!')) 
     else:
          print(("You lose,"), result, ("!"))
     response = input("Want to play again? (y/n): ")
     if response.lower() != 'y':
          break
print("--------------------------")
print("Completed by, Hector Maldonado")