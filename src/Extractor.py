"""
This module loads file and extracts sentences
"""
from nltk.tokenize import sent_tokenize, word_tokenize
from Matcher import Matcher
import re

def findAmount(sent):
    toRead = sent.lower()
    patt = re.compile(r'(\d*\.?\d+)\s(orang?|kasus?)')
    # patt = re.compile(r'(sejumlah?|sebanyak?|orang?|kasus?\s?(\d*\.?\d+)\sorang?|kasus?)|((\d+[\.\,]\d+\spersen))')
    matches = patt.finditer(toRead)
    return matches


def findDate(sent):
    min = 99999
    max = 0
    patt = re.compile(r'\(+[1-3]?[0-9]\/[1]?[0-9]/\d\d\d\d\)+|Senin|Selasa|Rabu|Kamis|Jumat|Sabtu|Minggu|\d\d\:\d\d|WIB|WITA|WIT')
    matches = patt.finditer(sent)
    for x in matches:
        if x.start() < min:
            min = x.start()
        if x.end() > max:
            max = x.end()
    return sent[min:max]

def formatInfo(article)

class Extractor:
    'Class for extraction information from text, usually amount and time, based on keyword'

    def __init__(self, text, pattern, method):
        'Extractor ctor'
        self.text = text
        self.keyword = pattern
        self.method = method

    def findInfoWithMethod(self):
        result = []
        list_of_sentence = sent_tokenize(self.text)
        for sent in list_of_sentence:
            res = Matcher(sent.lower(), self.keyword)
            articleDate = ""
            if method == 'optionBM':
                r = res.BMMatch()
            elif method == 'optionKMP':
                r = res.KMPMatch()
            elif method == 'optionRE':
                r = res.REMatch()
            if r > -1:
                result.append(sent)
            if articleDate == "" or articleDate == " ":
                resDate = Matcher(sent, self.keyword) 
                # articleDate = resDate
        return result, articleDate

    def extractInformation(self):
        result, articleDate = self.findInfoWithMethod()
        for res in result:
            date = findDate(res)
            amount = findAmount(res)
                
            if date == "":
                date = articleDate


            print(res)
            print(findAmount(res))
            print(findDate(res))
    



def findInfo(toFind):
    pass

file = open('../test/coba.txt');

textToRead = file.read()
# EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

keyword = "terkonfirmasi positif"
method = "optionBM"

ex = Extractor(textToRead, keyword.lower(), method)
print(''' Tes
tEs
TesT''')

result, date = ex.findInfoWithMethod()

for res in result:
    print(res)
    print(findAmount(res))
    print(findDate(res))
""" 
list_of_sentence = sent_tokenize(textToRead)

date = ""

for sent in list_of_sentence:
    amount = 0
    print(sent)
    info = Matcher(sent.lower(), keyword.lower()) # find keyword
    if info.BMMatch() > -1:   #find amount
        for x in info.REFindAmount():
            print(x)
        info.setText(sent)
        date = info.REFindDate()
        
        
        print(date)

    print()
 """

