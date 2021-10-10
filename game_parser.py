import sys
from cells import (
     Start,
     End,
     Air,
     Wall,
     Fire,
     Water,
     Teleport
 )


def read_lines ( filename ):
        
     try:
         file = open ( filename , 'r' ) # Opening the file.
     except FileNotFoundError :
         return str( filename ) + " does not exist!"
         sys.exit(0)

     lines=[]


     # Reading lines from the file
     while True:
         line = file.readline()
         if ( line=='' ):
             break
         lines.append( line ) 


     file.close()


     grid = parse( lines )
     return [ grid , lines ]



def parse( lines ):
     
     valid_letters = { 'X':0 , 'Y':0 , '1':0 , '2':0 , '3':0 ,
                      '4':0 , '5':0 , '6':0 , '7':0 , '8':0 , '9':0 }


     grid = []
     i = 0
     while i < len( lines ):
         line = lines[i] # Extracting each line of the configuration file.
         line.strip
         grid_line = []
         

         j = 0
         length = len( lines[0] )-1
         while j < length:


             char = line[ j ] # Extracting each character in the configuration file.
             #Creating appropriate cell objects.
             if ( char == 'X' ):

                 grid_line.append( Start() )  #adding each cell to form a line of the grid.
                 valid_letters[ 'X' ] += 1

             elif( char == 'Y' ):

                 grid_line.append( End() )  #adding each cell to form a line of the grid.
                 valid_letters [ 'Y' ] += 1 

             elif(char == ' '):

                 grid_line.append( Air() )  #adding each cell to form a line of the grid.
             
             elif(char == '*'):

                 grid_line.append( Wall() )  #adding each cell to form a line of the grid.
             
             elif(char == 'F'):

                 grid_line.append( Fire() )  #adding each cell to form a line of the grid.
             
             elif(char == 'W'):

                 grid_line.append( Water() )  #adding each cell to form a line of the grid.
             
             elif( ord(char) > 48 and ord(char) <= 57):
                  #Checking if the character is a number
                 grid_line.append( Teleport(char) )  #adding each cell to form a line of the grid.
                 valid_letters[ char ] += 1
             
             else:
                 raise ValueError ( "Bad letter in configuration file: " 
                                   + char + "." )
             j += 1


         grid.append( grid_line ) # Adding every line to the grid. 
         i += 1


     if ( valid_letters [ 'X' ] != 1 ): #Checking if we the number of starting positions is not equal to one.
         
         raise ValueError ( "Expected 1 starting position, got "
                          + str ( valid_letters [ 'X' ] ) + "." )


     if ( valid_letters [ 'Y' ] != 1 ): #Checking if we the number of ending positions is not equal to one.
          
          raise ValueError ( "Expected 1 ending position, got "
                           + str ( valid_letters[ 'Y' ] ) + "." )



     for teleport_pads in range ( 1 , 10 ):
          
          if ( valid_letters [ str ( teleport_pads ) ] % 2 != 0 ): #Checking whether all teleport pads have an exclusively matching pad or not.
                
                 raise ValueError ( "Teleport pad " + str ( teleport_pads )
                                  + " does not have an exclusively matching pad." )
   
   
     return grid

