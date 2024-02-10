import re
import os
from PyPDF2 import PdfReader

def extrair_texto_entre_palavras(pdf_texto, palavra_inicial, palavra_final):
    padrao = re.compile(f'{palavra_inicial}(.*?){palavra_final}', re.DOTALL)
    resultado = padrao.search(pdf_texto)
    if resultado:
        return resultado.group(1).strip()
    else:
        return None

def renomear_arquivo_com_razao_social(nome_arquivo, razao_social):
    _, extensao = os.path.splitext(nome_arquivo)
    razao_social_limpa = re.sub(r'[\\/*?:"<>|]', '', razao_social)
    novo_nome_arquivo = f"{razao_social_limpa}{extensao}"
    os.rename(nome_arquivo, novo_nome_arquivo)
    return novo_nome_arquivo

# Diretório contendo os arquivos PDF
diretorio = "C:/Users/Claudenir/Desktop/Renomear PDF's" 

# Iterar sobre os arquivos no diretório
for nome_arquivo in os.listdir(diretorio):
    if nome_arquivo.endswith(".pdf"):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)

        # Ler o PDF
        reader = PdfReader(caminho_arquivo)
        page = reader.pages[0]
        pdf_texto = page.extract_text()

        # Extrair o texto desejado
        razao_social = extrair_texto_entre_palavras(pdf_texto, 'Razão Social:', 'Endereço')

        if razao_social:
            # Renomear o arquivo com base na razão social
            novo_nome_arquivo = renomear_arquivo_com_razao_social(caminho_arquivo, razao_social)
            print(f"Arquivo '{nome_arquivo}' renomeado para: {novo_nome_arquivo}")
        else:
            print(f"Razão social não encontrada para o arquivo '{nome_arquivo}'.")
