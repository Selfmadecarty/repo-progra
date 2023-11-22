numeros = [1, 2, 3, 4, 5]

def multiplicar_lista(lista):
    resultado = 1
    for elemento in lista:
        resultado *= elemento
    return resultado

print(multiplicar_lista(numeros))