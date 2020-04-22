"""
This module loads file and extracts sentences
"""
from nltk.tokenize import sent_tokenize, word_tokenize
from Matcher import Matcher
import re


def findAmount(sent):
    'Finds an essential amount in a sentence'
    toRead = sent.lower()
    patt = re.compile(r'(\d*\.?\,?\d+)\s(orang?|kasus?|jiwa?|tewas?|meninggal?|korban?|)')
    matches = patt.finditer(toRead)
    return matches

def findDate(sent):
    'Finds the date in a sentence'
    min = 99999
    max = 0
    patt = re.compile(r'\(+[1-3]?[0-9]\/[1]?[0-9]/\d\d\d\d\)+|\(\d+\/\d+\)|Senin|Selasa|Rabu|Kamis|Jumat|Sabtu|Minggu|\d\d\:\d\d|WIB|WITA|WIT|kemarin|minggu')
    matches = patt.finditer(sent)
    for x in matches:
        if x.start() < min:
            min = x.start()
        if x.end() > max:
            max = x.end()
    return sent[min:max]

def formatInfo(article, amount, date):
    'Formats the string'
    form = ("""
Jumlah: {}
Waktu: {}
{}""") 
    return form.format(amount, date, article)


class Extractor:
    'Class for extraction information from text, usually amount and time, based on keyword'

    def __init__(self, text, pattern, method):
        'Extractor ctor'
        self.text = text
        self.keyword = pattern
        self.method = method

    def findInfoWithMethod(self):
        'Finds and collects all needed information'
        result = []
        list_of_sentence = sent_tokenize(self.text)
        for sent in list_of_sentence:
            res = Matcher(sent.lower(), self.keyword)
            articleDate = ""
            r = 0
            if self.method == 'optionBM':
                r = res.BMMatch()
            elif self.method == 'optionKMP':
                r = res.KMPMatch()
            elif self.method == 'optionRE':
                r = res.REMatch()
            if r > -1:
                result.append(sent)
            if articleDate == "" or articleDate == " ":
                resDate = Matcher(sent, self.keyword) 
                # articleDate = resDate
        return result, articleDate

    def extractInformation(self):
        'Extracts the information from the file and returns as a formatted string'
        result, articleDate = self.findInfoWithMethod()
        forms = []
        for res in result:
            date = findDate(res)
            amount = []
            for a in findAmount(res):
                amount.append(a.group())

            if date == " ":
                date = articleDate

            forms.append(formatInfo(res, amount, date))

        return forms