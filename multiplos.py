numeros = int(input("Digite la cantidad de numeros que desea evaluar: "))

cont2 = 0
cont3 = 0
for n in range(numeros):
    num = int(input("Digite un numero: "))
    if num % 2 == 0 and num % 3 == 0:
        cont2 = cont2 + 1
        cont3 = cont3 + 1
    elif (num % 3 == 0):
        cont3 = cont3 + 1
    elif (num % 2 == 0):
        cont2 = cont2 + 1
    else:
        print("El número ingresado no es multimplos de 3 o de 2.")

print(f'La cantidad de mpultimos de 2 es:  {cont2}')
print(f'La cantidad de mpultimos de 3 es:  {cont3}')

