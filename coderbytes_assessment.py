
## Reverse String
def ReverseString(rev_str):
    rev_str = ''
    for char in str[::-1]
        rev_str += char
    return(rev_str)

print ReverseString(raw_input())


## Factorial --> recursive -> Easier + each save solve be used for future
def Factorial(num):
    if num == 0:
        return 1
    else
        return Factorial(n-1) * n
    print Factorial(raw_input())


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
