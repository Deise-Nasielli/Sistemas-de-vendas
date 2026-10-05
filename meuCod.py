# ferramenta que seram usadas: streamlit, pandas, plotly
# streamlit run meuCod.py ou python -m streamlit run meuCod.py
# título - sistema de vendas
# Seção cadastrar vendas
    #Campo Data
    # Campo Vendedor - Gertrudes, Godofredo, Gandalf
    # Campo Produto - Notebook, Fone, celular
    # Campo quantidade
    # BOTAO Cadastrar#
# Seção vendas cadastrada
    #tabelas com as vendas
        # quando clicar no btn quenho q add a venda na tabela
# secção dashboard
    # Card/metrica - faturamento total
    # Gráfico de barras/coluna - vendas por vendedor
    #Grafico de pizza - venda por produto

import streamlit as st
import pandas as pd
import plotly.express as px

# carregar a base de vendas
tabelaVendas = pd.read_csv('vendas.csv')

st.write("# Sistema de Vendas")

# secao de cadastro de vendas
st.sidebar.write('### Cadastrar vendas')
data = st.sidebar.date_input('Data')
vendedor = st.sidebar.selectbox('Vendedor', ['Gertrudes', 'Godofredo', 'Gandalf'])
produto = st.sidebar.selectbox('Produto',['Notebook', 'Fone', 'Celular'])
quantidade = st.sidebar.number_input('Quantidade', step=1)
valor = st.sidebar.number_input('Valor')
botaoCadastrar = st.sidebar.button('Cadastrar venda')
# logica - quando clicar no btn quero que add a venda na tabela
if botaoCadastrar:
    if valor == 0 or quantidade == 0 or data == '' or vendedor == '' or produto == '':
        st.warning('Preencha todos os campos corretamente!')
    novaVenda = [str(data), vendedor, produto, quantidade, valor]
    ultimaLinha = len(tabelaVendas)
    tabelaVendas.loc[ultimaLinha]=novaVenda
    tabelaVendas.to_csv('vendas.csv', index=False)
    st.success('Venda cadastrada com sucesso!')
# secao de visualizar as vendas 
st.write('### Vendas cadastradas')
st.dataframe(tabelaVendas)

# secção dashboard
st.write('### Dashboard')
# Card/metrica - faturamento total
faturamentoTotal = tabelaVendas['valor'].sum()
faturamentoFormatado = f"{faturamentoTotal:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
st.metric('Faturamento total:', f'R$: {faturamentoFormatado}')
# Gráfico de barras/coluna - vendas por vendedor
graficoBarra = px.bar(tabelaVendas, x='vendedor', y='valor', color='produto')
st.plotly_chart(graficoBarra)
# Grafico de pizza - venda por produto
graficoPizza = px.pie(tabelaVendas, names='produto', values='valor', hole=0.4)
st.plotly_chart(graficoPizza)
