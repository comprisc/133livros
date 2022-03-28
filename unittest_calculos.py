import unittest_contas

import calculos

#mentoria de sabado
class MyTestCase(unittest.TestCase):
    def test_subtrair_2_numeros(self):
        # Configura
        numeroA = 3500
        numeroB = 1500
        resultado_Esperado =  2000

        #Executa
        resultado_obtido = calculos.subtrair_2_numeros(numeroA, numeroB)

        #valida / Compara
        self.assertEqual(resultado_Esperado, resultado_obtido)  # add assertion here


if __name__ == '__main__':
    unittest.main()
