
__author__="rojin.varghese"
__date__ ="$Dec 10, 2013 1:46:18 PM$"

from xlrd import open_workbook
import re
from xlrd import open_workbook
import xlwt


call_id = [];
keywordfound = [];
temp = []

book = open_workbook('C:/Documents and Settings/rojin.varghese/Desktop/LargeTest/Total.xls')
sheet = book.sheet_by_index(0)

book1 = open_workbook('C:/Documents and Settings/rojin.varghese/Desktop/LargeTest/Keywords.xls')
sheet1 = book1.sheet_by_index(0)

for j in range(sheet.nrows):
    line = sheet.cell_value(j,0)
    call_id.append(line);
    line = sheet.cell_value(j,1)
    line = re.sub('[-*>]', '', line)
    line = re.sub('[\n]', '', line)
    line = line.lower()

    for i in range(4):
        line1 = sheet1.cell_value(i,0)
        line1 = line1.lower()
        line1 = re.split(', ', line1)

        for x in line1:
           a = len(line)
           b = len(line.replace(x , ""))
           c = len(x)
           if (a-b) != 0:
              keywords = (a - b)/c
              keywordfound.append((i,0,j,x,keywords))

        line2 = sheet1.cell_value(i,1)
        line2 = line2.lower()
        line2 = re.split(', ', line2)

        for x in line2:
           a = len(line)
           b = len(line.replace(x , ""))
           c = len(x)
           if (a-b) != 0:
              keywords = (a - b)/c
              keywordfound.append((i,1,j,x,keywords))

        line3 = sheet1.cell_value(i,2)
        line3 = line3.lower()
        line3 = re.split(', ', line3)

        for x in line3:
           a = len(line)
           b = len(line.replace(x , ""))
           c = len(x)
           if (a-b) != 0:
              keywords = (a - b)/c
              keywordfound.append((i,2,j,x,keywords))

        line4 = sheet1.cell_value(i,3)
        line4 = line4.lower()
        line4 = re.split(', ', line4)

        for x in line4:
           a = len(line)
           b = len(line.replace(x , ""))
           c = len(x)
           if (a-b) != 0:
              keywords = (a - b)/c
              keywordfound.append((i,3,j,x,keywords))

        line5 = sheet1.cell_value(i,4)
        line5 = line5.lower()
        line5 = re.split(', ', line5)

        for x in line5:
           a = len(line)
           b = len(line.replace(x , ""))
           c = len(x)
           if (a-b) != 0:
              keywords = (a - b)/c
              keywordfound.append((i,4,j,x,keywords))


book2 = xlwt.Workbook()
sh1 = book2.add_sheet("Catg_TypeA")
sh2 = book2.add_sheet("Catg_TypeB")
sh3 = book2.add_sheet("Catg_TypeC")
sh4 = book2.add_sheet("Catg_TypeD")
sh5 = book2.add_sheet("Catg_TypeE")
sh6 = book2.add_sheet("Mastr_TypeA")
sh7 = book2.add_sheet("Mastr_TypeB")
sh8 = book2.add_sheet("Mastr_TypeC")
sh9 = book2.add_sheet("Mastr_TypeD")
sh10 = book2.add_sheet("Mastr_TypeE")
sh11 = book2.add_sheet("call_TypeA")
sh12 = book2.add_sheet("call_TypeB")
sh13 = book2.add_sheet("call_TypeC")
sh14 = book2.add_sheet("call_TypeD")
sh15 = book2.add_sheet("call_TypeE")
sh16 = book2.add_sheet("Subcall_TypeA")
sh17 = book2.add_sheet("Subcall_TypeB")
sh18 = book2.add_sheet("Subcall_TypeC")
sh19 = book2.add_sheet("Subcall_TypeD")
sh20 = book2.add_sheet("Subcall_TypeE")

r1 = r2 = r3 = r4 = r5 = r6 = r7 = r8 = r9 = r10 = 0
r11 = r12 = r13 = r14 = r15 = r16 = r17 = r18 = r19 = r20 = 0

