import pandas as pd
import matplotlib.pyplot as plt

# Ler a planilha
df = pd.read_excel('vendas.xlsx', engine='openpyxl')

# Calcular total por produto
df['Total'] = df['Quantidade'] * df['Preço Unitário']
total_vendas = df['Total'].sum()

print("Resumo das vendas:")
print(df)
print(f"\nTotal de vendas: R$ {total_vendas:.2f}")

# Gerar gráfico
df.plot(kind='bar', x='Produto', y='Total', title='Vendas por Produto')
plt.ylabel('Total em R$')
plt.savefig('grafico_vendas.png')
plt.show()

# Salvar relatório novo
df.to_excel('relatorio_vendas.xlsx', index=False)
print("Relatório salvo como 'relatorio_vendas.xlsx' e gráfico como 'grafico_vendas.png'")