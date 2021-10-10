import sys

def grid_to_string(grid,player):

    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    
    i = 0
    j = 0
    string_representation = ""

    while i < len(grid) : # Traversing through every list of cells of the grid.
        
        while j < len ( grid[i] ) : # Traversing through every cell in every list of cells of the grid. 
            
            if ( i == player.row and j == player.col ) : # Checking whether it is the position of the ACORN.
                
                string_representation += "A"
            
            else:
                
                string_representation += grid[i][j].display 
            
            j += 1
        
        string_representation += "\n"
        i += 1
        j = 0
    

    plural = ''
    if ( player.num_water_buckets > 1 or player.num_water_buckets == 0 ):
        plural = 's'
    

    # Adding the number of water buckets the player has , to the string representation.
    string_representation += "\nYou have {} water bucket{}.\n".format( player.num_water_buckets , plural ) 
    
    
    return string_representation