for a,b,c,d,e in keywordfound:

    if a == 0:

        if b == 0:
           sh1.write(r1, 0, d)
           sh1.write(r1, 1, e)
           sh1.write(r1, 2, c)
           r1 = r1+1
        elif b == 1 :
           sh2.write(r2, 0, d)
           sh2.write(r2, 1, e)
           sh2.write(r2, 2, c)
           r2 = r2+1
        elif b == 2 :
           sh3.write(r3, 0, d)
           sh3.write(r3, 1, e)
           sh3.write(r3, 2, c)
           r3 = r3+1
        elif b == 3 :
           sh4.write(r4, 0, d)
           sh4.write(r4, 1, e)
           sh4.write(r4, 2, c)
           r4 = r4+1
        elif b == 4 :
           sh5.write(r5, 0, d)
           sh5.write(r5, 1, e)
           sh5.write(r5, 2, c)
           r5 = r5+1
        book2.save("C:/Documents and Settings/rojin.varghese/Desktop/LargeTest/Keyword_numbes.xls")
    elif a == 1:

        if b == 0:
           sh6.write(r6, 0, d)
           sh6.write(r6, 1, e)
           sh6.write(r6, 2, c)
           r6 = r6+1
        elif b == 1 :
           sh7.write(r7, 0, d)
           sh7.write(r7, 1, e)
           sh7.write(r7, 2, c)
           r7 = r7+1
        elif b == 2 :
           sh8.write(r8, 0, d)
           sh8.write(r8, 1, e)
           sh8.write(r8, 2, c)
           r8 = r8+1
        elif b == 3 :
           sh9.write(r9, 0, d)
           sh9.write(r9, 1, e)
           sh9.write(r9, 2, c)
           r9 = r9+1
        elif b == 4 :
           sh10.write(r10, 0, d)
           sh10.write(r10, 1, e)
           sh10.write(r10, 2, c)
           r10 = r10+1
        book2.save("C:/Documents and Settings/rojin.varghese/Desktop/LargeTest/Keyword_numbes.xls")
    elif a == 2:
        
        if b == 0:
           sh11.write(r11, 0, d)
           sh11.write(r11, 1, e)
           sh11.write(r11, 2, c)
           r11 = r11+1
        elif b == 1 :
           sh12.write(r12, 0, d)
           sh12.write(r12, 1, e)
           sh12.write(r12, 2, c)
           r12 = r12+1
        elif b == 2 :
           sh13.write(r13, 0, d)
           sh13.write(r13, 1, e)
           sh13.write(r13, 2, c)
           r13 = r13+1
        elif b == 3 :
           sh14.write(r14, 0, d)
           sh14.write(r14, 1, e)
           sh14.write(r14, 2, c)
           r14 = r14+1
        elif b == 4 :
           sh15.write(r15, 0, d)
           sh15.write(r15, 1, e)
           sh15.write(r15, 2, c)
           r15 = r15+1
        book2.save("C:/Documents and Settings/rojin.varghese/Desktop/LargeTest/Keyword_numbes.xls")
    elif a == 3 :

        if b == 0:
           sh16.write(r16, 0, d)
           sh16.write(r16, 1, e)
           sh16.write(r16, 2, c)
           r16 = r16+1
        elif b == 1 :
           sh17.write(r17, 0, d)
           sh17.write(r17, 1, e)
           sh17.write(r17, 2, c)
           r17 = r17+1
        elif b == 2 :
           sh18.write(r18, 0, d)
           sh18.write(r18, 1, e)
           sh18.write(r18, 2, c)
           r18 = r18+1
        elif b == 3 :
           sh19.write(r19, 0, d)
           sh19.write(r19, 1, e)
           sh19.write(r19, 2, c)
           r19 = r19+1
        elif b == 4 :
           sh20.write(r20, 0, d)
           sh20.write(r20, 1, e)
           sh20.write(r20, 2, c)
           r20 = r20+1

        book2.save("C:/Documents and Settings/rojin.varghese/Desktop/LargeTest/Keyword_numbes.xls")
       

