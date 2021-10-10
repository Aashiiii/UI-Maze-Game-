from game_parser import read_lines
from player import Player
from grid import grid_to_string
import sys

class Game:

    def __init__( self , filename ):
        self.filename = filename
        self.grid = read_lines( self.filename )[0]

        #checking whether readlines() function was able to open the file or not
        if ( isinstance( self.grid , list )): #if list then we were able to find and open the file successfully 
            self.my_player = Player( self.grid )
        else:
            self.error_message = read_lines( self.filename )
            self.my_player = None
            
        self.listOfMoves = []
        self.numberOfMoves = 0


    def move( self, move ):

       if(self.my_player == None):
           return 
           
       self.my_player.move( move )
       
       #Checking whether the player tried to move out of bounds
       if(self.my_player.outOfGrid == False): #If false then player didn’t try to move out of bounds
  
           self.numberOfMoves += 1
           self.listOfMoves.append( move.lower() )
           my_cell = self.grid [ self.my_player.newrow ][ self.my_player.newcol ]
           result = my_cell.step( self )
           
           return [ result[0] , result[1] , result[2] ]

       else:

           result1 = grid_to_string( self.grid , self.my_player )
           result2 = "\nYou walked into a wall. Oof!\n"  #It will act as a wall if player tried to move out of bounds
          
           return [ result1 , result2 , "wall" ]
