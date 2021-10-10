class Player: 

    def __init__( self , grid ): 
        
        self.display = 'A'
        self.num_water_buckets = 0
        self.grid = grid 
        self.outOfGrid = False
        

        #Finding the starting cell and assigning that as the player's initial position.
        for m in range ( 0 , len( grid ) ):

               for n in range ( 0 , len( grid[ m ] )):

                   if( grid[ m ][ n ].display == 'X'):

                       self.row = m
                       self.col = n
                       self.newrow = m
                       self.newcol = n
                       break



    def add_water_buckets( self ):

        #increasing the number of water buckets the player has by 1.
        self.num_water_buckets += 1


    def move( self , move ):

        self.outOfGrid = False
        self.newrow = self.row
        self.newcol = self.col


        num_of_rows = len( self.grid )
        num_of_cols = len( self.grid [0] )
        

        #moving the player
        if (move == 'w' or move == 'W') :


            if( self.row-1 >= 0): #checking if the player is trying to move out of grid  
                self.newrow = self.row - 1
           
            else:   
                self.outOfGrid = True


        elif( move == 'a' or move == 'A' ):


            if( self.col-1 >= 0) : #checking if the player is trying to move out of grid
                self.newcol = self.col - 1
  
            else:
                self.outOfGrid = True


        elif( move == 's' or move == 'S' ):

            if( self.row +1 < num_of_rows ): #checking if the player is trying to move out of grid
                 self.newrow = self.row + 1

            else:
                self.outOfGrid=True


        elif( move == 'd' or move == 'D' ):


            if( self.col + 1 < num_of_cols): #checking if the player is trying to move out of grid
                self.newcol = self.col + 1
          
            else:
                self.outOfGrid = True
      

        else: # Move 'e' means wait. Hence there will be no change in the player's position.
            pass
