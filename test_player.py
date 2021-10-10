from player import Player
from game_parser import read_lines

# Testing the player class

def test_constructor(): 

    """ Testing the constructor of the player class. 

        It is testing whether the default values of the player
        are correct or not.
        The initial value of the row and column position of the 
        player should be the position of the starting cell.

        It is testing whether the other attributes of the 
        player class have also been initialised correctly or not.      

    """
    

    file1="/home/unit_test_grids/test_player_grid.txt"
    my_player=Player(read_lines(file1)[0])
    
    
    
    assert my_player.display=='A',"The display attribute for "\
                                 "the player is not correct."
    
    
    assert my_player.row==0,"The row of the player is not"\
                           " correct in the constructor."
    
    
    assert my_player.col==1,"The col of the player is not "\
                             "correct in the constructor."
    
    
    assert my_player.newrow==0,"The default new row of the player"\
                             " is not correct in the constructor."
    
    
    assert my_player.newcol==1,"The default new col of the player is not"\
                                " correct in the constructor."
    
    
    assert my_player.num_water_buckets==0,"The number of water buckets the "\
                                   "player has is not correct in the constructor."
    
    
    assert my_player.outOfGrid==False,"The default state of player telling"\
                                    " whether player is trying to move out of "\
                                     "grid is not correct in the constructor."




def test_add_water_buckets():

    """Testing the add_water_buckets function of 
    the player class
    
    Testing whether the add_water_buckets function is
    increasing the number of water buckets successfully by 1
    or not."""

    filename="/home/unit_test_grids/test_player_grid.txt"
    
    
    my_player=Player(read_lines(filename)[0])
    my_player.add_water_buckets()

    
    assert my_player.num_water_buckets==1,"The add water buckets function"\
                                         "is not updating the number of"\
                                         "water buckets correctly."




def test_player_move_positive():

    """Testing the move function for the player class.
    
     Positive unit test case , to test the move function for all valid 
    moves in which the player does not tries to move out of bounds.
    It is testing whether the move assigns the new row and column
    coordinates of the player correctly or not. It also checks
    whether it is correctly identifying whether the player is trying
    to move out of bounds or not."""

    file1="/home/unit_test_grids/test_player_grid.txt"
    file2="/home/unit_test_grids/test_player_grid2.txt"


    #Testing move s.

    my_player=Player(read_lines(file1)[0])
    my_player.move('s')
    
    
    assert my_player.newrow==1,"The new row of the player is not "\
                               "updated correctly for move s."
    
    
    assert my_player.newcol==1,"The new column of the player is not "\
                               "updated correctly for move s."
    
    
    assert my_player.outOfGrid==False,"The state of the player telling "\
                               "whether player is trying to move out of grid"\
                               "is not updated correctly for move s."
    
    #Testing move e.

    my_player=Player(read_lines(file1)[0])
    my_player.move('e')
    
    
    assert my_player.newrow==0,"The new row of the player is not "\
                               "updated correctly for move e."
    
    
    assert my_player.newcol==1,"The new column of the player is not "\
                               "updated correctly for move e."
    
    
    assert my_player.outOfGrid==False,"The state of the player telling "\
                               "whether player is trying to move out of grid"\
                               "is not updated correctly for move e."

    #Testing move d.

    my_player=Player(read_lines(file1)[0])
    my_player.move('d')
    
    
    assert my_player.newrow==0,"The new row of the player is not "\
                                "updated correctly for move d."
    
             
    assert my_player.newcol==2,"The new column of the player is not "\
                               "updated correctly for move d."
    
    
    assert my_player.outOfGrid==False,"The state of the player telling "\
                               "whether player is trying to move out of grid"\
                               "is not updated correctly for move d."

    #Testing move a.

    my_player=Player(read_lines(file1)[0])
    my_player.move('a')
    
    
    assert my_player.newrow==0,"The new row of the player is not "\
                               "updated correctly for move a."
    
    
    assert my_player.newcol==0,"The new column of the player is not "\
                               "updated correctly for move a."
    
    
    assert my_player.outOfGrid==False,"The state of the player telling "\
                               "whether player is trying to move out of grid"\
                               "is not updated correctly for move a."  
    

    #Testing move w. 
    
    my_player=Player(read_lines(file2)[0])
    my_player.move('w')
    
    
    assert my_player.newrow==5,"The new row of the player is not "\
                               "updated correctly for move w."
    
    
    assert my_player.newcol==2,"The new column of the player is not "\
                               "updated correctly for move w."
    
    
    assert my_player.outOfGrid==False,"The state of the player telling "\
                               "whether player is trying to move out of grid"\
                               "is not updated correctly for move w."


