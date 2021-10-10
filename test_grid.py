from grid import grid_to_string
from player import Player
from game_parser import read_lines



def test_grid_positive (): 


    """Testing the grid_to_string function. 
    
    Positive test cases.It is testing whether the grid_to_string
    function is returning the correct string representation of
    the grid and player or not for expected grid configuration.
    """



    file1 = "/home/unit_test_grids/test_grid.txt"
    grid = read_lines(file1)[0]
    my_player = Player(grid)


    result = grid_to_string(grid,my_player)
    expected_result = "*A***\n* W *\n*1  *\n*F 1*\n**  *\n**Y**\n\n"\
                     "You have 0 water buckets.\n"
    assert result == expected_result,"The grid_to_string function is not returning "\
                                   "the correct string representation of the grid "\
                                   "and player."


    #Updating the player attributes
    my_player.row = 2
    my_player.col = 2
    my_player.num_water_buckets = 3


    result = grid_to_string(grid,my_player)
    expected_result = "*X***\n* W *\n*1A *\n*F 1*\n**  *\n**Y**\n\n"\
                     "You have 3 water buckets.\n"
    assert result == expected_result,"The grid_to_string function is not returning "\
                                   "the correct string representation of the grid "\
                                   "and player."


    

def test_grid_edge():

    """Testing the grid_to_string function. 
    
    Edge test cases.It is testing whether the grid_to_string
    function is returning the correct string representation of
    the grid and player or not for edge case grid configurations.
    """

    file2 = "/home/unit_test_grids/test_grid2.txt"
    grid = read_lines(file2)[0]
    my_player = Player(grid)


    result = grid_to_string(grid,my_player)
    expected_result = "AY\n\nYou have 0 water buckets.\n"
    assert result == expected_result,"The grid_to_string function is not "\
                                   "returning the correct string representation "\
                                   "of the grid and player."

    
    file3 = "/home/unit_test_grids/test_grid3.txt"
    grid = read_lines(file3)[0]
    my_player = Player(grid)


    result = grid_to_string(grid,my_player)
    expected_result = "*\nA\nY\n*\n\nYou have 0 water buckets.\n"
    assert result == expected_result,"The grid_to_string function is not "\
                                   "returning the correct string representation "\
                                   "of the grid and player."
    

    file4 = "/home/unit_test_grids/test_grid4.txt"
    grid = read_lines(file4)[0]
    my_player = Player(grid)


    result = grid_to_string(grid,my_player)
    expected_result = "*AY*\n\nYou have 0 water buckets.\n"
    assert result == expected_result,"The grid_to_string function is not "\
                                    "returning the correct string representation "\
                                    "of the grid and player."




    
    
def run_tests():
    
    """Testing the grid_to_string function. 
    
    We are testing the positive and edge test cases.
    
    There are no possible negative test cases.
    Only valid grid and player is always passed to 
    this function as arguments.The validity of grid is
    handled by game_parser, which is tested in unit tests
    for game_parser in test_parser.py .
    
    """

    test_grid_positive() 
    test_grid_edge()

    print ( "Congratulations ! You passed all the"\
           " grid_to_string function tests. " )


