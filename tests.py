import unittest
import pandas as pd
from planilha_manager import gerar_cpf

class TestPlanilhaManager(unittest.TestCase):
    def test_gerar_cpf(self):
        cpf = gerar_cpf()
        self.assertTrue(len(cpf) == 11)  # Verifica se o CPF gerado tem 11 dígitos
        self.assertTrue(cpf.isdigit())  # Verifica se o CPF contém apenas dígitos

if __name__ == '__main__':
    unittest.main()
