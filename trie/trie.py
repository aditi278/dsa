class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()    

    def insert(self, word: str) -> None:
        curr = self.root
        for x in word:
            if x not in curr.children:
                curr.children[x] = TrieNode()
            curr = curr.children[x]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for x in word:
            if x not in curr.children:
                return False
            curr = curr.children[x]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for x in prefix:
            if x not in curr.children:
                return False
            curr = curr.children[x]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)