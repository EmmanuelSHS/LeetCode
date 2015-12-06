"""
Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("lintcode")
trie.search("lint") will return false
trie.startsWith("lint") will return true
"""

class Trie:
  def __init__(self):
    self.root = {}
    self.END = '/'

  # @param {string} word
  # @return {void}
  # Inserts a word into the trie.
  def insert(self, word):
      node = self.root
      for l in word:
          # node assigned to node's children
          # in this case left node = {}
          node = node.setdefault(l, {})
      # assign an ending mark to words
      # must have an ending flag
      node[self.END] = None

  # @param {string} word
  # @return {boolean}
  # Returns if the word is in the trie.
  def search(self, word):
      node = self.root
      for l in word:
          if l not in node:
              return False
          node = node[l]
      return self.END in node
      # this returns T/F
      # if ended, END in, out T; else F

  # @param {string} prefix
  # @return {boolean}
  # Returns if there is any word in the trie
  # that starts with the given prefix.
  def startsWith(self, prefix):
      node = self.root
      for l in prefix:
          if l not in node:
              return False
          node = node[l]
      return True

trie = Trie()
trie.insert("xyz")
trie.insert("abc")
trie.insert("abn")
print trie.search("xyz")
print trie.startsWith("a")
