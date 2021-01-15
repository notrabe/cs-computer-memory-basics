"""

# task 7 of 9

def csReverseIntegerBits(n):
    lst = []                       # init empty list.
    binary = '{0:08b}'.format(n)   # convert input num to binary.
    print(list(binary))            
    for i in list(binary):         # list each digit in the binary, append each digit to our empty list.
        lst.append(i)  
    lst.reverse()                  # reverse the order of the digits in the list.
    revBinary = ''.join(lst)       # join the digits.
    newNum = int(revBinary, 2)     # turn them into the desired number using base '2' for binary.
    return newNum
    

csReverseIntegerBits(267)

"""

# task 8 of 9

"""

"""
# task 9 of 9 DOES NOT PASS ALL HIDDEN TESTS

def csRaindrops(number):
    factors = []
    if3 = 'Pling'
    if5 = 'Plang'
    if7 = 'Plong'

    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(-i)
    
    if 3 in factors and 5 in factors and 7 in factors:
        print(if3, if5, if7)
        return if3, if5, if7
    elif 3 in factors and 5 in factors:
        print(if3, if5)
        return if3, if5
    elif 5 in factors and 7 in factors:
        print(if5, if7)
        return if5, if7
    elif 3 in factors and 7 in factors:
        print(if3, if7)
        return if3, if7
    elif 3 in factors:
        print(if3)
        return if3
    elif 5 in factors:
        print(if5)
        return if5
    elif 7 in factors:
        print(if7)
        return if7
    else:
        return str(number)

csRaindrops(5)