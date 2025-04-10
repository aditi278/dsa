def countConstruct(targetString, substrings, memo=None):
    if memo is None:
        memo = {}
    if targetString in memo.keys():
        return memo[targetString]
    if targetString == "":
        return 1
    
    count=0
    for s in substrings:
        if targetString.startswith(s):
            count+= countConstruct(targetString[len(s):], substrings, memo)
    memo[targetString] = count     
    return count


if __name__ == "__main__":
    print("targetString: abcdef, Array:[ab, abc, cd, def, abcd]", countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print("targetString: purple, Array:[purp, p, ur, le, purpl]", countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print("targetString: skateboard, Array:[bo, rd, ate, t, ska, sk, boar]", countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print("targetString: enterapotentpot, Array:[a, p, ent, enter, ot, o, t]", countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print("targetString: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef, Array:[e, ee, eee, eeee, eeeee]", countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))
