#Exercise 6: Write all content of a given file into a new file by skipping line number 5

#Given test.txt file:
#line1
#line2
#line3
#line4
#line5
#line6
#line7

#Expected Output: new_file.txt
#line1
#line2
#line3
#line4
#line6
#line7

fhandread = open('test.txt', 'r')
linelist = fhandread.readlines()
fhandread.close()
fhandwrite = open('new_file.txt', 'w')
contador = 0
for line in linelist:
    contador = contador + 1
    if contador != 5:
        fhandwrite.write(line)
    else: continue
fhandwrite.close()
