'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # occurences stores the times th shows up
    occurences = 0

    # the base case for the recursion 
    if len(word) <= 1:
        return 0

    # pointers to keep track of where i am in the string
    pointer_a = 0
    pointer_b = 1

    # if the pointers are at the right strings
    if word[pointer_a] + word[pointer_b] == "th":
        # incrmeent the pointers by 2 to not waste loops
        pointer_a += 2
        pointer_b == 2
        # occurences should go up by 1
        occurences += 1
        # then we can use recursion to check the rest of the string by slicing the word string starting at pointer_a
        occurences += count_th(word[pointer_a:])
    else:
        # pointer should only go up by 1 here in case since i am not sure what the next 2 strings in the list would be
        pointer_a += 1
        pointer_b += 1
        occurences += count_th(word[pointer_a:])

    return occurences
