#Exercise 3: Slice list into 3 equal chunks and reverse each chunk

#Given:
#sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

#Expected Outcome:
#Chunk  1 [11, 45, 8]
#After reversing it  [8, 45, 11]
#Chunk  2 [23, 14, 12]
#After reversing it  [12, 14, 23]
#Chunk  3 [78, 45, 89]
#After reversing it  [89, 45, 78]

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

lenlist = len(sample_list)

tercio = lenlist // 3
tercio2 = int(tercio*2)

chunk1 = sample_list[:tercio]
chunk2 = sample_list[tercio:tercio2]
chunk3 = sample_list[tercio2:]

print('Chunk 1', chunk1)
print('After reversing it', chunk1[::-1])
print('Chunk 2', chunk2)
print('After reversing it', chunk2[::-1])
print('Chunk 3', chunk3)
print('After reversing it', chunk3[::-1])
