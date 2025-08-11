import streamlit as st
import tempfile
import os
from gerar_planilha_comite import padronizar_e_gerar_planilha


st.set_page_config(page_title="Gerador Planilha Comitê", page_icon="📊")

st.title("Gerador de Planilha Comitê")
st.write("Faça upload dos arquivos Jira e Maximo para gerar a planilha final formatada.")

jira_file = st.file_uploader("Escolha o arquivo Jira.xlsx", type=["xlsx"])
maximo_file = st.file_uploader("Escolha o arquivo Maximo.xlsx ou Maximo.csv", type=["xlsx", "csv"])

if jira_file and maximo_file:
    if st.button("Gerar Planilha"):
        with st.spinner("Processando..."):
            try:
                # Criar pasta temporária para salvar os arquivos
                with tempfile.TemporaryDirectory() as temp_dir:
                    caminho_jira = os.path.join(temp_dir, "Jira.xlsx")
                    caminho_maximo = os.path.join(temp_dir, "Maximo.xlsx" if maximo_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" else "Maximo.csv")
                    caminho_saida = os.path.join(temp_dir, "planilha_final.xlsx")

                    # Salvar uploads
                    with open(caminho_jira, "wb") as f:
                        f.write(jira_file.getbuffer())

                    with open(caminho_maximo, "wb") as f:
                        f.write(maximo_file.getbuffer())

                    # Rodar a função passando os caminhos da pasta temporária
                    padronizar_e_gerar_planilha(caminho_jira=caminho_jira, caminho_maximo=caminho_maximo, caminho_saida=caminho_saida)

                    # Ler arquivo gerado para download
                    with open(caminho_saida, "rb") as f:
                        dados_planilha = f.read()

                    st.success("Planilha gerada com sucesso!")
                    st.download_button(label="Baixar planilha", data=dados_planilha, file_name="planilha_final.xlsx")
            except Exception as e:
                st.error(f"Erro ao gerar planilha: {e}")
else:
    st.info("Por favor, envie ambos os arquivos para prosseguir.")
