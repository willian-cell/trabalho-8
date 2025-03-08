import pandas as pd
import streamlit as st

def carregar_dados():
    """Carrega os dados do arquivo e retorna um DataFrame limpo."""
    try:
        colunas = ["Nome", "Gênero", "Altura", "Peso", "Ano"]
        dados = pd.read_csv("ARQUIVO_DE_DADOS.py", names=colunas)
        
        # Limpeza e conversão dos dados
        dados["Gênero"] = dados["Gênero"].str.upper().str.strip()
        dados["Altura"] = pd.to_numeric(dados["Altura"].str.replace("m", ""), errors='coerce')
        dados["Peso"] = pd.to_numeric(dados["Peso"].str.replace("kg", ""), errors='coerce')
        dados["Ano"] = pd.to_numeric(dados["Ano"], errors='coerce')
        
        return dados.dropna()
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return None

def separar_generos(dados):
    """Separa os dados por gênero."""
    return dados[dados["Gênero"] == "M"], dados[dados["Gênero"] == "F"]

def separar_por_decadas(dados):
    """Organiza os dados em décadas."""
    decadas = {"60": [], "70": [], "80": [], "90": []}
    
    for _, row in dados.iterrows():
        try:
            ano = int(row["Ano"])
            if 1960 <= ano < 1970:
                decadas["60"].append(row.to_dict())
            elif 1970 <= ano < 1980:
                decadas["70"].append(row.to_dict())
            elif 1980 <= ano < 1990:
                decadas["80"].append(row.to_dict())
            elif 1990 <= ano < 2000:
                decadas["90"].append(row.to_dict())
        except ValueError:
            continue
    
    return {decada: pd.DataFrame(pessoas).sort_values("Ano") for decada, pessoas in decadas.items()}


def Banco(dados):
    """Exibe o banco de dados original completo."""
    st.title("📜 Banco de Dados Completo")
    if dados is None or dados.empty:
        st.error("⚠️ Nenhum dado encontrado no arquivo.")
    else:
        st.dataframe(dados, use_container_width=True)
        csv_dados = dados.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Baixar Banco de Dados", csv_dados, "banco_de_dados.csv", "text/csv")

def criar_lista_decada(dados):
    """Cria listas organizadas por décadas."""
    dados["Idade"] = 2025 - dados["Ano"]
    df_nomes = dados.sort_values("Nome")[["Nome", "Ano"]]
    df_idades = dados.sort_values("Idade")[["Nome", "Idade"]]
    return df_nomes, df_idades

def separar_por_altura(dados):
    """Separa os dados por altura em grupos específicos."""
    df_altura = dados.sort_values("Altura")[["Nome", "Altura"]]
    bins = [0, 1.55, 1.65, 1.75, 2.00]
    labels = ["1.50m", "1.60m", "1.70m", "1.90m"]
    dados["Grupo Altura"] = pd.cut(dados["Altura"], bins=bins, labels=labels)
    df_altura_grupos = dados.sort_values("Grupo Altura")[["Nome", "Grupo Altura"]]
    return df_altura, df_altura_grupos

def separar_por_peso(dados):
    """Agrupa os dados por peso em faixas específicas."""
    bins = [0, 60, 70, 80, 200]
    labels = ["60k", "70k", "80k", "90k+"]
    dados["Grupo Peso"] = pd.cut(dados["Peso"], bins=bins, labels=labels)
    return dados.sort_values("Grupo Peso")[["Nome", "Grupo Peso"]]