import pandas as pd
import os
import faker

# Inicializa o gerador de dados falsos
faker_generator = faker.Faker()

# Função para gerar CPFs falsos
def gerar_cpf():
    return faker_generator.ssn()

# Caminho para a planilha de dados
caminho_planilha = 'C:/Users/lLean/Downloads/Cópia_de_Vendas.xlsx'

# Verifica se o arquivo existe
if not os.path.isfile(caminho_planilha):
    print(f"Arquivo não encontrado: {caminho_planilha}")
    exit()

# Carrega a planilha
planilha = pd.ExcelFile(caminho_planilha)

# Exibe as abas disponíveis
print("Abas disponíveis:", planilha.sheet_names)

# Tenta carregar os dados das abas
try:
    vendas_df = pd.read_excel(caminho_planilha, sheet_name='Vendas')
    pagamentos_df = pd.read_excel(caminho_planilha, sheet_name='Pagamentos')
except ValueError as e:
    print(f"Erro ao carregar as abas: {e}")
    exit()

# Adiciona coluna de CPF aos dados de vendas
vendas_df['CPF'] = [gerar_cpf() for _ in range(len(vendas_df))]

# Combina os dados das abas
dados_combinados = pd.merge(vendas_df, pagamentos_df, on='Nome do Vendedor', how='left')

# Salva os dados combinados em um novo arquivo Excel
caminho_salvamento = 'C:/Users/lLean/Downloads/Dados_Combinados.xlsx'
dados_combinados.to_excel(caminho_salvamento, index=False)

print(f"Dados combinados salvos em: {caminho_salvamento}")
