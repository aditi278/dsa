def countConstruct(targetString, substrings):
    n = len(targetString)
    arr = [0]*(n+1)
    arr[0] = 1

    for i in range(n):
        if arr[i] == 0:
            continue
        for s in substrings:
            if targetString[i:].startswith(s):
                arr[i+len(s)]+=arr[i]
    return arr[n]



if __name__ == "__main__":
    print("targetString: abcdef, Array:[ab, abc, cd, def, abcd]", countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print("targetString: purple, Array:[purp, p, ur, le, purpl]", countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print("targetString: skateboard, Array:[bo, rd, ate, t, ska, sk, boar]", countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print("targetString: enterapotentpot, Array:[a, p, ent, enter, ot, o, t]", countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print("targetString: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef, Array:[e, ee, eee, eeee, eeeee]", countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))
