

def subtrair_2_numeros( numeroA, numeroB):# na linha da def o parentese serve para receber parametros/valores

    resultado = numeroA - numeroB
    return resultado

 # isso é um método que não retorna nada.
 # A função responde alguma coisa. Exemplo: Vc pede ifood ele te retorna o que vai e quando...
 # agora preciso chamar a função lá de cima.

if __name__ == '__main__':
    print(f'Calculos')
    resultado = subtrair_2_numeros(15,9)
    print(f'O resultado da subtração é: {resultado}')






