def allConstruct(targetString, substrings):
    n = len(targetString)
    arr = [[] for i in range(n+1)]
    arr[0].append([])
    
    for i in range(n):
        if len(arr[i]) == 0:
            continue
        for s in substrings:
            if targetString[i:].startswith(s):
                for x in arr[i]:
                    temp = [ss for ss in x]
                    temp.append(s)
                    arr[i+len(s)].append(temp)

    return arr[n]



if __name__ == "__main__":
    print("targetString: abcdef, Array:[ab, abc, cd, def, abcd]", allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print("targetString: purple, Array:[purp, p, ur, le, purpl]", allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print("targetString: skateboard, Array:[bo, rd, ate, t, ska, sk, boar]", allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print("targetString: enterapotentpot, Array:[a, p, ent, enter, ot, o, t]", allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print("targetString: eeeeeeeeeeeeef, Array:[e, ee, eee, eeee, eeeee]", allConstruct("eeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))
