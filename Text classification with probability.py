
__author__="rojin.varghese"
__date__ ="$Nov 8, 2013 8:48:18 PM$"

import os
from xlrd import open_workbook
import re
import xlwt
j = os.path.join

def train(text):
    c = {}
    lastword = ""
    line = re.sub('[\-#*>]', '', text)
    line = re.sub('[\n]', '', line)
    for word in line.split():
        word = word.lower()
        if c.has_key(lastword):
            inner = c[lastword]
            if inner.has_key(word):
                inner[word] += 1
            else:
                inner[word] = 1
        else:
            c[lastword] = {word: 1}
        lastword = word
    return c

def probability_of(dict, lastword, word):
    
    word = word.lower()
    if dict.has_key(lastword):
        inner = dict[lastword]
        sumvalues = sum([v for v in inner.values()])
        if inner.has_key(word):
            return inner[word] / (sumvalues * 1.0)
    return 0

def classify(text, dict):

    lastword = ""
    probabilities = 0
    line = re.sub('[\-#*>]', '', text)
    line = re.sub('[\n]', '', line)
    for word in line.split():
        probabilities += probability_of(dict, lastword, word)
        lastword = word
    return probabilities / (len(text.split()) * 1.0)

if __name__ == "__main__":
    
    ranking = []

    book = open_workbook('C:/Documents and Settings/rojin.varghese/Desktop/Test_mail.xls')
    sheet1 = book.sheet_by_index(0)
    book1 = xlwt.Workbook()
    sh = book1.add_sheet("sheet")

    
    for i in range(sheet1.nrows):

      line = sheet1.cell_value(i,1)
      line = re.sub('[\-*>]', '', line)
      line = re.sub('[\n]', '', line)
      for file in os.listdir("C:/Documents and Settings/rojin.varghese/Desktop/ICICI_emails"):
          trained = train(open(j("C:/Documents and Settings/rojin.varghese/Desktop/ICICI_emails", file)).read())
          value = classify(line, trained)
          ranking.append((value, file))

      sh.write(i, 0, ranking[-1][1])
      sh.write(i, 1, ranking[-2][1])
      book1.save("C:/Documents and Settings/rojin.varghese/Desktop/Results/ProbabilityResult.xls")


    
