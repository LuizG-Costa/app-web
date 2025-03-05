import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout = "wide")

df_reviwes = pd.read_csv("customer reviews.csv")
df_top100_book = pd.read_csv("Top-100 Trending Books.csv")

# BARRA DE SELEÇÃO DE LIVROS 
books = df_top100_book["book title"].unique()
book = st.sidebar.selectbox("Books", books)

df_book = df_top100_book[df_top100_book["book title"] == book]
df_book_filter = df_reviwes[df_reviwes["book name"] == book]


book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price= f"${df_book['book price'].iloc[0]}"
book_rating= df_book["rating"].iloc[0]
book_yearPublication= df_book["year of publication"].iloc[0]

#COLOCANDO TITULO, SUBTITULO E DEMAIS INFORMAÇÕES 
st.title(book_title)
st.subheader(book_genre)

col1, col2, col3 = st.columns(3)
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of Publication", book_yearPublication)

st.divider()
# CONSTRUINDO UM FOR PARA PERCORRER AS REVIEWS DOS LIVROS 
for row in df_book_filter.values:
    massage = st.chat_message(f"{row[4]}")
    massage.write(f"**{row[2]}**")
    massage.write(row[5])
    