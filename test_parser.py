from game_parser import read_lines 
from game_parser import parse 
from cells import (
     Start,
     End,
     Air,
     Wall,
     Fire,
     Water,
     Teleport
 )





def test_read_lines_positive():


    """Testing the read_lines function.

    Positive test case. It checks whether read_lines 
    function is passing the correct arguments to
    parse function or not when different valid and 
    expected configuration files are given."""


    file1="/home/unit_test_grids/read_lines_test.txt"

    received=read_lines(file1)
    expected=['*X**\n', '*  *\n', '*  *\n', '**Y*\n']

    assert received[1]==expected,"The read_lines function is not passing the "\
                                   "correct list of strings to parse."
   


    file2="/home/unit_test_grids/read_lines_test2.txt"

    received=read_lines(file2)
    expected=['**X**\n', '**Y**\n']

    assert received[1]==expected,"The read_lines function is not passing the "\
                                 "correct list of strings to parse."
   


def test_read_lines_negative():

    """Testing the read_lines function.

    Negative test case. It checks whether read_lines 
    function is returning the correct error message or
    not when the given configuration filename does
    not exists."""


    file="/home/unit_test_grids/read_lines_tests.txt"

    received=read_lines(file)
    expected="/home/unit_test_grids/read_lines_tests.txt does not exist!"

    assert received==expected,"The read_lines function is not return the correct "\
                               "error message when file does not exists."
   


def test_read_lines_edge():

    """Testing the read_lines function.

    Edge test case.It checks whether read_lines 
    function is passing the correct arguments to
    parse function or not when the configuration
    file has only one line, and when the
    configuration file has only one letter
    in each line."""


    file3="/home/unit_test_grids/read_lines_test3.txt"

    received=read_lines(file3)[1]
    expected=['*XY**\n']

    assert received==expected,"The read_lines function is not passing the "\
                              "correct list of strings to parse."


    file4="/home/unit_test_grids/read_lines_test4.txt"

    received=read_lines(file4)[1]
    expected=['*\n','X\n','Y\n','*\n']

    assert received==expected,"The read_lines function is not passing the "\
                               "correct list of strings to parse."
   



def test_parse_positive():


    """Testing the parse function.

    Positive test case.It tests whether the parse
    function is assigning, the correct cell object
    to the grid or not when valid list of strings are passed 
    to it as arguments.It checks whether it returns 
    the correct list of list of cells or not. """


    lines_list1 = ['*X*\n', '*W*\n', '*Y*\n']
    received=parse(lines_list1)
  
  
  
    assert isinstance(received[0][0],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[0][1],Start)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[0][2],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[1][0],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[1][1],Water)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[1][2],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[2][0],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[2][1],End)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[2][2],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    
    lines_list2 = ['*X**\n', '*WF*\n', '*  *\n', '*1 *\n', '* 1*\n', '*Y**\n']
    received=parse(lines_list2)
    
    
    assert isinstance(received[0][0],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[0][1],Start)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[0][2],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[0][3],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[1][0],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[1][1],Water)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[1][2],Fire)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[1][3],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[2][0],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[2][2],Air)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[2][2],Air)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[2][3],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[3][0],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[3][1],Teleport)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[3][2],Air)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[3][3],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[4][0],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[4][1],Air)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[4][2],Teleport)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[4][3],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[5][0],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[5][1],End)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[5][2],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    assert isinstance(received[5][3],Wall)== True,"The parse() function failed to "\
                                                  "create correct list of list of cells."
    
    
    
