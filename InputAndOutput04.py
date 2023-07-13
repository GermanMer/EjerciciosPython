#Exercise 4: Display float number with 2 decimal places using print()
#Given: num = 458.541315
#Expected Output: 458.54

given_num = 458.541315
print('%.2f' % given_num)

#'%.2f', es una cadena de formato que especifica cómo se va a formatear un número de punto flotante (float).
    #%, es el operador de formato utilizado para insertar un valor en una cadena.
    #.2, indica que se deben mostrar dos decimales después del punto decimal.
    #f, indica que el valor que se insertará será un número de punto flotante.
#% given_num, es el valor que se va a insertar en la cadena de formato.
    #El operador % se utiliza para realizar esta inserción.
    #El valor given_num se colocará en el lugar de %f en la cadena de formato.
