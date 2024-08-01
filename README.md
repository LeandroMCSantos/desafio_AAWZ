# Desafio Técnico

## Descrição

Este projeto visa gerenciar e analisar dados de vendas e comissões de vendedores.

## Arquivos

- `planilha_manager.py`: Script para ler a planilha, adicionar CPFs e salvar o arquivo atualizado.
- `calculadora_comissoes.py`: Script para calcular comissões com base nas vendas.
- `relatorio_vendas.py`: Script para gerar relatórios de vendas.
- `vendedor_manager.py`: Script para gerenciar dados dos vendedores.
- `tests.py`: Testes para verificar a funcionalidade dos scripts.

## Como Executar

1. Ative seu ambiente virtual:
    ```bash
    .\venv\Scripts\activate
    ```
2. Execute os scripts conforme necessário:
    ```bash
    python planilha_manager.py
    python calculadora_comissoes.py
    python relatorio_vendas.py
    python vendedor_manager.py
    ```
3. Execute os testes:
    ```bash
    python tests.py
    ```

## Dependências

- pandas
- numpy
- openpyxl

Instale as dependências usando:
```bash
pip install pandas numpy openpyxl
