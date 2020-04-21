""" This module creates an extractor to extract where
    {pattern} occurs in {text}
"""

class Extractor:
    """Class for Extracting information"""

    def __init__(self, text, pattern):
        'Extractor ctor'
        self.text = text
        self.pattern = pattern

    def KMPMatch(self):
        'String matcher using Knuth-Morris-Pratt algorithm'
        n = len(self.text)
        m = len(self.pattern)
        fail = self.computeFail()
        i = 0
        j = 0
        while i < n:
            if (self.pattern[j] == self.text[i]): # match
                if j == m-1:
                    return i-m+1
                i += 1
                j += 1
            elif j > 0:
                j = fail[j-1]
            else:
                i += 1
        return -1 # no match

    def computeFail(self):
        fail = [None for i in range (len(self.pattern))]
        fail[0] = 0
        m = len(self.pattern)
        j = 0
        i = 1
        while i < m:
            if self.pattern[j] == self.pattern[i]: # j+1 chars match
                fail[i] = j+1
                i += 1
                j += 1
            elif j>0:   # j follows matching prefix
                j = fail[j-1]
            else:       # no match
                fail[i] = 0
                i += 1
        print(fail)
        return fail

match1 = Extractor("abacaabaccabacabaabb", "abacab")
print("Text to match: " + match1.text)
print("Pattern to find: " + match1.pattern)
print("Location matched: " + str(match1.KMPMatch()))
