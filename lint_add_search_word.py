#!/usr/bin/env python
# coding=utf-8

class WordDictionary:
    def __init__(self):
        self.root = {}
        self.END = '/'

    def addWord(self, word):
        node = self.root
        for l in word:
            node =  node.setdefault(l, {})
        node[self.END] = None

    def search(self, word, index = 0, node = {}):
        if index == 0:
            node = self.root
        if index == len(word) - 1:
            if node != {}:
                if word[index] == '.':
                    return True
                try:
                    return self.END in node[word[index]]
                except:
                    return False
            return False
        else:
            if word[index] != '.':
                if word[index] not in node:
                    return False
                node = node[word[index]]
                return self.search(word, index + 1, node)
            else:
                for l in node:
                    if self.search(word, index + 1, node[l]):
                        return True
                return False



wordDictionary = WordDictionary()
print wordDictionary.search(".")
wordDictionary.addWord("word")
wordDictionary.search("ford")
wordDictionary.addWord("a")
print wordDictionary.search("wo.d")
print wordDictionary.search(".")
print wordDictionary.search("wor.")
print wordDictionary.search("w...")
print wordDictionary.search("word")
print wordDictionary.search("wordl")
