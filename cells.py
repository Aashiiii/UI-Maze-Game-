import sys
from grid import grid_to_string

class Start:

    def __init__( self ):
        self.display = 'X'

    def step(self , my_game):

        my_player = my_game.my_player
        #updating the player's position
        my_player.row = my_player.newrow
        my_player.col = my_player.newcol

        return [ grid_to_string( my_player.grid , my_player ) , "" , "continue" ] #player can continue playing



class End:

    def __init__(self):
        self.display = 'Y'

    def step(self , my_game ):

        my_player = my_game.my_player

        #updating the player's position
        my_player.row = my_player.newrow
        my_player.col = my_player.newcol

        result1 = grid_to_string ( my_player.grid , my_player ) + "\n"

        #player has won the game
        result = "\nYou conquer the treacherous maze set up" \
               " by the Fire Nation and reclaim the Honourable " \
               "Furious Forest Throne, restoring your hometown" \
               " back to its former glory of rainbow and sunshine!" \
               " Peace reigns over the lands.\n"
        
        listmoves = my_game.listOfMoves
        numbermoves = my_game.numberOfMoves
        
        #number of moves made by player
        plural=''
        if( numbermoves > 1 ):
            plural = 's'
        result += "\nYou made {} move{}.\n".format( numbermoves , plural )
        
        #list of moves made by player
        plural=''
        if ( len (listmoves) > 1):
            plural = 's'
        result += "Your move{}: ".format( plural )
        i=0
        while i < len(listmoves) -1 :
            result += str( listmoves[i] ) + ', '
            i+=1
        result+=str(listmoves [len(listmoves) -1]) + "\n"

        #Adding winning message to result.
        result+= "\n=====================\n" \
                 "====== YOU WIN! =====\n" \
                 "====================="
        return [result1 , result , "win"] 

class Air:

    def __init__(self):
        self.display = ' '

    def step(self,my_game):
        my_player = my_game.my_player

        #updating the player's position
        my_player.row = my_player.newrow
        my_player.col = my_player.newcol

        return [ grid_to_string( my_player.grid , my_player ), "" , "continue" ] #player can continue playing



class Wall:

    def __init__(self):
        self.display = '*'

    def step ( self, my_game ):
        my_player = my_game.my_player

        #Removing the last move from list of moves because it wont be counted as the player waled into a wall.
        my_game.listOfMoves = my_game.listOfMoves [0 : len(my_game.listOfMoves)-1]
        #Reducing the number of moves
        my_game.numberOfMoves -= 1

        result1 = grid_to_string( my_player.grid , my_player )
        result = "\nYou walked into a wall. Oof!\n"
        return [result1 , result , "wall"] #player tried to walk into a wall


class Fire:

   def __init__(self):
        self.display = 'F'

   def step( self , my_game ):
        my_player = my_game.my_player

        #updating the player's position
        my_player.row = my_player.newrow
        my_player.col = my_player.newcol
         
        #checking if player has water bucket to survive the fire.
        if( my_player.num_water_buckets > 0):

            #player has water buckets to survive.
            my_player.num_water_buckets -= 1
            my_player.grid [ my_player.newrow ][ my_player.newcol ] = Air()

            result1 = grid_to_string(my_player.grid , my_player)
            result="\nWith your strong acorn arms, " \
                    "you throw a water bucket at the fire. "\
                    "You acorn roll your way through "\
                    "the extinguished flames!\n"
            return [ result1 , result , "continue" ] #player can continue playing

        else:

            #player lost the game.
            result1 = grid_to_string (my_player.grid , my_player) + "\n"
            result = "\nYou step into the fires and watch " \
                    "your dreams disappear :(.\n" \
                    "\nThe Fire Nation triumphs! The Honourable " \
                    "Furious Forest is reduced to a pile of ash " \
                    "and is scattered to the winds by the next storm... " \
                    "You have been roasted.\n"
            
            listmoves = my_game.listOfMoves
            numbermoves = my_game.numberOfMoves
            
            #number of moves made by player
            plural = ' '
            if ( numbermoves > 1):
                plural = 's'
            result += "\nYou made {} move{}.\n".format( numbermoves , plural )
        
            #list of moves made by player
            plural = ''
            if( len(listmoves) > 1):
                plural = 's'
            result += "Your move{}: ".format( plural )
            i=0
            while i < len(listmoves)-1 :
                 result += str(listmoves[i]) + ', '
                 i += 1
            result += str( listmoves[ len( listmoves)-1]) + "\n"


            #Adding Game Over message to result.
            result += "\n=====================\n" \
                        "===== GAME OVER =====\n" \
                        "====================="
            return [ result1 , result , "lose" ]#player has lost the game


class Water:

    def __init__(self):
        self.display = 'W'

    def step( self , my_game ):
        my_player = my_game.my_player

        #updating the player's position
        my_player.row = my_player.newrow
        my_player.col = my_player.newcol
        
        #increasing the number of water buckets that player has by 1.
        my_player.add_water_buckets()

        #changing the water cell to air after player collected the water bucket
        my_player.grid [ my_player.row ][ my_player.col ] = Air()

        result1 = grid_to_string( my_player.grid , my_player )
        result = "\nThank the Honourable Furious Forest, " \
                 "you've found a bucket of water!\n"

        return [ result1 , result , "continue" ]#player can continue playing


class Teleport:
    
    def __init__( self , display ):
        self.valid = True
        self.display = display

    def step( self , my_game ):
        my_player = my_game.my_player

        #updating the player's position
        my_player.row = my_player.newrow
        my_player.col = my_player.newcol

        #Teleporting the player from one teleport pad to another
        flag = 0
        for i in range ( 0  , len(my_player.grid ) ):
            for j in range ( 0 , len(my_player.grid [0])-1 ):

                if( my_player.grid [i][j].display == self.display and
                  ( my_player.row != i or my_player.col != j ) and
                   flag == 0): #checking if the cell is a matching teleport pad on which the player isn’t already standing.

                    my_player.row = i
                    my_player.col = j
                    flag = 1 #To make sure that player is only teleported once.

        result1 = grid_to_string( my_player.grid , my_player )
        
        #player has been teleported
        result = "\nWhoosh! The magical gates break Physics as we know" \
                 " it and opens a wormhole through space and time.\n"
               
        return [ result1 , result , "continue" ] #player can continue playing



