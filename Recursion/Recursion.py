import copy

## Write all permutations of a set of letters
def scrabbles(letters):
    if len(letters) == 1:
        return letters
    wordlist = []
    for i, letter in enumerate(letters):
        remainder = letters
        remainder = remainder[:i] + remainder[(i+1):]
        smallwords = scrabbles(remainder)
        for word in smallwords:
            wordlist.append(letter + word)
    return wordlist

## All plays (all letters or fewer)
def allplays(letters):
    if len(letters) == 1:
        return letters
    wordlist = []
    for i, letter in enumerate(letters):
        remainder = letters
        remainder = remainder[:i] + remainder[(i+1):]
        smallwords = allplays(remainder)
        for word in smallwords:
            wordlist.append(word)
            wordlist.append(letter + word)
    return wordlist

def cardhand(hand, handsize = 5):
    if len(hand) == 0:
        return ['']
    elif handsize == 0:
        return ['']
    elif len(hand) == handsize:
        return hand
    handlist = []
    handcopy = copy.deepcopy(hand)
    for card in hand:
        ## pop card
        handcopy = handcopy[1:]
        smallhands = cardhand(hand, handsize - 1)
        for item in smallhands:
            handlist.append(card + item)
    return handlist
