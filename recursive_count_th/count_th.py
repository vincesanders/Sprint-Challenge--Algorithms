'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# O(1) space
def count_th(word): # O(n) n = word length (worst case), for every 'th', runtime will decrease by 1
    # If the word has less than 2 letters then it can't match 'th'
    if len(word) < 2:
        return 0
    if word[0] =='t' and word[1] == 'h':
        # if there is still letters left to test
        if len(word) > 2:
            return 1 + count_th(word[2:]) # we know the next lette is 'h' and won't match 't', so we can skip
        else:
            return 1
    else: # no match, check the next substring
        if len(word) > 2: # there is still letters left to test
            return count_th(word[1:])
        else: # no match and not enough letters left to test
            return 0
