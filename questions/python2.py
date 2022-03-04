# -------------------------------------------------------------------------------------------------------------------------------------------------

# INSTRUCTIONS

# In case it is not clear, the Question appears first, then examples, then any hints and finally the function that you need to complete appears underneath:
#
# 	<QUESTION>
#
# 	<EXAMPLES>
#
# 	<HINT>

# You are allowed access to the internet for this assessment, but remember you could use the DOCUMENTATION that comes bundled with your Python installation.
# Every command has help documentation. To read it:
# 	1. Access Python from your CLI
# 	2. Type help(<command>) and hit enter, where <command> is the command you want help with. For example: help(str)

# -------------------------------------------------------------------------------------------------------------------------------------------------

# <QUESTION 1>

# Given a string, return a string where for every char in the original string, there are three chars.

# <EXAMPLES>

# one("The") → "TTThhheee"
# one("AAbb") → "AAAAAAbbbbbb"
# one("Hi-There") → "HHHiii---TTThhheeerrreee"

# <HINT>
# How does a for loop iterate through a string?

def one(string):
    finalResult = '' 
    for i in string: 
        finalResult += i * 3
    return finalResult

# -------------------------------------------------------------------------------------------------------------------------------------------------

    # <QUESTION 2>

    # Write a function which returns the boolean True if the input is only divisible by one and itself.

    # The function should return the boolean False if not.

    # <EXAMPLES>

    # two(3) → True
    # two(8) → False

    # <HINT>
    # What operator will give you the remainder?
    # Use your CLI to access the Python documentation and get help manipulating strings - help(range).


def two(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# -------------------------------------------------------------------------------------------------------------------------------------------------

    # <QUESTION 3>

    # Write a function which takes an integer input, a, and returns the sum a+aa+aaa+aaaa.

    # So if 2 was the input, the function should return 2+22+222+2222 which is 2468.

    # <EXAMPLES>

    # three(9) → 11106
    # three(5) → 6170

    # <HINT>
    # What happens if you multiply a string by a number?


def three(a):
    string = str(a)
    two = string*2
    three = string*3
    four = string*4
    return a + int(two) + int(three) + int(four)

# -------------------------------------------------------------------------------------------------------------------------------------------------

    # <QUESTION 4>

    # Given two Strings of equal length, 'merge' them into one String.

    # Do this by 'zipping' the Strings together.

    # Start with the first char of the first String.
    # Then add the first char from the second String.
    # Then add the second char from the first String.
    # And so on.

    # Maintain case.

    # You will not encounter whitespace.

    # <EXAMPLES>

    # four("String","Fridge") → "SFtrriidngge"
    # four("Dog","Cat") → "DCoagt"
    # four("True","Tree") → "TTrrueee"
    # four("return","letter") → "rleettutrenr"

    # <HINT>
    # Use your CLI to access the Python documentation and get help manipulating strings - help(list.insert).
    # How would you seperate a string into characters?


def four(string1, string2):
    splitString1 = list(string1)
    splitString2 = list(string2)
    result = ('')
    for i in range(0, len(splitString1)):
        result += splitString1[i] + splitString2[i]
    return result

# -------------------------------------------------------------------------------------------------------------------------------------------------

    # <QUESTION 5>

    # Write a function to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

    # <EXAMPLES>

    # five() → [100,102,122,198,200]
    # five() → [108,104,106,188,200]
    # five() → [154,102,132,178,164]

    # <HINT>
    # There is a module which can be used to generate random numbers, this module is called random.
    # The random module contains a function called randint.

import random
def five():
    result = []
    i = 1
    while i <= 5:
        randomNumber = random.randint(100, 200)
        if randomNumber % 2 == 0:
            result.append(randomNumber)
            i += 1
    return result

# -------------------------------------------------------------------------------------------------------------------------------------------------

    # <QUESTION 6>

    # Given a string, return the boolean True if it ends in "py", and False if not.

    # Ignore Case.

    # For Example:

    # six("ilovepy") → True
    # six("welovepy") → True
    # six("welovepyforreal") → False
    # six("pyiscool") → False

    # <HINT>
    # There are no hints for this question.


def six(string):
    ignoreCase = string.lower()
    splitString = list(ignoreCase)
    if splitString[-1] == 'y':
        if splitString[-2] == 'p':
            return True
    return False

# -------------------------------------------------------------------------------------------------------------------------------------------------

    # <QUESTION 7>

    # Given three ints, a b c, one of them is small, one is medium and one is large.

    # Return the boolean True if the three values are evenly spaced, so the
    # difference between small and medium is the same as the difference between
    # medium and large.

    # Do not assume the ints will come to you in a reasonable order.

    # <EXAMPLES>

    # seven(2, 4, 6) → True
    # seven(4, 6, 2) → True
    # seven(4, 6, 3) → False
    # seven(4, 60, 9) → False

    # <HINT>
    # There is a function for lists called sort.
    # Use the cli to access the documentation help(list.sort)


def seven(a, b, c):
    list1 = [a,b,c]
    list1.sort()
    if list1[-1] - list1[-2] == list1[1] - list1[0]:
        return True
    return False

# -------------------------------------------------------------------------------------------------------------------------------------------------

    # <QUESTION 8>

    # Given a string and an integer, n, return a string that removes n letters from the 'middle' of the string.

    # The string length will be at least n, and be odd when the length of the input is odd, so there will always be a 'middle'.

    # <EXAMPLES>

    # eight("Hello", 3) → "Ho"
    # eight("Chocolate", 3) → "Choate"
    # eight("Chocolate", 1) → "Choclate"

    # <HINT>
    # Use the cli to access the documentation help(str.replace)


def eight(string,  a):
    for i in range(0, a):
        string = string[:len(string)//2] + string[1 + len(string)//2:]
    return string


# -------------------------------------------------------------------------------------------------------------------------------------------------

    # <QUESTION 9>

    # Given two string inputs, if one can be made from the other return the boolean True, if not return the boolean False.

    # <EXAMPLES>

    # nine("god", "dog") → True
    # nine("tree", "tiredest") → True
    # nine("cat", "dog") → False
    # nine("tripping", "gin") → True

    # <HINT>
    # There are no hints for this question.


def nine(string1, string2):
    if len(string1) > len(string2):
        return nine(string2, string1)

    checkForWord = []
    string1Lower = string1.lower()
    string2Lower = string2.lower()
    for i in string1Lower:
        # print(i)
        if i not in string2Lower:
            checkForWord.append(False)
            # print(checkForWord)
        else:
            checkForWord.append(True)
            # print(checkForWord)
    if False in checkForWord:
        return False
    else:
        return True


# -------------------------------------------------------------------------------------------------------------------------------------------------

    # <QUESTION 10>

    # Write a function which takes 2 integers greater than 0, x,y as input and generates a 2-dimensional array.

    # The element value in the i-th row and j-th column of the array should be i*j.

    # <EXAMPLES>

    # ten(3,2) → [[0,0,0],[0,1,2]]
    # ten(2,1) → [[0,0]]
    # ten(3,4) → [[0,0,0],[0,1,2],[0,2,4],[0,3,6]]

    # <HINT>
    # Think about nesting for loops.


def ten(x, y):
    return []

# -------------------------------------------------------------------------------------------------------------------------------------------------
