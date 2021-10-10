from game_parser import read_lines
from player import Player
from grid import grid_to_string
from game import Game
from cells import (
     Start,
     End,
     Air,
     Wall,
     Fire,
     Water,
     Teleport
 )



def test_start_constructor():

    """
    Testing the constructor of the 
    Start cell
    """

    start_cell=Start() 
    assert start_cell.display=='X' # Checking the display attribute of the constructor



def test_end_constructor():

    """
    Testing the constructor of the 
    End cell
    """

    end_cell=End() 
    assert end_cell.display=='Y' # Checking the display attribute of the constructor



def test_air_constructor():

    """
    Testing the constructor of the 
    Air cell
    """

    air_cell=Air() 
    assert air_cell.display==' ' # Checking the display attribute of the constructor



def test_wall_constructor():

    """
    Testing the constructor of the 
    Wall cell
    """

    wall_cell=Wall() 
    assert wall_cell.display=='*' # Checking the display attribute of the constructor



def test_water_constructor():

    """
    Testing the constructor of the 
    Water cell
    """

    water_cell=Water() 
    assert water_cell.display=='W' # Checking the display attribute of the constructor



def test_fire_constructor():

    """
    Testing the constructor of the 
    Fire cell
    """

    fire_cell=Fire() 
    assert fire_cell.display=='F' # Checking the display attribute of the constructor



def test_teleport_constructor():

    """
    Testing the constructor of the 
    Teleport cell
    """

    teleport_cell1=Teleport('1') 
    assert teleport_cell1.display=='1' # Checking the display attribute of the constructor


    teleport_cell2=Teleport('7') 
    assert teleport_cell2.display=='7' # Checking the display attribute of the constructor



def test_start_step():

    """ It tests the step function of the
    Start class.
    It tests whether the step function is returning the 
    correct list or not, where the first element of
    list represents the string representation of
    the grid and player.
    Second elements of list gives the additional move display
    message.
    Third element of list teels whether the player should continue 
    playing or not, or has the player tried to walk into wall, or
    has the player won or lost the game.

    """


    file1="/home/unit_test_grids/test_cells_grid.txt" 


    my_game=Game(file1)
    my_game.my_player.move('e') 


    start_cell=Start()
    result=start_cell.step(my_game)


    assert result[0]=="**A*\n*  *\n**Y*\n\nYou have 0 water buckets.\n","The step function is not returning"\
                                                                         "the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]=="","The step function is not returning"\
                         "the correct list. The second element of "\
                         "list is not the correct additional move  "\
                         "display message"
    
    
    assert result[2]=="continue","The step function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether "\
                                 "the player has won or lost, or whether the player"\
                                 "tried to walk into a wall"




def test_end_step():
    
    """ It tests the step function of the
    End class.
    It tests whether the step function is returning the 
    correct list or not, where the first element of
    list represents the string representation of
    the grid and player.
    Second elements of list gives the additional move display
    message.
    Third element of list teels whether the player should continue 
    playing or not, or has the player tried to walk into wall, or
    has the player won or lost the game.

    """


    file="/home/unit_test_grids/test_cells_grid2.txt"

    my_game=Game(file)
    my_game.move('s')

    end_cell=End()
    result=end_cell.step(my_game)


    expected_result1="\nYou conquer the treacherous maze set up by "\
                      "the Fire Nation and reclaim the Honourable Furious "\
                      "Forest Throne, restoring your hometown back to its "\
                      "former glory of rainbow and sunshine! Peace reigns over "\
                      "the lands.\n\n"\
                      "You made 1 move.\n"\
                      "Your move: s"\
                      "\n\n====================="\
                      "\n====== YOU WIN! ====="\
                      "\n====================="
  
   
    assert result[0]=="**X**\n**A**\n\nYou have 0 water buckets.\n\n","The step function is not returning"\
                                                                         " the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    
    assert result[1]==expected_result1,"The step function is not returning"\
                         "the correct list. The second element of "\
                         "list is not the correct additional move  "\
                         "display message"
    
    
    
    assert result[2]=="win","The step function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether "\
                                 "the player has won or lost, or whether the player"\
                                 "tried to walk into a wall"



