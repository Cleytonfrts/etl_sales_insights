
# 📊 Dashboard de Vendas com Streamlit + Plotly

import pandas as pd
import plotly.express as px
import streamlit as st

# 🧾 Carregando os dados tratados
df = pd.read_csv('ready/vendas_tratadas.csv')

# 🎯 Título da aplicação
st.set_page_config(page_title="Dashboard de Vendas", layout="wide")
st.title("📊 Dashboard de Vendas")

# 📆 Filtros interativos
col1, col2 = st.columns(2)

with col1:
    regioes = st.multiselect("Filtrar por Região:", df['regiao'].unique(), default=df['regiao'].unique())

with col2:
    produtos = st.multiselect("Filtrar por Produto:", df['produto'].unique(), default=df['produto'].unique())

# 🎯 Aplicar filtros
df_filtros = df[(df['regiao'].isin(regioes)) & (df['produto'].isin(produtos))]

# 📊 KPI cards
col1, col2, col3 = st.columns(3)
col1.metric("Receita Total", f"R$ {df_filtros['receita'].sum():,.2f}")
col2.metric("Total de Vendas", df_filtros['id_venda'].nunique())
col3.metric("Itens Vendidos", df_filtros['quantidade'].sum())

# 📈 Gráfico de barras - Receita por Região
fig1 = px.bar(df_filtros.groupby('regiao')['receita'].sum().reset_index(),
              x='regiao', y='receita', title='Receita por Região')
st.plotly_chart(fig1, use_container_width=True)

# 📉 Gráfico de linha - Receita por Data
fig2 = px.line(df_filtros.groupby('data')['receita'].sum().reset_index(),
               x='data', y='receita', title='Receita ao Longo do Tempo')
st.plotly_chart(fig2, use_container_width=True)

# 📊 Gráfico de pizza - Participação por Produto
fig3 = px.pie(df_filtros, values='receita', names='produto', title='Participação por Produto')
st.plotly_chart(fig3, use_container_width=True)
