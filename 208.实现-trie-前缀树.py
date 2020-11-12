#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start

#Tips: design, trie

class TrieNode:
    def __init__(self, val=None, is_end=False):
        self.val=val
        self.next_node_dict = {}
        self.is_end = is_end


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i in word:
            if i not in node.next_node_dict:
                node.next_node_dict[i] = TrieNode(i)
            node = node.next_node_dict[i]
        node.is_end = True
        return

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for i in word:
            if i not in node.next_node_dict:
                return False
            node = node.next_node_dict[i]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for i in prefix:
            if i not in node.next_node_dict:
                return False
            node = node.next_node_dict[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

