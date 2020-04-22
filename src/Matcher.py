""" This module creates an matcher to indicate where
    {pattern} occurs in {text}
"""
import re

class Matcher:
    """Class for matching pattern on a given text"""

    def __init__(self, text, pattern):
        'Matcher ctor'
        self.text = text
        self.pattern = pattern

    def setText(self, text):
        'Sets the text to read'
        self.text = text

    def setPattern(self, pattern):
        'Sets the pattern to match'
        self.patterm = pattern

    def BMMatch(self):
        'String matcher using Boyer-Moore Algorithm'
        last = self.computeLastOccurence();
        n = len(self.text)
        m = len(self.pattern)
        i = m-1
        if i > n-1:
            return -1   # no match if pattern longer than text
        j = m-1
        while 1:
            if self.pattern[j] == self.text[i]:
                if j == 0:
                    return i	# found match
                else:
                    i -= 1
                    j -= 1
            else:
                lastOcc = last[ord(self.text[i])]	# last occurance
                i = i + m - min([j, 1+lastOcc])
                j = m - 1
            if i > n-1:
                break
        return -1		# no match

    def computeLastOccurence(self):
        'Returns array storing index of last occurence of each ASCII character in pattern'
        last = [-1 for x in range(128)]
        for i in range (len(self.pattern)):
            last[ord(self.pattern[i])] = i
        return last


    def KMPMatch(self):
        'String matcher using Knuth-Morris-Pratt Algorithm'
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
        'Returns array storing size where repeating patterns happen'
        fail = [0 for i in range (len(self.pattern))]
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

    def REMatch(self):
        pa = self.pattern
        patt = re.compile(self.pattern)
        matches = patt.search(self.text) == None
        if matches:
            return -1
        else:
            return 1
