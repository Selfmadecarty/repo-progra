numeros = [1, 2, 3, 4, 5]

def multiplicar_lista(lista):
  resultado = 1
  for elemento in lista:
    resultado *= elemento
  return resultado

print(multiplicar_lista(numeros))

def suma_lista(lista):
  suma = 0
  for elemento in lista:
    suma += elemento
  return suma

print(suma_lista(numeros))