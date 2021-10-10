import sys
from game import Game
from grid import grid_to_string

 

# Checking whether enough number of command line arguments are provided or not
if ( len( sys.argv ) < 3 ):

    print( " Usage: python3 solver.py <filename> <mode>" )
    sys.exit( 0 )


#Moving the player in order to find the next node and game state.
def move ( node , this_game , this_move ):

    for pre_move in node [1] :
        this_game.move( pre_move )

    return this_game.move( this_move )


#Checking whether we have already visited that game state or not.
def check_visited ( result ) :

     for elem in visited :

        # result[0] denotes the game state- game configuration and player.
        if( elem == ( result[0] ) ):

            return True 

     return False



#Adding the node to the list of nodes. 
#Adding the game state to the list of visited game states. 

def add_node ( is_visited , result , this_move ) :
    
    if ( is_visited == False and result [2] == "continue" ):

                #adding the next node to node list and adding current node to visited
                next_node = [ node [0]+1 , node [1] + this_move ]

                nodes_list.append ( next_node )
                visited.append ( result [0] )

    if ( result [2] == "win" ):

                #Printing the path
                print ( "Path has {} moves.".format( node[0]+1 ) )

                i=0
                print ( "Path: ", end='' )

                while i < len ( node [1] ):
                    print ( node [1] [i] , end = ', ')
                    i += 1
 
                print ( this_move )
                sys.exit (0)



#Checking if the mode of search is BFS (Breadth First Search) or not
if ( sys.argv [2] == 'BFS' ):

    my_game = Game ( sys.argv [1] )
    nodes_list = [ [0,""] ]
    visited = [grid_to_string ( my_game.grid , my_game.my_player ) ]

    while True:

        if len ( nodes_list ) == 0:
            break


        node = nodes_list[ 0 ]
        nodes_list = nodes_list[ 1: ]
        moves = [ 'w' , 'a' , 's' , 'd' , 'e' ]


        for this_move in moves:

            #moving the player and finding the next node
            this_game = Game ( sys.argv [1] )

            result = move ( node , this_game , this_move )

            is_visited = check_visited ( result )

            add_node ( is_visited , result , this_move )


    print ( "There is no possible path." )



#Checking if the mode of search is DFS (Depth First Search) or not
elif ( sys.argv [2] == 'DFS' ): 

    my_game = Game ( sys.argv [1] )

    nodes_list = [ [0,""] ]
    visited = [ grid_to_string ( my_game.grid , my_game.my_player ) ]

    while True:

        if len ( nodes_list ) == 0:
            break

        node = nodes_list [ -1 ]
        nodes_list = nodes_list[ :-1 ]
        moves = [ 'w' , 'a' , 's' , 'd' , 'e' ]


        for this_move in moves:

            #moving the player and finding the next node
            this_game = Game ( sys.argv [1] )

            result = move( node , this_game , this_move )

            is_visited = check_visited ( result )

            add_node ( is_visited , result , this_move )


    print ( "There is no possible path." )


#Handling the situation when the user enters wrong search mode.
else:

    error_message =  " Usage: python3 solver.py <filename> <mode>" \
                     "Only 2 modes are possible. Input BFS for" \
                     " Breadth first search and DFS for Depth First Search"

    print(error_message)

