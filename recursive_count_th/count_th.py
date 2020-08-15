'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    string = len(word)
    substring = "th"
    sublen = len(substring)

    if string <= 1:
        return 0

    elif word[0 : sublen] == substring:
        return count_th(word[sublen - 1:]) + 1

    else:
        return count_th(word[sublen - 1:])


# WHAT WE KNOW:
# - that the function input is a string
# - that the output should the number of occurences of the letters "th"
# - that letter case matters ie. TH is not equal to th
# - the function has to be recursive ie. recursive binary search
# - NO LOOPS
# 
# BASE CASE:
# - if the string has a length of 1 or less, return 0