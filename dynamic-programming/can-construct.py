#Check if targetString can be constructed from list of strings 
def canConstruct(targetString, substrings, memo=None):
    if memo is None:
        memo={}
    if targetString in memo.keys():
        return memo[targetString]
    if targetString == "":
        return True
    
    for s in substrings:
        if targetString.startswith(s):
            if canConstruct(targetString[len(s):], substrings, memo=memo):
                memo[targetString] = True
                return True
    memo[targetString] = False
    return False

if __name__=="__main__":
    print("targetString: abcdef, Array:[ab, abc, cd, def, abcd]", canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print("targetString: skateboard, Array:[bo, rd, ate, t, ska, sk, boar]", canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print("targetString: enterapotentpot, Array:[a, p, ent, enter, ot, o, t]", canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print("targetString: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef, Array:[e, ee, eee, eeee, eeeee]", canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))