"""
This module loads file and extracts sentences
"""
from nltk.tokenize import sent_tokenize, word_tokenize
from Matcher import Matcher
from os import path
from Extractor import Extractor
import re
class Form:
    'Class for forming results based on folder input'   
    def __init__(self, filename, keyword, method):
        'Form ctor'
        self.filename = filename
        self.article = ""
        self.info = []
        self.keyword = keyword.lower()
        self.method = method

    def readFile(self):
        'Reads file from filename and puts results in info'
        file = open(path.join('static', 'files', self.filename));
        self.article = file.read()
        extract = Extractor(self.article, self.keyword, self.method)
        self.info = extract.extractInformation()
