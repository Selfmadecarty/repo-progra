numeros = [1, 2, 3, 4, 5]

def suma_lista(lista):
  suma = 0
  for elemento in lista:
    suma += elemento
  return suma

print(suma_lista(numeros))