
## Reverse String
def ReverseString(rev_str):
    rev_str = ''
    for char in str[::-1]
        rev_str += char
    return(rev_str)

print ReverseString(input())


## Factorial --> recursive -> Easier + each save solve be used for future
def Factorial(num):
    if num == 0:
        return 1
    else
        return Factorial(n-1) * n
    print Factorial(input()) ## raw_input() is no more in python3


#**
# 1. String module is import
# 2.
#
import string
def LongestWord(sentence):
    cancel_punct = sentence.translate(str.maketrans("", "", str.punctuation))
    split_sen = cancel_punct.split()
    return max(split_sen, key=len)


## Letter changes

#
# The string module is imported to use its ascii_lowercase constant.
#
# The ord function is used to convert each letter in the string to its corresponding ASCII code.
#
# --> The letter is encoded by adding 1 to its ASCII code, and then taking the modulo 26 to ensure that the encoded letter stays
# within the range of lowercase letters (97 to 122).
# The encoded letter is then converted back to a character using the chr function.
# If the encoded letter is a vowel, it is capitalized, otherwise it is left in lowercase.
# The modified letter is added to the encoded_string.
# -->  optimized as it uses index and replace
# Also vowels is defined once rather than inside a loop ..> to reduce no of times string created
# #

import string
def LetterChanges(inp_str):
    letters= string.ascii_lowercase
    vowels = 'aeiou'
    encode_str = ''
    for letter in inp_str:
        if letter.lower() in letters:
            if letter == 'z':
                encode_str += 'A'
            else:
                encode_letter = chr((ord(letter.lower()) - 97 + 1) % 26 + 97)  ## subtracting by 97('a') and adding 1 to to convert to range from 1 to 26
                #Representing its position in the alphabet
                encode_str += encode_letter.upper() if encode_letter in vowels else encode_letter
        else:
            encode_str += letter
    return encode_str

##
#2 True condition-->
#a) Checking distance between a and b characters

def ABCheck(str):
    for i in range((len(str) - 4)):
        if str[i] == "a" and str[i + 4] == "b":
            return True
        elif str[i] == "b" and str[i + 4] == "a":
            return True
        else:
            i += 1
        return False


##
# string parameter being passed and return the string with the letters
# #in alphabetical order (ie. hello becomes ehllo). Assume numbers and
# #punctuation symbols will not be included in the string."
# Removes any punctuation marks (. , ;)

punct = list()
def AlphabetSoup(str):
    for line in str:
        if line in punct:
            str = str.replace(line, "")
        str.sort()
        str = "".join(str)
    return str

print AlphabetSoup(input())


##  Find Arithmetic / Geometric --> diff between each number consistent

def ArGeo(ar):
    arr = ar.split(",")
    if (int(arr[1] - int(arr[0]) == (int(arr[len(arr) - 1])) - (int(arr[len(arr) -2])))):
        return "Arithmetic"
    elif (int(arr[1] - int(arr[0]) == (int(arr[len(arr) - 1])) - (int(arr[len(arr) -2])))):
        return "Geometric"
    else:
        return -1

##eturn the string true if num2 is greater
#than num1, otherwise return the string false. If the parameter values
#are equal to each other then return the string -1."

def CheckNums(n1,n2):
    n1 = int(n1)
    n2 = int(n2)
    if n2 == n1:
        return -1
    else:
        return (n2 > n1)

print (CheckNums(int(input()), int(input())))


##Ex0h(str)
#string true if there is an equal number of x's
#and o's, otherwise return the string false. Only these two letters will be
#entered in the string, no punctuation or numbers.

def EqualX(str):
    x_swap = 0
    o_swap = 0
    for i in str:
        if i == "x":
            x_swap += 1
        elif i == "o":
            o_swap += 1
    return x_swap == o_swap
print (EqualX(input()))

##Optimized for larger inputs:

def EqualX(str):
    x_count = str.count("x")
    o_count = str.count("o")
    return x_count == o_count
print(EqualX(input()))


## Used the fnc capitalized and then appended after first element. Make the list to a single string
## join is better than + in concatenation for lot of strings
def Capitalize(str):
    words = str.split(" ")
    caplist = []
    for word in words:
        word1 = word[0].capitalized()
        caplist.append(word1 + word[1:])
    capped = "".join(caplist)
    return capped


## lemon - melon // senile - feniles
def Palindrome(str):
    length = (len(str) - 1)

    for i in range(length):
        if str[i] != str[length - i]:
            return False
    return True

print (Palindrome(input()))

