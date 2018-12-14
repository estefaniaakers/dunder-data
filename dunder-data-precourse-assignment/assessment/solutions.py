# solutions

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

    '''
    return (x + y) / (x * y)

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
    return string.count(letter)

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
    return max(some_list), min(some_list)

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
    return max([num for num in some_list if num % 7 == 0])

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
    x_factors = [num for num in range(1, x+1) if x % num == 0]
    y_factors = [num for num in range(1, y+1) if y % num == 0]
    return max(set(x_factors) & set(y_factors))

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
    return len(string.split())

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
    return sum([substring in word for word in string.split()])

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
    words = string.split()
    max_word = ''
    for word in words:
        if len(word) > len(max_word):
            max_word = word
    return max_word

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
    doubles = []
    words = string.split()
    for word in words:
        prev_char = ''
        for char in word:
            if char == prev_char:
                doubles.append(word)
                break
            prev_char = char
    return doubles

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
    return {num: [num ** 2, num ** 3, num ** 4] for num in range(1, n+1)}

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
    return some_list[-4::2]

def reorder_list(orig_list, order):
    '''
    Reorder a list based on another list

    Parameters
    ----------
    orig_list: a list that will get reordered
    order: a list of integers that correspond to the new order of the list

    Examples
    --------
    if orig_list is ['a', 'b', 'c'] and order is [2, 0, 1] then
    you would return ['c', 'a', 'b']

    '''
    return [orig_list[num] for num in order]

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
    the probability of sum of the dice equaling the total rounded to 2 decimals

    '''
    import random
    count = 0
    for i in range(num_simulations):
        cur_roll = [random.choice(faces) for _ in range(num_dice)]
        if sum(cur_roll) == total:
            count += 1
    return count / num_simulations
