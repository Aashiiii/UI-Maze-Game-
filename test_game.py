from game import Game

def test_constructor_positive():



    """ Testing the constructor of the game class. 

        It is testing whether the attributes of the 
        game class have been initialised correctly or not.  

        In the positive case, the configuration file exists,
        and our player's row and column should be initialised
        with the position of the start cell. 

        It is not testing the grid attribute of the game class
        because it has been tested in unit tests for read_lines
        function of game_parser.py in test_parser.py  

    """


    file1="/home/unit_test_grids/test_game_grid.txt"
    my_game=Game(file1)
    
    assert my_game.filename==file1,"The filename is not correct "\
                                     "in the constructor."
    
    
    assert my_game.listOfMoves==[],"The list of moves is not correct "\
                                 "in the constructor."
    
    
    assert my_game.numberOfMoves==0,"The number of moves is not correct "\
                                  "in the constructor."
    
    
    assert my_game.my_player.row==0,"The constructor is not creating the my_player"\
                                    " object correctly.The row attribute of my_player "\
                                    " object is not initialised correctly."
    
    
    assert my_game.my_player.col==1,"The constructor is not creating the my_player"\
                                    " object correctly.The column attribute (col) of my_player "\
                                    " object is not initialised correctly."
    
    
    assert my_game.my_player.num_water_buckets==0,"The constructor is not creating the my_player"\
                                                  " object correctly.The number of water buckets"\
                                                  " attribute (num_water_buckets) of my_player "\
                                                  " object is not initialised correctly."



def test_constructor_negative():

    """ Testing the constructor of the game class. 

        It is testing whether the attributes of the 
        game class have been initialised correctly or not.  

        In the negative case, the configuration file does not
        exists,our player object for the game should be None.

        It is not testing the grid attribute of the game class
        because it has already been tested in unit tests for 
        read_lines function of game_parser.py in test_parser.py  

    """

    file1="/home/unit_test_grids/test_game_grids.txt"
    my_game=Game(file1)
    
    
    assert my_game.filename==file1,"The filename is not correct "\
                                     "in the constructor."
    
    
    assert my_game.listOfMoves==[],"The list of moves is not correct "\
                                 "in the constructor."
    
    
    assert my_game.numberOfMoves==0,"The number of moves is not correct "\
                                  "in the constructor."
    
    
    assert my_game.my_player==None,"The constructor is not creating"\
                                   "the correct player object when the"\
                                   "Configuration file does not exists."




