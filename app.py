import streamlit as st
from gerar_planilha_comite import padronizar_e_gerar_planilha
import tempfile
from io import BytesIO

# CSS customizado
st.markdown("""
    <style>
    .main {background-color: #121212; color: #EEEEEE; font-family: 'Montserrat', sans-serif; padding: 2rem;}
    h1, h2, h3, h4, h5 {color: #0033A0; font-weight: 700;}
    div.stButton > button {background-color: #D71920; color: white; border-radius: 8px; padding: 0.6em 1.2em; font-weight: 600; border: none; transition: background-color 0.3s ease;}
    div.stButton > button:hover {background-color: #FF3B3F; cursor: pointer;}
    .stFileUploader > label {font-weight: 600; color: #EEEEEE;}
    div.stTextInput > label, div.stTextArea > label {color: #EEEEEE; font-weight: 600;}
    .css-1d391kg {background-color: #000000; color: #EEEEEE; padding: 1rem;}
    ::-webkit-scrollbar {width: 8px;}
    ::-webkit-scrollbar-track {background: #222222;}
    ::-webkit-scrollbar-thumb {background-color: #D71920; border-radius: 10px; border: 2px solid #222222;}
    </style>
""", unsafe_allow_html=True)

st.title("Gerador de Planilhas para o Comitê")
st.markdown("Envie os arquivos **Jira.xlsx** e **Maximo.xlsx** ou **Maximo.csv** para gerar a planilha formatada automaticamente.")

jira_file = st.file_uploader("Escolha o arquivo Jira", type=["xlsx"])
maximo_file = st.file_uploader("Escolha o arquivo Maximo", type=["xlsx", "csv"])

if jira_file and maximo_file:
    if st.button("Gerar Planilha"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp_jira, \
             tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx" if maximo_file.name.endswith(".xlsx") else ".csv") as tmp_maximo:
            
            # Salva os uploads em arquivos temporários
            tmp_jira.write(jira_file.read())
            tmp_maximo.write(maximo_file.read())

            # Gera a planilha final com formatação
            caminho_saida = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx").name
            padronizar_e_gerar_planilha(tmp_jira.name, tmp_maximo.name, caminho_saida)

            # Lê o arquivo final para download
            with open(caminho_saida, "rb") as f:
                output_bytes = f.read()

            st.success("Planilha gerada com sucesso! 🎉")
            st.download_button(
                label="📥 Baixar Planilha Formatada",
                data=output_bytes,
                file_name="planilha_comite.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
else:
    st.info("Aguardando upload dos arquivos para começar...")