def test_air_step():

    """ It tests the step function of the
    Air class.
    It tests whether the step function is returning the 
    correct list or not, where the first element of
    list represents the string representation of
    the grid and player.
    Second elements of list gives the additional move display
    message.
    Third element of list teels whether the player should continue 
    playing or not, or has the player tried to walk into wall, or
    has the player won or lost the game.

    """
    
    file1="/home/unit_test_grids/test_cells_grid.txt"
    
    my_game=Game(file1)
    my_game.my_player.move('s')
    
    air_cell=Air()
    result=air_cell.step(my_game)

    
    assert result[0]=="**X*\n* A*\n**Y*\n\nYou have 0 water buckets.\n","The step function is not returning"\
                                                                         "the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]=="","The step function is not returning"\
                         "the correct list. The second element of "\
                         "list is not the correct additional move  "\
                         "display message"
    
    
    assert result[2]=="continue","The step function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether "\
                                 "the player has won or lost, or whether the player"\
                                 "tried to walk into a wall"


def test_wall_step():
    
    
    """ It tests the step function of the
    Wall class.
    It tests whether the step function is returning the 
    correct list or not, where the first element of
    list represents the string representation of
    the grid and player.
    Second elements of list gives the additional move display
    message.
    Third element of list teels whether the player should continue 
    playing or not, or has the player tried to walk into wall, or
    has the player won or lost the game.

    """
    
    file1="/home/unit_test_grids/test_cells_grid.txt"
    
    my_game=Game(file1)
    my_game.my_player.move('d')
    
    
    wall_cell=Wall()
    result=wall_cell.step(my_game)

    
    assert result[0]=="**A*\n*  *\n**Y*\n\nYou have 0 water buckets.\n","The step function is not returning"\
                                                                         "the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]=="\nYou walked into a wall. Oof!\n","The step function is not returning"\
                                                         "the correct list. The second element of "\
                                                         "list is not the correct additional move  "\
                                                         "display message"
    
    
    assert result[2]=="wall","The step function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether "\
                                 "the player has won or lost, or whether the player"\
                                 "tried to walk into a wall"


def test_fire_step():
    
    """ It tests the step function of the
    Fire class.
    It tests whether the step function is returning the 
    correct list or not, where the first element of
    list represents the string representation of
    the grid and player.
    Second elements of list gives the additional move display
    message.
    Third element of list teels whether the player should continue 
    playing or not, or has the player tried to walk into wall, or
    has the player won or lost the game.

    """

    
    #Testing for the situation when the player does not has water buckets, so the player loses the game.
    file3="/home/unit_test_grids/test_cells_grid3.txt"
    my_game=Game(file3)
    my_game.move('s')
    fire_cell=Fire()
    result=fire_cell.step(my_game)
    
    
    expected_result1="\nYou step into the fires and watch your dreams disappear :(.\n\n"\
                     "The Fire Nation triumphs! The Honourable Furious Forest "\
                     "is reduced to a pile of ash and is scattered to the winds "\
                     "by the next storm... You have been roasted.\n\n"\
                     "You made 1 move .\n"\
                     "Your move: s\n\n"\
                     "=====================\n"\
                     "===== GAME OVER =====\n"\
                     "====================="
    
    
    assert result[0]=="**X*\n* A*\n**Y*\n\nYou have 0 water buckets.\n\n","The step function is not returning"\
                                                                         "the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]==expected_result1,"The step function is not returning"\
                                                         "the correct list. The second element of "\
                                                         "list is not the correct additional move  "\
                                                         "display message"
    
    
    assert result[2]=="lose","The step function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether "\
                                 "the player has won or lost, or whether the player"\
                                 "tried to walk into a wall"
    

    
    #Testing for the situation when the player does has water buckets, so the player survives the fire.
    file4="/home/unit_test_grids/test_cells_grid4.txt"
    
    my_game=Game(file4)
    my_game.my_player.num_water_buckets=1
    my_game.move('s')
    my_game.move('a')
    
    fire_cell=Fire()
    result=fire_cell.step(my_game)

    
    expected_result1="\nWith your strong acorn arms, "\
                    "you throw a water bucket at the fire. "\
                    "You acorn roll your way through "\
                    "the extinguished flames!\n"
    
    
    assert result[0]=="**X*\n*A *\n**Y*\n\nYou have 0 water buckets.\n","The step function is not returning"\
                                                                         " the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
   
   
    assert result[1]==expected_result1,"The step function is not returning"\
                                                         "the correct list. The second element of "\
                                                         "list is not the correct additional move  "\
                                                         "display message"
   
   
    assert result[2]=="continue","The step function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether "\
                                 "the player has won or lost, or whether the player"\
                                 "tried to walk into a wall"
    


