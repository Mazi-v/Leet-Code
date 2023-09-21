"Implement Trie (Prefix Tree)"
class Trie:

    def __init__(self):
        self.Tries = [None]*26
        self.is_valid = False


    def insert(self, word: str) -> None: 
        if len(word) == 0:
            self.is_valid = True
            return
        pos = ord(word[0]) - ord('a')
        if self.Tries[pos] == None:
            self.Tries[pos] = Trie()
        self.Tries[pos].insert(word[1:])
        

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.is_valid
        pos = ord(word[0]) - ord('a')
        if self.Tries[pos] == None:
            return False
        return self.Tries[pos].search(word[1:])

    def startsWith(self, word: str) -> bool:
        if len(word) == 0:
            return True
        pos = ord(word[0]) - ord('a')

        if self.Tries[pos] == None:
            return False
        return self.Tries[pos].startsWith(word[1:])


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)