def test_parse_negative():

    """Testing the parse function.

    Negative test case. It checks whether parse
    function is raising the correct value error 
    with right error message or not when the given 
    list of strings has bad or invalid letter,or
    more or less than one starting or ending cell, and 
    non-matching teleport pads.

    """


    try:

        lines=['*X**\n', '*C *\n', '*Y**\n']
        received=parse(lines)

    except ValueError as e:

        assert str(e)=="Bad letter in configuration file: C.","The parse function failed "\
                                                               "to identify bad letters in the "\
                                                               "list of strings received as argument."
        



    try:

        lines=['*X**\n', '* X*\n', '*Y**\n']
        received=parse(lines)

    except ValueError as e:

        assert str(e)=="Expected 1 starting position, got 2.","The parse function failed "\
                                                               "to identify the presence of more "\
                                                               "than 1 starting position."
    
  
  
  
    try:

        lines=['****\n', '*  *\n', '*Y**\n']
        received=parse(lines)

    except ValueError as e:

        assert str(e)=="Expected 1 starting position, got 0.","The parse function failed "\
                                                              "to identify the absence of "\
                                                              "starting position."
       


    try:

        lines=['*X**\n', '* Y*\n', '*Y**\n']
        received=parse(lines)

    except ValueError as e:

        assert str(e)=="Expected 1 ending position, got 2.","The parse function failed "\
                                                            "to identify the presence of "\
                                                            "more than 1 ending position."




    try:

        lines=['**X*\n', '*W *\n', '****\n']
        received=parse(lines)

    except ValueError as e:

        assert str(e)=="Expected 1 ending position, got 0.","The parse function failed to "\
                                                             "identify the absence of ending "\
                                                             "position."
       



    try:

        lines=['*X**\n', '* 1*\n', '*Y**\n']
        received=parse(lines)

    except ValueError as e:

        assert str(e)=="Teleport pad 1 does not have an exclusively matching pad.","The parse function failed "\
                                                                                    "to identify teleport pads not"\
                                                                                    " present in pairs."





def test_parse_edge():

    """Testing the parse function.

    Edge test case.It checks whether parse
    function is raising the correct value error 
    with right error message or not when the given 
    list of strings has more than one bad letters,
    when the list of strings has more than one value errors,and
    when the configuration file is empty i.e list of strings 
    passed as argument is [' \n']. It also checks the cases
    when the configuration has only one line, configuration has
    only one character in each line, and when the configuration 
    has only start and end cell.

    """
    

    try:

        lines=['*X***\n', '*CD *\n', '**Y**\n']
        received=parse(lines)

    except ValueError as e:

        assert str(e)=="Bad letter in configuration file: C.","The parse function failed to "\
                                                               "identify bad letters in the list of "\
                                                               "strings received as argument."
        



    try:

        lines=['****\n', '*  *\n', '****\n']
        received=parse(lines)

    except ValueError as e:

        assert str(e)=="Expected 1 starting position, got 0.","The parse function failed to "\
                                                               "identify the absence of starting "\
                                                               "position."
       




    try:

        lines=[' n']
        received=parse(lines)

    except ValueError as e:

        assert str(e)=="Expected 1 starting position, got 0.","The parse function failed to "\
                                                               "identify the absence of "\
                                                               "starting position."



    
    lines_list1 = ['*XY*\n']
    received=parse(lines_list1)

  
  
    assert isinstance(received[0][0],Wall)== True,"The parse() function failed to create"\
                                                   " correct list of list of cells."
    
    
    assert isinstance(received[0][1],Start)== True,"The parse() function failed to create"\
                                                   " correct list of list of cells."
    
    
    assert isinstance(received[0][2],End)== True,"The parse() function failed to create"\
                                                   " correct list of list of cells."
    
    
    assert isinstance(received[0][3],Wall)== True,"The parse() function failed to create"\
                                                   " correct list of list of cells."
    

 
 
    lines_list1 = ['*\n','X\n','Y\n','*\n']
    received=parse(lines_list1)

   
    assert isinstance(received[0][0],Wall)== True,"The parse() function failed to create"\
                                                   " correct list of list of cells."
    
    
    assert isinstance(received[1][0],Start)== True,"The parse() function failed to create"\
                                                   " correct list of list of cells."
    
    
    assert isinstance(received[2][0],End)== True,"The parse() function failed to create"\
                                                   " correct list of list of cells."
    
    
    assert isinstance(received[3][0],Wall)== True,"The parse() function failed to create"\
                                                   " correct list of list of cells."
    

   
   
    lines_list1 = ['X\n','Y\n']
    received=parse(lines_list1)

   
   
    assert isinstance(received[0][0],Start)== True,"The parse() function failed to create"\
                                                   " correct list of list of cells."
    
    
    assert isinstance(received[1][0],End)== True,"The parse() function failed to create"\
                                                   " correct list of list of cells."





def run_tests():
    """ Testing the game_parser class. 

    Testing the read_lines function-
      
      It tests all positive, negative, and edge test cases
      It does not tests the edge test case when the given 
      configuration file is empty, because in that case
      value error will be raised by parse function. Parse
      function is called inside read_lines function.This 
      functionality has been tested under unit tests for 
      parse function.

    Testing the parse function.

 """

    test_read_lines_positive()
    test_read_lines_negative()
    test_read_lines_edge()
    test_parse_positive()
    test_parse_negative()
    test_parse_edge()
    print("Congratulations ! You passed all the"\
           " game_parser class tests.")


