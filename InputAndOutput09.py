#Exercise 9: Check file is empty or not
#Write a program to check if the given file is empty or not

import os
if os.stat('test.txt').st_size == 0:
  print('File is empty.')
else:
  print('File is not empty.')
