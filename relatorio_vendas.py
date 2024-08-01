import pandas as pd

# Função para gerar relatórios de vendas
def gerar_relatorio_vendas(vendas_df):
    # Verifica os tipos das colunas e tenta converter para numérico
    vendas_df['Valor da Venda'] = pd.to_numeric(vendas_df['Valor da Venda'], errors='coerce')
    vendas_df['Custo da Venda'] = pd.to_numeric(vendas_df['Custo da Venda'], errors='coerce')
    
    # Agrupa por 'Nome do Vendedor' e calcula as métricas desejadas
    relatorio = vendas_df.groupby('Nome do Vendedor').agg({
        'Valor da Venda': ['sum', 'mean', 'count'],
        'Custo da Venda': 'sum'
    }).reset_index()
    
    # Ajusta os nomes das colunas do DataFrame
    relatorio.columns = ['Nome do Vendedor', 'Total de Vendas', 'Média de Vendas', 'Número de Vendas', 'Total de Custos']
    
    return relatorio

# Função para gerar relatórios de pagamentos
def gerar_relatorio_pagamentos(pagamentos_df):
    # Verifica os tipos das colunas e tenta converter para numérico
    pagamentos_df['Valor do Pagamento'] = pd.to_numeric(pagamentos_df['Valor do Pagamento'], errors='coerce')
    
    # Agrupa por 'Nome do Vendedor' e calcula as métricas desejadas
    relatorio = pagamentos_df.groupby('Nome do Vendedor').agg({
        'Valor do Pagamento': ['sum', 'mean', 'count']
    }).reset_index()
    
    # Ajusta os nomes das colunas do DataFrame
    relatorio.columns = ['Nome do Vendedor', 'Total de Pagamentos', 'Média de Pagamentos', 'Número de Pagamentos']
    
    return relatorio

# Exemplo de uso
if __name__ == "__main__":
    caminho_planilha_atualizada = r'C:\Users\lLean\Downloads\Cópia_de_Vendas.xlsx'  # Altere para o caminho correto da sua planilha
    
    try:
        # Lista as planilhas disponíveis
        excel_file = pd.ExcelFile(caminho_planilha_atualizada)
        print("Planilhas disponíveis:", excel_file.sheet_names)
        
        # Leitura das planilhas
        vendas_df = pd.read_excel(caminho_planilha_atualizada, sheet_name='Vendas')  # Ajuste o nome da planilha se necessário
        pagamentos_df = pd.read_excel(caminho_planilha_atualizada, sheet_name='Pagamentos')  # Ajuste o nome da planilha se necessário
        
        # Exibe uma amostra dos dados para verificação
        print("\nAmostra de Dados de Vendas:")
        print(vendas_df.head())
        print("\nAmostra de Dados de Pagamentos:")
        print(pagamentos_df.head())
        
        # Geração dos relatórios
        relatorio_vendas = gerar_relatorio_vendas(vendas_df)
        relatorio_pagamentos = gerar_relatorio_pagamentos(pagamentos_df)
        
        # Exibe os relatórios
        print("\nRelatório de Vendas:")
        print(relatorio_vendas)
        
        print("\nRelatório de Pagamentos:")
        print(relatorio_pagamentos)
    
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_planilha_atualizada}")
    
    except ValueError as e:
        print(f"Erro ao ler a planilha: {e}")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
