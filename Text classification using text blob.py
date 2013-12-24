from text.classifiers import NaiveBayesClassifier
from text.blob import TextBlob
import os
from xlrd import open_workbook
import re
import xlwt

train = []

book = open_workbook('C:/Documents and Settings/rojin.varghese/Desktop/LargeTest/One_Category_Train.xls')
sheet1 = book.sheet_by_index(0)
print "Training.............\n"
for j in range(sheet1.nrows):
      line1 = sheet1.cell_value(j,1)
      line1 = re.sub('[\-*>]', '', line1)
      line1 = re.sub('[\n]', '', line1)
      line2 = sheet1.cell_value(j,2)
      stored = [(line1, line2)]
      train = train + stored

print  "Training algo....\n"
cl = NaiveBayesClassifier(train)

book = open_workbook('C:/Documents and Settings/rojin.varghese/Desktop/LargeTest/One_Category_Test.xls')
sheet = book.sheet_by_index(0)

book1 = xlwt.Workbook()
sh = book1.add_sheet("sheet")

print "Classifying..........."

for j in range(sheet.nrows):
    id = sheet.cell_value(j,0)
    line = sheet.cell_value(j,1)
    line = re.sub('[-*>]', '', line)
    line = re.sub('[\n]', '', line)
    a = cl.classify(line)
    sh.write(j, 0, id)
    sh.write(j, 1, a)
    
book1.save("C:/Documents and Settings/rojin.varghese/Desktop/LargeTest/One_Category_result_new.xls")

