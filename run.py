from game import Game
from grid import grid_to_string
import os
import sys


if ( len( sys.argv ) <= 1 ):

    print ( "Usage: python3 run.py <filename> [play]" ) #Telling the player how command line arguments should be placed
    sys.exit (0)


my_game = Game ( sys.argv[1] )#creating our game



#checking whether we were able to open the configuration file or not.

if ( my_game.my_player != None ):#If none then we weren’t  able to find and open the configuration file successfully 
    
    print ( grid_to_string ( my_game.grid , my_game.my_player ) )#printing the game configuration and player

else:
   
    print ( my_game.error_message )#printing error message for FileNotFound error
    sys.exit (0)


clear = False

if ( len ( sys.argv ) > 2 ):
    
    if ( sys.argv [2] == "play" ):#checking whether player wants to clear screen after every move or not
      
       clear = True


while True:
    
    move = input ( "Input a move: " )

    valid_moves = ['w','a','s','d','e','W','A','S','D','E']
    
    if (clear == True ):
        
        os.system ('clear')

    if ( move == 'q' or move == 'Q'):
        
        print ( "\nBye!" )
        sys.exit (0)

    elif move in valid_moves: #checking whether move is valid or not
        
        result = my_game.move ( move )
        print ( result [0] + result [1] ) #printing game configuration and player
         
        if ( result[2] == "win" or result [2] == "lose" ): #checking if the player won or lost the game 
            sys.exit (0)
            
    else:
       
        print( grid_to_string ( my_game.grid , my_game.my_player ))
        print( "Please enter a valid move (w, a, s, d, e, q).\n" )

