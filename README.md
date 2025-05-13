# 📊 Projeto ETL Sales Insights

Este projeto realiza um processo completo de ETL com Python e pandas, carrega os dados em um banco MySQL, exporta os dados tratados e exibe uma dashboard interativa com Streamlit e Plotly.

---

## 📁 Estrutura do Projeto

```
etl_sales_insights/
├── raw/             # CSV original gerado com dados fictícios
├── ready/           # CSV tratado após o ETL
├── src/
│   ├── etl.ipynb      # ETL com pandas + SQLAlchemy
│   └── dashboard.py      # Dashboard interativa com Streamlit + Plotly
├── requirements.txt # Pacotes necessários
├── README.md        # Instruções e explicações do projeto
```

---

## 🧱 Etapas para rodar o projeto (Windows + VS Code)

### 1. Abra o terminal no VS Code dentro da pasta extraída:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Instale os pacotes:

```bash
pip install -r requirements.txt
```

---

## 🛢️ Banco de Dados MySQL

Crie o banco no seu MySQL Workbench com:

```sql
CREATE DATABASE db_vendas;
```

---

## 📒 Executar o notebook ETL

Abra o arquivo `src/etl.ipynb` no Jupyter e execute as células.

Ele irá:
- Ler o CSV de `raw/`
- Calcular receita e tratar a data
- Enviar para o MySQL (`db_vendas.vendas`)
- Exportar `vendas_tratadas.csv` para a pasta `ready/`

---

## 📈 Executar a Dashboard com Streamlit

Após rodar o ETL e com a `.venv` ativada, execute:

```bash
streamlit run src/dashboard.py
```

Abra o navegador em `http://localhost:8501`

A dashboard inclui:
- Filtros por região e produto
- Gráficos interativos (barras, linha, pizza)
- Indicadores de receita, vendas e quantidade

---

## ✅ Requisitos

- Python 3.x
- VS Code com extensão Jupyter
- MySQL (Workbench ou XAMPP)
- Navegador instalado para abrir o Streamlit

---

## 📌 Observação

Este é um **projeto de portfólio para fins de estudo**, idealizado para demonstrar domínio de ETL com Python, manipulação com pandas, conexão com banco de dados MySQL, e visualização de dados interativa com Streamlit.

