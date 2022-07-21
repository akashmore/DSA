class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for ele in word:
            if ele not in curr.children:
                curr.children[ele] = TrieNode()
            curr = curr.children[ele]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ele in word:
            if ele not in curr.children:
                return False
            curr = curr.children[ele]
        return curr.endOfWord
                

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ele in prefix:
            if ele not in curr.children:
                return False
            curr = curr.children[ele]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)