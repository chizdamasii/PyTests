"""
Write an algorithm that analyzes and decodes a string.

The cipher works as follows: it takes the alphabet and a keyword (that shall not include duplicate letters) and builds a new string starting with the keyword and continues with the letters of the unused alphabet.

Example (the keyword in the example is KEYWORD):

Input:
- "KEYWORD" as the keyword
- String that has to be deciphered.
Output: String representing the decoded word.

Example:

For: KEYWORD and code: LXQAJI

Output is PYTHON
"""
import fileinput


def get_input():
    f = fileinput.input()
    return next(f).strip('\n'), next(f).strip('\n')


def main():
    keyword, cripted_word = get_input()
    #keyword = 'KEYWORD'
    #cripted_word = 'LXQAJI'
    #output = 'PYTHON'
    result = -1
    text = ""
    #I am asuming only upper chars are allowed
    result = ""
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #verifiyng keyword validity
    for char in chars:
        count = keyword.count(char)
        if count>1:
            print("The key is not valid, it contains duplicate letters")
			return
    #creating the new chars string
    newChars = keyword
    for letter in chars:
        if letter not in newChars:
            newChars += letter
    #decrypt using the newChars string
    for letter in cripted_word:
        index = newChars.index(letter)
        result += chars[index]
    print (result)


if __name__ == '__main__':
    main()