def test_player_move_edge():

    """ Testing the move function for the player class.

    Edge unit test case, in which the player tries to 
    move out of bounds. It is testing this for all valid moves.
    It is testing whether the move function assigns the new row and column
    coordinates of the player correctly or not. It also checks
    whether it is correctly identifying whether the player is trying
    to move out of bounds or not."""


    file1="/home/unit_test_grids/test_player_grid.txt"
    file2="/home/unit_test_grids/test_player_grid2.txt"
    file3="/home/unit_test_grids/test_player_grid3.txt"
    file4="/home/unit_test_grids/test_player_grid4.txt"
    


    #Testing for move w. 
    my_player=Player(read_lines(file1)[0])
    my_player.move('w')
    
    
    assert my_player.newrow==0,"The new row of the player is not "\
                               "updated correctly for move w."
    
    
    assert my_player.newcol==1,"The new column of the player is not "\
                               "updated correctly for move w."
    
    
    assert my_player.outOfGrid==True,"The state of the player telling "\
                               "whether player is trying to move out of grid"\
                               "is not updated correctly for move w when the"\
                               "player is trying to do so."

    

    #Testing for move s.
    my_player=Player(read_lines(file2)[0])
    my_player.move('s')
    
    
    assert my_player.newrow==6,"The new row of the player is not "\
                               "updated correctly for move s."
    
    
    assert my_player.newcol==2,"The new column of the player is not "\
                               "updated correctly for move s."
    
    
    assert my_player.outOfGrid==True,"The state of the player telling "\
                               "whether player is trying to move out of grid"\
                               "is not updated correctly for move s when the"\
                               "player is trying to do so."                         
     
    

    #Testing for move a.
    my_player=Player(read_lines(file3)[0])
    my_player.move('a')
    
    
    assert my_player.newrow==1,"The new row of the player is not "\
                               "updated correctly for move a."
    
    
    assert my_player.newcol==0,"The new column of the player is not "\
                               "updated correctly for move a."
    
    
    assert my_player.outOfGrid==True,"The state of the player telling "\
                               "whether player is trying to move out of grid"\
                               "is not updated correctly for move a when the"\
                               "player is trying to do so."  
    
    

    #Testing for move d.
    my_player=Player(read_lines(file4)[0])
    my_player.move('d')
    
    
    assert my_player.newrow==2,"The new row of the player is not "\
                               "updated correctly for move d."
    
    
    assert my_player.newcol==4,"The new column of the player is not "\
                               "updated correctly for move d."
    
    
    assert my_player.outOfGrid==True,"The state of the player telling "\
                               "whether player is trying to move out of grid"\
                               "is not updated correctly for move d when the"\
                               "player is trying to do so."  

    #move e is wait.For move e, the player’s position does not changes.So with move 'e', player can not try to move out of bounds.

def run_tests():

    """ Testing the player class.
     
     Testing the constructor of the player class. 

     Testing the add_water_buckets function of 
     the player class

     Testing the move function of the player class-

        It tests only positive and edge test cases for the move function.
        It does not has any negative test cases because only the
        valid moves such 'w', 'a',' s', 'd' and 'e' will be passed to the 
        move function of the player.It will never receive any
        invalid move. This is handled by the run.py class. 
        This functionality has been tested in the e2e tests.  
        
 """
   
    test_constructor()
    test_add_water_buckets()
    test_player_move_positive()
    test_player_move_edge()
    
    print("Congratulations ! You passed all the"\
           " player class tests.")

