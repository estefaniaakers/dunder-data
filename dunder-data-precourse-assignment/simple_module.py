'''
This is a simple module with a few functions
'''

author = 'Ted Petrou'
favorite_number = 4

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def count_vowels(word):
    count = 0
    for letter in word.lower():
        count += letter in 'aeiou'
        
    return count