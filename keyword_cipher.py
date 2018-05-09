
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
