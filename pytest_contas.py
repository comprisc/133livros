import pytest
import csv
import main

lista_para_multiplicar = [
    (2, 3, 6),
    (0, 4, 0),
    (-5, -3, 15),
    (8, 1000, 8000),
    (7, '', ''),
    (9, ' ', '         '),
    (10, 'a', 'aaaaaaaaaa')
]
@pytest.mark.parametrize('numero1, numero2, resultado_esperado', lista_para_multiplicar)
def teste_multiplicar_2_numeros(numero1, numero2, resultado_esperado):
    # Configura - virá da lista

    # Executa
    
    resultado_obtido = main.multiplicar_2_numeros(int(numero1), int(numero2))

    # Valida
    assert float (resultado_obtido) == resultado_esperado

 #Vamos escrever a função para utilizar a lita ane

def ler_dados_csv():
    dados_csv = []  #criamos uma lista vazia
    nome_arquivo = 'vendors/massa_dividir_2_numeros.csv'
    try:
        with open(nome_arquivo, newline='') as arquivo_csv:
            campos = csv.reader(arquivo_csv, delimiter=';')
            next(campos)
            for linha  in campos:
                dados_csv.append(linha)
        return dados_csv  #está retornando lá naquela lisata vazia de cima
    except FileNotFoundError:
          print (f'Arquivo não encontrado: {nome_arquivo}')
    except Exception as fail:
          print (f'Falha não prevista: {fail}')

@pytest.mark.parametrize('numero1, numero2, resultado_esperado', ler_dados_csv())
def teste_dividir_2_numeros(numero1,numero2, resultado_esperado):
    #os valores agora vem da lista
    #Configura
    #numero1 = 9
    #numero2 = 2

    #resultado_esperado = 4.5

    #Executa
    resultado_obtido = main.dividir_2_numeros(numero1, numero2)

    #Valida
    assert resultado_obtido == resultado_esperado











