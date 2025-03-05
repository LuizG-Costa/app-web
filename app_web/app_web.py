import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout = "wide")

df_reviwes = pd.read_csv("customer reviews.csv")
df_top100_book = pd.read_csv("Top-100 Trending Books.csv")



price_max = df_top100_book["book price"].max()
price_min = df_top100_book["book price"].min()


# DEFINIDOR DE PREÇO
price_filter = st.sidebar.slider("Price of books in US$", price_min, price_max, price_max)
df_100books = df_top100_book[df_top100_book["book price"] <= price_filter]
df_100books 


# DEFININDO OS GRAFICO EM BARRA E COLUNA
col1, col2 = st.columns(2)

graf_bar = px.bar(df_100books["year of publication"].value_counts())
col1.plotly_chart (graf_bar)


graf_hist = px.histogram(df_100books["book price"])
col2.plotly_chart (graf_hist)
