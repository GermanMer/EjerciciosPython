#Exercise 10: Read line number 4 from the following file
#test.txt
#line1
#line2
#line3
#line4
#line5
#line6
#line7

fhand = open('test.txt')
lines = fhand.readlines()
print(lines[3])
fhand.close()
