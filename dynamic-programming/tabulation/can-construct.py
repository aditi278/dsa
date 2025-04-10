def canConstruct(targetString, substrings):
    n = len(targetString)
    arr = [False]*(n+1)
    arr[0] = True
    for i in range(n):
        if not arr[i]:
            continue
        for s in substrings:
            if targetString[i:].startswith(s):
                arr[i+len(s)] = True
    return arr[n]

if __name__=="__main__":
    print("targetString: abcdef, Array:[ab, abc, cd, def, abcd]", canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print("targetString: skateboard, Array:[bo, rd, ate, t, ska, sk, boar]", canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print("targetString: enterapotentpot, Array:[a, p, ent, enter, ot, o, t]", canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print("targetString: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef, Array:[e, ee, eee, eeee, eeeee]", canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))