'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word): # O(n) n = word length (worst case)
    if len(word) < 2:
        return 0
    if word[0] =='t' and word[1] == 'h':
        if len(word) > 2:
            return 1 + count_th(word[2:])
        else:
            return 1
    else:
        if len(word) > 2:
            return count_th(word[1:])
        else:
            return 0
