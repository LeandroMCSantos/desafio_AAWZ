import pandas as pd
import os

# Função para gerenciar dados dos vendedores
def gerenciar_vendedores(vendas_df):
    vendedores_unicos = vendas_df['Nome do Vendedor'].unique()
    return pd.DataFrame(vendedores_unicos, columns=['Nome do Vendedor'])

# Exemplo de uso
if __name__ == "__main__":
    caminho_planilha_atualizada = r'C:\Users\lLean\Downloads\Cópia_de_Vendas.xlsx'
    
    # Verificar se o arquivo existe
    if not os.path.isfile(caminho_planilha_atualizada):
        print(f"Arquivo não encontrado: {caminho_planilha_atualizada}")
    else:
        try:
            vendas_df = pd.read_excel(caminho_planilha_atualizada, sheet_name='Vendas')
            vendedores_df = gerenciar_vendedores(vendas_df)
            print(vendedores_df)
        except ValueError as e:
            print(f"Erro ao ler a planilha: {e}")