def test_game_move_positive():

    """Testing the move function for the game class.
    
    Positive unit test case , to test the move function for all valid 
    moves in which the player does not tries to move out of bounds.
    It is testing whether the move function returns the correct
    result or not.
    
    The game move first moves the player, and then calls the step
    function of that cell.The result of move function of game
    depends on move function of player.Hence it not purely a 
    unit test.The move function of player is tested in test_player.py

    The move function manipualtes the list returned by step function 
    of cells. The correctness of move function also depends on whether 
    the step function is correct or not. This is further tested in 
    test_cells.py
    
    """


    file1="/home/unit_test_grids/test_game_grid.txt"
    file2="/home/unit_test_grids/test_game_grid2.txt"
    file3="/home/unit_test_grids/test_game_grid3.txt"
    file4="/home/unit_test_grids/test_game_grid4.txt"

    # Testing for move 's'.
    my_game=Game(file1)
    
    
    result=my_game.move('s')
    
    
    assert my_game.listOfMoves==['s'],"The list of moves is not updated "\
                                    "correctly after the player moves."
    
    
    assert my_game.numberOfMoves==1,"The number of moves is not updated "\
                                  "correctly after the player moves."  
    
    
    assert result[0]=="*X**\n*A *\n**Y*\n\nYou have 0 water buckets.\n","The move function is not returning"\
                                                                         "the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]=="","The move function is not returning"\
                         "the correct list. The second element of "\
                         "list is not the correct additional move  "\
                         "message"
    
    
    assert result[2]=="continue","The move function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether"\
                                 "the player has won or lost."

    
    
    # Testing for move 'd'.
    my_game=Game(file2)
    
    
    result=my_game.move('d')
    
    
    assert my_game.listOfMoves==['d'],"The list of moves is not updated "\
                                    "correctly after the player moves."
    
    
    assert my_game.numberOfMoves==1,"The number of moves is not updated "\
                                  "correctly after the player moves."  
    
    
    assert result[0]=="****\nXA *\n**Y*\n\nYou have 0 water buckets.\n","The move function is not returning"\
                                                                         "the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]=="","The move function is not returning"\
                         "the correct list. The second element of "\
                         "list is not the correct additional move  "\
                         "message"
    
    
    assert result[2]=="continue","The move function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether"\
                                 "the player has won or lost."


    
    
    # Testing for move 'a'.
    my_game=Game(file3)
    
    
    result=my_game.move('w')
    
    
    assert my_game.listOfMoves==['w'],"The list of moves is not updated "\
                                    "correctly after the player moves."
    
    
    assert my_game.numberOfMoves==1,"The number of moves is not updated "\
                                  "correctly after the player moves."  
    
    
    assert result[0]=="****\n* AY\n**X*\n\nYou have 0 water buckets.\n","The move function is not returning"\
                                                                         "the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]=="","The move function is not returning"\
                         "the correct list. The second element of "\
                         "list is not the correct additional move  "\
                         "message"
    
    
    assert result[2]=="continue","The move function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether"\
                                 "the player has won or lost."

    
    
    # Testing for move 'a'.
    my_game=Game(file4)
    
    
    result=my_game.move('a')
    
    
    assert my_game.listOfMoves==['a'],"The list of moves is not updated "\
                                    "correctly after the player moves."
    
    
    assert my_game.numberOfMoves==1,"The number of moves is not updated "\
                                  "correctly after the player moves."  
    
    
    assert result[0]=="****\n* AX\n*Y**\n\nYou have 0 water buckets.\n","The move function is not returning"\
                                                                         "the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]=="","The move function is not returning"\
                         "the correct list. The second element of "\
                         "list is not the correct additional move  "\
                         "message"
    
    
    assert result[2]=="continue","The move function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether"\
                                 "the player has won or lost."



    # Testing for move 'e'.
    my_game=Game(file2)
    
    result=my_game.move('e')
    
    
    assert my_game.listOfMoves==['e'],"The list of moves is not updated "\
                                    "correctly after the player moves."
    
    
    assert my_game.numberOfMoves==1,"The number of moves is not updated "\
                                  "correctly after the player moves."  
    
    
    assert result[0]=="****\nA  *\n**Y*\n\nYou have 0 water buckets.\n","The move function is not returning"\
                                                                         "the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]=="","The move function is not returning"\
                         "the correct list. The second element of "\
                         "list is not the correct additional move  "\
                         "message"
    
    
    assert result[2]=="continue","The move function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether"\
                                 "the player has won or lost."




def test_game_move_negative():
    """ Testing the move function for the game class.
    
    Negative unit test case. In the negative case, the configuration 
    file does not exists,our player object for the game should be None.
    The game move should not return anything in this case.

    """

    file="/home/unit_test_grids/test_game_grids.txt"
    my_game=Game(file)
    
    result=my_game.move('s')
    
    assert my_game.listOfMoves==[],"The move function of game is changing "\
                                  "the initial list of moves when the"\
                                  "configuration file does not exists"
    
    
    assert my_game.numberOfMoves==0,"The move function of game is changing "\
                                  "the initial number of moves when the"\
                                  "configuration file does not exists"
    
    
    assert result==None,"The move function is not working"\
                        "correctly when the configuration "\
                        "file does not exists"
                                