def test_water_step():
    
    """ It tests the step function of the
    Water class.
    It tests whether the step function is returning the 
    correct list or not, where the first element of
    list represents the string representation of
    the grid and player.
    Second elements of list gives the additional move display
    message.
    Third element of list teels whether the player should continue 
    playing or not, or has the player tried to walk into wall, or
    has the player won or lost the game.

    """
    
    
    file4="/home/unit_test_grids/test_cells_grid4.txt"
    
    
    my_game=Game(file4)
    my_game.my_player.move('s')
    
    
    water_cell=Water()
    result=water_cell.step(my_game)
    
    
    expected_result1="\nThank the Honourable Furious Forest, "\
                     "you've found a bucket of water!\n"

    
    
    assert result[0]=="**X*\n*FA*\n**Y*\n\nYou have 1 water bucket.\n","The step function is not returning"\
                                                                         "the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]==expected_result1,"The step function is not returning"\
                         "the correct list. The second element of "\
                         "list is not the correct additional move  "\
                         "display message"
    
    
    assert result[2]=="continue","The step function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether "\
                                 "the player has won or lost, or whether the player"\
                                 "tried to walk into a wall"



def test_teleport_step():
   
   
    """ It tests the step function of the
    Teleport class.
    It tests whether the step function is returning the 
    correct list or not, where the first element of
    list represents the string representation of
    the grid and player.
    Second elements of list gives the additional move display
    message.
    Third element of list teels whether the player should continue 
    playing or not, or has the player tried to walk into wall, or
    has the player won or lost the game.

    """
    
    file5="/home/unit_test_grids/test_cells_grid5.txt"
    
    
    my_game=Game(file5)
    my_game.my_player.move('s')
    
    
    teleport_cell=Teleport('1')
    result=teleport_cell.step(my_game)
    
    
    expected_result1="\nWhoosh! The magical gates break Physics as we know"\
                     " it and opens a wormhole through space and time.\n"

    
    
    assert result[0]=="**X*\n* 1*\n* A*\n**Y*\n\nYou have 0 water buckets.\n","The step function is not returning"\
                                                                         " the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]==expected_result1,"The step function is not returning"\
                         "the correct list. The second element of "\
                         "list is not the correct additional move  "\
                         "display message"
    
    
    assert result[2]=="continue","The step function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether "\
                                 "the player has won or lost, or whether the player"\
                                 "tried to walk into a wall"




def run_tests():

    """ Testing all the cell classes.
     
     Testing the constructor of all the cell classes.

     Testing the step function of all the cell classes-

        It only tests the positive test cases.
        We do not have any negative test cases because only 
        valid moves are passed to player and game move.This 
        is handled by run.py, and is tested in e2e tests.

        The game configuration is also always valid.This is handled
        by game_parser.py. It is tested in unit tests for game_parser.py
        in test_parser.py   
        
        We do not have any edge test cases.
        The step function is called inside game move, after the player
        move has been called. The step function wraps up the move by
        finally updating player's position, number and list of moves.
        It returns the string representation of grid and player,
        the additional display message about the move, and 
        tells whether the player can continue or not, or whether
        the player has won or lost, or if thw player tried to walk into
        a wall.

        We have to pass the game object as arguments to the step function.
        It is not an independent unit test ,it depends on whether the
        game class is working correctly or not. As explained above, it
        wraps up the player move and returns the result. It depends
        on the functionality of other classes involved in our game.
  
     """
        
    test_start_constructor()
    test_start_step()
    test_end_constructor()
    test_end_step()
    test_air_constructor()
    test_air_step()
    test_wall_constructor()
    test_wall_step()
    test_fire_constructor()
    test_fire_step()
    test_water_constructor()
    test_water_step()
    test_teleport_constructor()
    test_teleport_step()
    print("Congratulations ! You passed all the cell class test cases.")


    


