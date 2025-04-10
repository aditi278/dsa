#Find all possible ways to construct targetString using a list of strings
def allConstruct(targetString, substrings, memo=None):
    if memo is None:
        memo = {}
    if targetString == "":
        return [[]]
    if targetString in memo.keys():
        return memo[targetString]
    
    listOfSubstrings = []
    for s in substrings:
        if targetString.startswith(s):
            possibleSubstring = allConstruct(targetString[len(s):], substrings, memo=memo)
            for p in possibleSubstring:
                ls = [s]
                for ss in p:
                    ls.append(ss)
                listOfSubstrings.append(ls)
    memo[targetString] = listOfSubstrings
    return listOfSubstrings


if __name__ == "__main__":
    print("targetString: abcdef, Array:[ab, abc, cd, def, abcd]", allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print("targetString: purple, Array:[purp, p, ur, le, purpl]", allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print("targetString: skateboard, Array:[bo, rd, ate, t, ska, sk, boar]", allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print("targetString: enterapotentpot, Array:[a, p, ent, enter, ot, o, t]", allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print("targetString: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef, Array:[e, ee, eee, eeee, eeeee]", allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))
