import re
import os
from PyPDF2 import PdfReader
import shutil

def renomear_arquivo_com_razao_social(caminho_arquivo, competencia_sem_barra, razao_social_dam):
    diretorio, nome_arquivo = os.path.split(caminho_arquivo)
    _, extensao = os.path.splitext(nome_arquivo)
    competencia_limpa = re.sub(r'[\\/*?:"<>|]', '', competencia_sem_barra)
    razao_social_limpa = re.sub(r'[\\/*?:"<>|]', '', razao_social_dam)
    novo_nome_arquivo = f"{competencia_limpa}-DAM.ENC.ISSQN {razao_social_limpa}{extensao}"
    novo_caminho_arquivo = os.path.join(diretorio, novo_nome_arquivo)
    shutil.move(caminho_arquivo, novo_caminho_arquivo)
    return novo_caminho_arquivo

# Diretório contendo os arquivos PDF
diretorio = "C:/Users/Claudenir/Desktop/Renomear PDF's/Guias" 

def extrair_texto_entre_palavras(pdf_texto, palavra_inicial, palavra_final):
    padrao = re.compile(f'{palavra_inicial}(.*?){palavra_final}', re.DOTALL)
    resultado = padrao.search(pdf_texto)
    if resultado:
        return resultado.group(1).strip()
    else:
        return None
    
def alterar_pdf_dam():
    for nome_arquivo in os.listdir(diretorio):
        if nome_arquivo.endswith(".pdf"):
            caminho_arquivo = os.path.join(diretorio, nome_arquivo)
            
            # Verificar se o arquivo existe antes de tentar abri-lo
            if os.path.exists(caminho_arquivo):
                print(caminho_arquivo)
                
                # Ler o PDF
                reader = PdfReader(caminho_arquivo)
                page = reader.pages[0]
                pdf_texto = page.extract_text()
                
                # Extrair o texto desejado
                razao_social = extrair_texto_entre_palavras(pdf_texto, 'Contribuinte', 'Endereço')
                competencia = extrair_texto_entre_palavras(pdf_texto, 'Competência', 'Venc. do Imposto')

                if razao_social:
                    # Renomear o arquivo com base na razão social e manter na mesma pasta
                    novo_caminho_arquivo = renomear_arquivo_com_razao_social(caminho_arquivo, competencia, razao_social)
                    print(f"Arquivo '{nome_arquivo}' renomeado para: {novo_caminho_arquivo}")
                else:
                    print(f"Razão social não encontrada para o arquivo '{nome_arquivo}'.")
                
                # Certifique-se de fechar o arquivo PDF
                reader.reader.stream.close()
                
            else:
                print(f"Arquivo '{nome_arquivo}' não encontrado.")

alterar_pdf_dam()
