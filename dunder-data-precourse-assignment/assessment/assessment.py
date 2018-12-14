'''
This is your precourse assesment. Below is a set of functions that you must complete.
Delete `pass` and write the contents of the function that will produce the desired outcome.

The docstrings under the functions will give you instructions on how to produce
the desired output.

Your code will be run against a unit test in file assessment_unittest.py
Open that file to see how basic unit tests are done. Pandas runs many 1000's of unit tests.

To test your code
----------------
At the command prompt run the following:
>>> python assessment_unittest.py

If any of the tests failed you will see `FAILED(failures=n)` 
where n is the number of tests failed.

If all your tests are correct you will see `OK`

Please commit the changes back to github

The first function has been done for you.

'''

def mult_dummy(x, y):
    '''
    Multiplies two numbers together

    Parameters
    ----------
    x: number
    y: number

    Returns
    -------
    The value when x and y are multiplied together
    '''
    return x * y

def add_divide_product(x, y):
    '''
    Divide the sum of two numbers by their product

    Parameters
    ----------
    x: positive number
    y: positive number

    Returns
    -------
    The value of the division of the sum of two numbers by their product

    '''
    pass

def count_letters(string, letter):
    '''
    Counts the occurrences of a single letter in a string

    Parameters
    ----------
    string: a string with characters
    letter: a single character that you will count in the string

    Return
    ------
    The number of times `letter` appears in `string`
    '''
    pass

def largest_smallest(some_list):
    '''
    Find the largest and smallest value in a list

    Parameters
    ----------
    some_list: a list of numbers

    Returns
    -------
    a tuple of the largest and smallest numbers in the list
    '''
    pass

def greatest_divisble_7(some_list):
    '''
    Find the largest number in a list that is divisible by 7

    Parameters
    ----------
    some_list: a list of numbers

    Returns
    -------
    The largest number that is divisible by 7
    '''
    pass

def greatest_common_factor(x, y):
    '''
    Find the greatest common factor between x and y

    Parameters
    ----------
    x: a positive integer
    y: a positive integer

    Returns
    -------
    The largest integer divisible by x and y
    '''
    pass

def count_words(string):
    '''
    Count the words in the string

    Parameters
    ----------
    string: any string

    Returns
    -------
    An integer of the number of words in the string

    Hint
    ----
    look at the split method
    '''
    pass

def count_substring_words(string, substring):
    '''
    Count the number of words that contain a certain word

    Parameters
    ----------
    string: any string
    substring : any string

    Returns
    -------
    The number of words in `string` that contain an exact match of `substring`
    '''
    pass

def longest_word(string):
    '''
    Get the longest word from a string

    Parameters
    ----------
    string: a string of words separated by spaces

    Returns
    -------
    The string with the most characters
    '''
    pass

def double_letter_words(string):
    '''
    Get all the words that have two consecutive repeating letters

    Parameters
    ----------
    string: a string of words separated by spaces

    Returns
    -------
    a list of all words that contain at least one occurrence of 
    consecutive repeating letters
    '''
    pass

def dict_of_powers(n):
    '''
    Create a dictionary with keys as integers 1 to n (inclusive) 
    and the values as a list of that integer raised to the 2nd, 3rd and 4th power

    Parameters
    ----------
    n: positive integer

    Returns
    -------
    a dictionary with keys as integers 1 to n (inclusive) 
    and the values as a list of that integer raised to the 2nd, 3rd and 4th power

    '''
    pass

def last_2_list(some_list):
    '''
    Select the 4th to last and 2nd to last elements in a list

    Parameters
    ----------
    some_list: a list of elements

    Returns
    -------
    a list with the 4th and 2nd to last elements of `some_list`
    '''
    pass

def reorder_list(orig_list, order):
    '''
    Reorder a list based on another list

    Parameters
    ----------
    orig_list: a list that will get reordered
    order: A list of integers that correspond to the new order of the list.
           Will contain all integers between 0 and len(orig_list)-1

    Examples
    --------
    if orig_list is ['a', 'b', 'c'] and order is [2, 0, 1] then
    you would return ['c', 'a', 'b']

    '''
    pass

def prob_3_dice(num_dice, faces, total, num_simulations=10000):
    '''
    Finds the probability through simulation that the dice thrown will equal the total

    Parameters
    ----------
    num_dice: number of dice thrown
    faces: a list of the possible faces (integers)
    total: the sum of the faces that we want to find the probability of
    num_simulations: the number of times to simulate the dice throw. Default of 10000

    Returns
    -------
    the probability of sum of the dice equaling the total

    Hint
    ----
    Use the choice function in the random module to simulate dice throws

    '''
    pass
