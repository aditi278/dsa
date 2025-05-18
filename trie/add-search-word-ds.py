class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for x in word:
            if x not in curr.children:
                curr.children[x] = Trie()
            curr = curr.children[x]
        curr.endOfWord = True   

    def search(self, word: str, curr=None) -> bool:
        if curr is None:
            curr = self.root
        for x in word:
            if x == '.':
                exists = False
                newWord = word.split('.', 1)[1]
                for y in curr.children:
                    if len(newWord) == 0:
                        if curr.children[y].endOfWord:
                            return True
                    else:
                        exists = exists or self.search(newWord, curr.children[y])
                return exists
            elif x not in curr.children:
                return False
            curr = curr.children[x]
        return curr.endOfWord