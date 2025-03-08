import streamlit as st
import pandas as pd
from data_processing import carregar_dados, separar_generos, separar_por_decadas, criar_lista_decada, separar_por_altura, separar_por_peso, Banco

def main():
    st.set_page_config(page_title="Análise de Dados", layout="wide")
    
    st.title("📊 Análise de Dados - Por Willian Batista Oliveira")
    st.subheader("Trabalho 8 - Professor Lúcio Renan Vieira")

    dados = carregar_dados()
    
    if dados is None:
        st.error("❌ Erro ao carregar os dados. Verifique se o arquivo `ARQUIVO_DE_DADOS.py` contém dados válidos.")
        return
    
    opcoes = [
        "Selecionar análise",
        "1️⃣ Listar Gênero Masculino/Feminino",
        "2️⃣ Separar Pessoas por Décadas",
        "3️⃣ Criar Lista para Cada Década",
        "4️⃣ Separar por Altura Progressiva",
        "5️⃣ Separar por Peso",
        "6️⃣ Banco de dados completo original"
    ]
    
    escolha = st.sidebar.selectbox("📌 Escolha uma análise:", opcoes)
    
    if escolha == "1️⃣ Listar Gênero Masculino/Feminino":
        df_masc, df_femi = separar_generos(dados)
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("👨 Gênero Masculino")
            st.dataframe(df_masc, use_container_width=True)
            csv_masc = df_masc.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Baixar CSV Masculino", csv_masc, "masculino.csv", "text/csv")
        with col2:
            st.subheader("👩 Gênero Feminino")
            st.dataframe(df_femi, use_container_width=True)
            csv_femi = df_femi.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Baixar CSV Feminino", csv_femi, "feminino.csv", "text/csv")
    
    elif escolha == "2️⃣ Separar Pessoas por Décadas":
        decadas = separar_por_decadas(dados)
        
        st.subheader("📆 Separação por Décadas")
        
        for decada, df in decadas.items():
            st.subheader(f"📌 Década de {decada}")
            if df.empty:
                st.warning("Nenhuma pessoa encontrada nesta década.")
            else:
                st.dataframe(df, use_container_width=True)
                
                csv_decada = df.to_csv(index=False).encode('utf-8')
                st.download_button(f"📥 Baixar CSV Década {decada}", csv_decada, f"decada_{decada}.csv", "text/csv")

    elif escolha == "3️⃣ Criar Lista para Cada Década":
        df_nomes, df_idades = criar_lista_decada(dados)
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📖 Tabela de Nomes por Década")
            st.dataframe(df_nomes, use_container_width=True)
            csv_nomes = df_nomes.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Baixar CSV Nomes", csv_nomes, "nomes_decadas.csv", "text/csv")
        with col2:
            st.subheader("📆 Tabela de Idade por Década")
            st.dataframe(df_idades, use_container_width=True)
            csv_idades = df_idades.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Baixar CSV Idades", csv_idades, "idades_decadas.csv", "text/csv")
    
    elif escolha == "4️⃣ Separar por Altura Progressiva":
        df_altura, df_altura_grupos = separar_por_altura(dados)
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📏 Tabela de Alturas Progressivas")
            st.dataframe(df_altura, use_container_width=True)
            csv_altura = df_altura.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Baixar CSV Alturas", csv_altura, "alturas.csv", "text/csv")
        with col2:
            st.subheader("📊 Tabela de Agrupamento por Altura")
            st.dataframe(df_altura_grupos, use_container_width=True)
            csv_altura_grupos = df_altura_grupos.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Baixar CSV Agrupamento Altura", csv_altura_grupos, "alturas_grupos.csv", "text/csv")
    
    elif escolha == "5️⃣ Separar por Peso":
        df_peso = separar_por_peso(dados)
        st.subheader("⚖️ Separação por Peso")
        st.dataframe(df_peso, use_container_width=True)
        csv_peso = df_peso.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Baixar CSV", csv_peso, "pesos.csv", "text/csv")
    
    elif escolha == "6️⃣ Banco de dados completo original":
        Banco(dados)

if __name__ == "__main__":
    main()
