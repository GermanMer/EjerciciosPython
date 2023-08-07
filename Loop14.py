#Exercise 14: Reverse a given integer number

#Given:
#76542

#Expected output:
#24567

number = 76542

reverse_number = 0

while number > 0:
    digito = number % 10
    reverse_number = (reverse_number * 10) + digito
    number = number // 10
print(reverse_number)
