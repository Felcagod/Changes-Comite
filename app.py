import streamlit as st

# CSS customizado para o tema moderno e clean com paleta do Carrefour
st.markdown("""
    <style>
    /* Fundo preto e branco predominante */
    .main {
        background-color: #121212;
        color: #EEEEEE;
        font-family: 'Montserrat', sans-serif;
        padding: 2rem;
    }
    /* Cabeçalho */
    h1, h2, h3, h4, h5 {
        color: #0033A0; /* Azul escuro Carrefour */
        font-weight: 700;
    }
    /* Botões */
    div.stButton > button {
        background-color: #D71920; /* Vermelho Carrefour */
        color: white;
        border-radius: 8px;
        padding: 0.6em 1.2em;
        font-weight: 600;
        border: none;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #FF3B3F;
        cursor: pointer;
    }
    /* File uploader */
    .stFileUploader > label {
        font-weight: 600;
        color: #EEEEEE;
    }
    /* Inputs e área de texto */
    div.stTextInput > label, div.stTextArea > label {
        color: #EEEEEE;
        font-weight: 600;
    }
    /* Sidebar */
    .css-1d391kg {
        background-color: #000000;
        color: #EEEEEE;
        padding: 1rem;
    }
    /* Scrollbar personalizado */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #222222;
    }
    ::-webkit-scrollbar-thumb {
        background-color: #D71920;
        border-radius: 10px;
        border: 2px solid #222222;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Gerador de Planilhas para o Comitê")
st.markdown("Envie os arquivos **Jira.xlsx** e **Maximo.xlsx** para gerar a planilha formatada automaticamente.")

jira_file = st.file_uploader("Escolha o arquivo Jira ", type=["xlsx"])
maximo_file = st.file_uploader("Escolha o arquivo Maximo ", type=["xlsx", "csv"])

if jira_file and maximo_file:
    if st.button("Gerar Planilha"):
        # Aqui você pode colocar a chamada para sua função que processa os arquivos
        st.success("Planilha gerada com sucesso! 🎉")
else:
    st.info("Aguardando upload dos arquivos para começar...")


