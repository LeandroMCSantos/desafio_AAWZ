import pandas as pd

# Função para calcular comissões
def calcular_comissoes(vendas_df, comissoes_df):
    # Verificar e converter os tipos de dados das colunas
    vendas_df['Valor da Venda'] = pd.to_numeric(vendas_df['Valor da Venda'], errors='coerce')
    comissoes_df['Comissão'] = pd.to_numeric(comissoes_df['Comissão'], errors='coerce')

    # Agrupar vendas por vendedor e somar o valor total de vendas
    total_vendas = vendas_df.groupby('Nome do Vendedor')['Valor da Venda'].sum()
    
    # Configurar o DataFrame de comissões com o índice de vendedor
    comissoes_df = comissoes_df.set_index('Nome do Vendedor')
    
    # Combinar o total de vendas com o DataFrame de comissões
    comissoes_totais = total_vendas.to_frame(name='Total de Vendas').join(comissoes_df)
    
    # Verificar se há valores NaN após a junção e preenchê-los com 0
    comissoes_totais = comissoes_totais.fillna(0)
    
    # Calcular a comissão total
    comissoes_totais['Comissão Total'] = comissoes_totais.apply(
        lambda row: row['Total de Vendas'] * row['Comissão'] / 100, axis=1
    )
    
    return comissoes_totais

# Exemplo de uso
if __name__ == "__main__":
    # Caminho para a planilha atualizada
    caminho_planilha = r'C:\Users\lLean\Downloads\Cópia_de_Vendas.xlsx'
    
    # Ler os dados das planilhas
    try:
        vendas_df = pd.read_excel(caminho_planilha, sheet_name='Vendas')  # Nome da aba de vendas
        comissoes_df = pd.read_excel(caminho_planilha, sheet_name='Pagamentos')  # Nome da aba de comissões
        
        # Calcular as comissões
        resultado = calcular_comissoes(vendas_df, comissoes_df)
        
        # Exibir o resultado
        print(resultado)
        
        # Opcional: salvar o resultado em um novo arquivo Excel
        resultado.to_excel(r'C:\Users\lLean\Downloads\Comissoes_Calculadas.xlsx', sheet_name='Comissões Calculadas')
        
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
