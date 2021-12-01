""""
Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False
str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False
str.isdigit()
This method checks if all the characters of a string are digits (0-9).

>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False
str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).

>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False
str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).

>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False

"""

# AlphaNumberic Function
def alphanumeric(s):
    for i in range(len(s)):
        if s[i].isalnum():
            return True
    return False
        
# Alphabetic Function
def alphabetical(s):
    for i in range(len(s)):
        if s[i].isalpha():
            return True
    return False
  
# Digits Function
def digits(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return True
    return False
 
# Lower Case Function
def lowercase(s):
    for i in range(len(s)):
        if s[i].islower():
            return True
    return False

# Upper Case Function
def uppercase(s):
    for i in range(len(s)):
        if s[i].isupper():
            return True
    return False

def main():
    s = input()
    
    #To Print only 5 line we have to make  a function
    # Alphanumeric Check
    print(alphanumeric(s))
    
    # Alphabetic check    
    print(alphabetical(s))
        
    #Digits Check
    print(digits(s))
        
    #Lower Case Check
    print(lowercase(s))
    
    # Upper Case Check
    print(uppercase(s))
            
if __name__ == '__main__':
    main()