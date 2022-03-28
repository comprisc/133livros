import pytest

def somar_2_numeros(numero1, numero2):
    return numero1 + numero2


def multiplicar_2_numeros(numero1, numero2):
    return numero1 * numero2

def dividir_2_numeros(numero1, numero2):
    try:
        return numero1 / numero2
    except ZeroDivisionError:
        return 'divisao por zero'



if __name__ == '__main__':

  resultado = somar_2_numeros(20, 30)
  print(f' O resutado da soma é {resultado}')

  resultado = multiplicar_2_numeros(5, 2)
  print(f' O resultado da multiplicação é {resultado}')

  resultado = dividir_2_numeros(10, 2)
  print(f' O resultado da multiplicação é {resultado}')
  #resultado é a variável










