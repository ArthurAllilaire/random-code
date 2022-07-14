txt = "JACOBSANDERS"


def perm_generator(txt, delimiter = ""):
    """
    Take a string and returns each possible permutation
    """
    result = []

    if len(txt) == 1:
        return txt

    for i in range(len(txt)):
        char = txt[i]
        rest_of_txt =  txt[:i] + txt[i+1:]

        for j in range(len(txt)):
            return 




"""
abc - take a as fixed then get all permutations bc, cb


"""
