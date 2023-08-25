#Exercise 8: Generate a Python list of all the even numbers between 4 to 30

#Expected Output:
#[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

def even_numbers_between(start, end):
    lista = []
    for i in range(int(start), int(end)):
        if i % 2 == 0:
            lista.append(i)
        else: continue
    print(lista)

even_numbers_between(4, 30)
