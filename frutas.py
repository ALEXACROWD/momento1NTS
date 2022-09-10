frutas = []
i = 0

while (i < 10):
    fruta = {}
    fruta['nombre'] = input("Digite el nombre de la fruta: ")
    fruta['color'] = input("Digite el color de la fruta: ")
    fruta['precio'] = input("Digite el valor de la fruta: ")
    i = i + 1
    frutas.append(fruta)
    
frutas.reverse()
    
print(frutas)