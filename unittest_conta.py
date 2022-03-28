import unittest

import main


class Casos_De_Teste(unittest.TestCase):

    lista_para_multiplicar = [
        (2, 3, 6),
        (0, 4, 0),
        (-5, -3, 15)
    ]
    def testar_multiplica_2_numeros(self):
        # Configura
        numero1 = 2
        numero2 = 4
        resultado_Esperado = 8

        # Executa
        resultado_obtido = main.multiplicar_2_numeros(numero1, numero2)


        # valida / Compara
        self.assertEqual(resultado_Esperado, resultado_obtido)  # add assertion here

    def testar_somar_dois_numeros(self):

        numero1 = 2
        numero2= 3
        resultado_Esperado = 5

        resultado_obtido = main.somar_2_numeros(numero1, numero2)

        self.assertEqual(resultado_Esperado, resultado_obtido)




if __name__ == '__main__':
    unittest.main()