def test_game_move_edge():

    """ Testing the move function for the player class.

    Edge unit test case, in which the player tries to 
    move out of bounds,or tries to walk into a wall. It 
    is testing this for all possible valid moves.
    It is testing whether the move function returns the correct
    result in these edge cases or not."""
    

    file1="/home/unit_test_grids/test_game_grid.txt"
    file2="/home/unit_test_grids/test_game_grid2.txt"
    file3="/home/unit_test_grids/test_game_grid3.txt"
    file4="/home/unit_test_grids/test_game_grid4.txt"


    #When the player walks into a wall

    #Testing for move 'd' when the player tries to walk into a wall.
    my_game=Game(file1)
    
    
    result=my_game.move('d')
    
    
    assert my_game.listOfMoves==[],"The move function of game is changing "\
                                   "the initial list of moves when the"\
                                  "player tries to walk into a wall."
    
    
    assert my_game.numberOfMoves==0,"The move function of game is changing "\
                                  "the initial number of moves when the"\
                                  "player tries to walk into a wall."
    
    
    assert result[0]=="*A**\n*  *\n**Y*\n\nYou have 0 water buckets.\n","The move function is not returning"\
                                                                         "the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]=="\nYou walked into a wall. Oof!\n","The move function is not returning"\
                                                         "the correct list. The second element of "\
                                                         "list is not the correct additional move  "\
                                                         "message"
    
    
    assert result[2]=="wall","The move function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether "\
                                 "the player has won or lost, or whether the player"\
                                 "tried to walk into a wall"

    
    
    #Testing for move 'a' when the player tries to walk into a wall.
    my_game=Game(file1)
    
    
    result=my_game.move('a')
    
    
    assert my_game.listOfMoves==[],"The move function of game is changing "\
                                  "the initial list of moves when the"\
                                  "player tries to walk into a wall."
    
    
    assert my_game.numberOfMoves==0,"The move function of game is changing "\
                                  "the initial number of moves when the"\
                                  "player tries to walk into a wall."
    
    
    assert result[0]=="*A**\n*  *\n**Y*\n\nYou have 0 water buckets.\n","The move function is not returning"\
                                                                         "the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]=="\nYou walked into a wall. Oof!\n","The move function is not returning"\
                                                         "the correct list. The second element of "\
                                                         "list is not the correct additional move  "\
                                                         "message"
    
    
    assert result[2]=="wall","The move function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether "\
                                 "the player has won or lost, or whether the player"\
                                 "tried to walk into a wall"


    #Testing for move 'w' when the player tries to walk into a wall.
    my_game=Game(file2)
    
    
    result=my_game.move('w')
    
    
    assert my_game.listOfMoves==[],"The move function of game is changing "\
                                  "the initial list of moves when the"\
                                  "player tries to walk into a wall."
    
    
    assert my_game.numberOfMoves==0,"The move function of game is changing "\
                                  "the initial number of moves when the"\
                                  "player tries to walk into a wall."
    
    
    assert result[0]=="****\nA  *\n**Y*\n\nYou have 0 water buckets.\n","The move function is not returning"\
                                                                         "the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]=="\nYou walked into a wall. Oof!\n","The move function is not returning"\
                                                         "the correct list. The second element of "\
                                                         "list is not the correct additional move  "\
                                                         "message"
    
    
    
    assert result[2]=="wall","The move function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether "\
                                 "the player has won or lost, or whether the player"\
                                 "tried to walk into a wall"

    
    
    
    #Testing for move 's' when the player tries to walk into a wall.
    my_game=Game(file2)
    
    
    
    result=my_game.move('s')
    
    
    assert my_game.listOfMoves==[],"The move function of game is changing "\
                                  "the initial list of moves when the"\
                                  "player tries to walk into a wall."
    
    
    assert my_game.numberOfMoves==0,"The move function of game is changing "\
                                  "the initial number of moves when the"\
                                  "player tries to walk into a wall."
    
    
    assert result[0]=="****\nA  *\n**Y*\n\nYou have 0 water buckets.\n","The move function is not returning"\
                                                                         "the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]=="\nYou walked into a wall. Oof!\n","The move function is not returning"\
                                                         "the correct list. The second element of "\
                                                         "list is not the correct additional move  "\
                                                         "message"
    
    
    assert result[2]=="wall","The move function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether "\
                                 "the player has won or lost, or whether the player"\
                                 "tried to walk into a wall"



    #move e is wait.For move e, the player’s position does not changes.So with move 'e', player can not try to move out of bounds.

    # When the player tries to walk out of bounds.


    #Testing for move 'w' when the player tries to walk out of bounds.
    my_game=Game(file1)
    
    
    result=my_game.move('w')
    
    
    assert my_game.listOfMoves==[],"The move function of game is changing "\
                                  "the initial list of moves when the"\
                                  "player tries to walk into a wall."
    
    
    assert my_game.numberOfMoves==0,"The move function of game is changing "\
                                  "the initial number of moves when the"\
                                  "player tries to walk into a wall."
    
    
    assert result[0]=="*A**\n*  *\n**Y*\n\nYou have 0 water buckets.\n","The move function is not returning"\
                                                                         "the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]=="\nYou walked into a wall. Oof!\n","The move function is not returning"\
                                                         "the correct list. The second element of "\
                                                         "list is not the correct additional move  "\
                                                         "message"
    
    
    assert result[2]=="wall","The move function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether "\
                                 "the player has won or lost, or whether the player"\
                                 "tried to walk into a wall"

    
    
    #Testing for move 'a' when the player tries to walk out of bounds.
    my_game=Game(file2)
    
    
    result=my_game.move('a')
    
    
    assert my_game.listOfMoves==[],"The move function of game is changing "\
                                  "the initial list of moves when the"\
                                  "player tries to walk into a wall."
    
    
    assert my_game.numberOfMoves==0,"The move function of game is changing "\
                                  "the initial number of moves when the"\
                                  "player tries to walk into a wall."
    
    
    assert result[0]=="****\nA  *\n**Y*\n\nYou have 0 water buckets.\n","The move function is not returning"\
                                                                         "the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]=="\nYou walked into a wall. Oof!\n","The move function is not returning"\
                                                         "the correct list. The second element of "\
                                                         "list is not the correct additional move  "\
                                                         "message"
    
    
    assert result[2]=="wall","The move function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether "\
                                 "the player has won or lost, or whether the player"\
                                 "tried to walk into a wall"


    
    
    #Testing for move 's' when the player tries to walk out of bounds.
    my_game=Game(file3)
    
    
    result=my_game.move('s')
    
    
    assert my_game.listOfMoves==[],"The move function of game is changing "\
                                  "the initial list of moves when the"\
                                  "player tries to walk into a wall."
    
    
    assert my_game.numberOfMoves==0,"The move function of game is changing "\
                                  "the initial number of moves when the"\
                                  "player tries to walk into a wall."
    
    
    assert result[0]=="****\n*  Y\n**A*\n\nYou have 0 water buckets.\n","The move function is not returning"\
                                                                         "the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]=="\nYou walked into a wall. Oof!\n","The move function is not returning"\
                                                         "the correct list. The second element of "\
                                                         "list is not the correct additional move  "\
                                                         "message"
    
    
    assert result[2]=="wall","The move function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether "\
                                 "the player has won or lost, or whether the player"\
                                 "tried to walk into a wall"

    
    #Testing for move 'd' when the player tries to walk out of bounds.
    my_game=Game(file4)
    
    
    result=my_game.move('d')
    
    
    assert my_game.listOfMoves==[],"The move function of game is changing "\
                                  "the initial list of moves when the"\
                                  "player tries to walk into a wall."
    
    
    assert my_game.numberOfMoves==0,"The move function of game is changing "\
                                  "the initial number of moves when the"\
                                  "player tries to walk into a wall."
    
    
    assert result[0]=="****\n*  A\n*Y**\n\nYou have 0 water buckets.\n","The move function is not returning"\
                                                                         "the correct list. The first element of "\
                                                                         "list is not the correct representation "\
                                                                         "of grid configuration and player."
    
    
    assert result[1]=="\nYou walked into a wall. Oof!\n","The move function is not returning"\
                                                         "the correct list. The second element of "\
                                                         "list is not the correct additional move  "\
                                                         "message"
    
    
    assert result[2]=="wall","The move function is not returning"\
                                 "the correct list. The third element of "\
                                 "list is not telling correctly whether "\
                                 "the player can continue playing or whether "\
                                 "the player has won or lost, or whether the player"\
                                 "tried to walk into a wall"

    

    #move e is wait.For move e, the player’s position does not changes.So with move 'e', player can not try to move out of bounds.


    

def run_tests():

    """ Testing the game class.
     
     Testing the constructor of the game class for positive
     and negative test case. 

     Testing the move function of the game class-

     It tests all positive, negative, and edge test cases for 
     the move function.
        
        It tests the only negative test case when the configuration 
        file does not exists.
        It does not has any negative test cases for invalid moves
        because only the valid moves such 'w', 'a',' s', 'd' and 'e' 
        will be passed as arguments to the move function of the game.
        It will never receive any invalid move. This is handled by the 
        run.py class. 
        This functionality has been tested in the e2e tests. 
        
 """
   
    test_constructor_positive()
    test_constructor_negative()
    test_game_move_positive()
    test_game_move_negative()
    test_game_move_edge()
    print("Congratulations ! You passed all the game test cases.")


