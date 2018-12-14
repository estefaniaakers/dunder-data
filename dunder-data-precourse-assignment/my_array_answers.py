import random

def create_random_array(n):
    return [random.randint(1, 100) for i in range(n)]

def add_constant(array, x):
    return [a + x for a in array]

def sub_constant(array, x):
    return [a - x for a in array]

def mul_constant(array, x):
    return [a * x for a in array]

def div_constant(array, x):
    return [a / x for a in array]

def pow_constant(array, x):
    return [a ** x for a in array]

def add(array1, array2):
    final_array = []
    for i, a in enumerate(array1):
        b = array2[i]
        final_array.append(a + b)
    return final_array

def sub(array1, array2):
    final_array = []
    for i, a in enumerate(array1):
        b = array2[i]
        final_array.append(a - b)
    return final_array

def mul(array1, array2):
    final_array = []
    for i, a in enumerate(array1):
        b = array2[i]
        final_array.append(a * b)
    return final_array

def div(array1, array2):
    final_array = []
    for i, a in enumerate(array1):
        b = array2[i]
        final_array.append(a / b)
    return final_array

def pow_(array1, array2):
    final_array = []
    for i, a in enumerate(array1):
        b = array2[i]
        final_array.append(a ** b)
    return final_array

def max_(array):
    return max(array)

def min_(array):
    return min(array)

def mean(array):
    return sum(array) / len(array)

def median(array):
    n = len(array)
    middle = int(n / 2)
    array_sorted = sorted(array)
    
    # even number of elements
    if n % 2 == 0:
        right = array_sorted[middle]
        left = array_sorted[middle - 1]
        return (left + right) / 2
    # odd
    else:
        return array_sorted[middle]
    
def dot_product(array1, array2):
    return sum(mul(array1, array2))

def distance(array1, array2):
    return sum(pow_constant(sub(array1, array2), 2)) ** .5
