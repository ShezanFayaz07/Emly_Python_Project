from TestMain import *

#Colors:
#---------------------------------------------
Red     =   '\033[31m'
Green   =   '\033[32m'
Yellow  =   '\033[33m'
Blue    =   '\033[34m'
Magenta =   '\033[35m'
Cyan    =   '\033[36m'
White   =   '\033[37m'

#Variables Used:
#---------------------------------------------
Player_Mood = ''
ReturnDicision = ['RETURN', 'R', 'r']


# Function used to ask playerDecision:

#___________________________________________________________________
def IsPlayerReady():
    global Player_Mood
    
    print(f"{Magenta}Do you want to start the Game---")
    Player_Mood = input(f"{Yellow}Y/N OR RETURN/R/r: {Green}")
#____________________________________________________________________
    

    

while(True):
    IsPlayerReady();
    
    if Player_Mood == 'Y' or Player_Mood == 'y':
        gameLoop()
        break
    
    if Player_Mood in ReturnDicision:
        exit()
        
        
print(White)