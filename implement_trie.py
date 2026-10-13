"""
Pattern: Tries / Prefix Trees
Problem: Implement Trie (Prefix Tree) (LeetCode #208)
Description: A trie (pronounced as "try") or prefix tree is a tree-like data structure 
used to efficiently store and retrieve keys in a dataset of strings.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


# --- Test Cases ---
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print("Inserted: 'apple'")
    
    print(f"Search 'apple': {trie.search('apple')} (Expected: True)")
    print(f"Search 'app': {trie.search('app')} (Expected: False)")
    print(f"Starts with 'app': {trie.startsWith('app')} (Expected: True)")
    
    trie.insert("app")
    print("Inserted: 'app'")
    print(f"Search 'app' now: {trie.search('app')} (Expected: True)")