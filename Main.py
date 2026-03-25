from Gameloop import gameLoop
from CL_Colors import *


#Variables Used:
#---------------------------------------------
Player_Mood = ''
ReturnDicision = ['RETURN', 'R', 'r']


# Function used to ask playerDecision:

#___________________________________________________________________
def IsPlayerReady():
    global Player_Mood
    
    print(f"{Magenta}Do you want to start the Game---")
    Player_Mood = input(f"{Yellow}Y/N OR RETURN/R/r: {White}")
#____________________________________________________________________
    
#____________________________________________________________________
def showWelcomeAndRules():
    print(f"""{Cyan}
========================================
        HANGMAN (Single Player CLI)
========================================{White}

{Yellow}Welcome!{White}
Guess the secret word one letter at a time.

{Magenta}Rules:{White}
1. Enter only one letter (a-z) each turn.
2. Correct letter -> revealed in all positions.
3. Wrong letter -> attempts decrease by 1.
4. Repeated guess -> warning, no attempt loss.
5. You win if all letters are revealed.
6. You lose if attempts reach 0.
""")
    
    

while(True):
    showWelcomeAndRules()
    IsPlayerReady();
    
    #⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
    #Dev use only:
    if Player_Mood == 'mm1':
        exit(0)
    #⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
    
    if Player_Mood == 'Y' or Player_Mood == 'y':
        gameLoop()
        break
    
    if Player_Mood in ReturnDicision:
        exit(0)
        
        
print(White)