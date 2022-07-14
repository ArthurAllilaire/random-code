#Code for 1.1 
# Requirements - find if a string has all unique characters - no additional data structures.
text = 'abcdefgha'
#Create an array that has all possible options - i.e. all 128 ascii characters - with false as their value
def is_unique(text):
    ascii_len = 128
    if len(text) > ascii_len:
        return False
    charset = [0] * ascii_len
    # for every char in string
    for char in text:
    # Converst to ascii (use ord())
        if charset[ord(char)]:
            return False
    #The index in the array should then be used
        charset[ord(char)] = 1

    return True
        

print(is_unique(text))