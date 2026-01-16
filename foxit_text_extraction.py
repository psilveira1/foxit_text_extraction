import os
import time
import pyautogui
import pyperclip
from pypdf import PdfReader

# --- TEU DIRETÓRIO ---
DIRETORIO_RAIZ = r"C:\Users\patyp\Desktop\references\01_PDF\livros\teste"

# --- CONFIGURAÇÕES ---
ATALHO_PERSONALIZADO = ['alt', 't'] 

# Tempos (Ajustados para maior estabilidade)
TEMPO_ABRIR_PDF = 3.5      # Tempo para o Foxit abrir
TEMPO_JANELA_SALVAR = 2.0  # Tempo para a janela aparecer
TEMPO_CONVERSAO = 2.5      # Tempo para o Foxit processar o texto
TEMPO_FECHAR = 1.0         # Tempo extra para garantir o fechamento

def verificar_se_pdf_tem_texto(caminho_pdf):
    """ Verifica se o PDF é texto ou imagem (OCR) """
    try:
        leitor = PdfReader(caminho_pdf)
        texto_acumulado = ""
        # Verifica até 3 páginas
        paginas_para_checar = min(3, len(leitor.pages))
        
        for i in range(paginas_para_checar):
            texto_pagina = leitor.pages[i].extract_text()
            if texto_pagina:
                texto_acumulado += texto_pagina

        if len(texto_acumulado.strip()) < 5:
            return False # É Image Based
        return True # Tem texto

    except Exception:
        return False # Na dúvida, assume que não é processável nativamente

def converter_ciclo_completo():
    print("--- INICIANDO CONVERSÃO (COM FECHAMENTO SEGURO) ---")
    print(f"Alvo: {DIRETORIO_RAIZ}")
    print("--- Larga o mouse e teclado em 5 segundos... ---")
    time.sleep(5)

    total_convertidos = 0
    total_ignorados_imagem = 0

    for pasta_atual, subpastas, arquivos in os.walk(DIRETORIO_RAIZ):
        
        # --- FILTRO DE PASTAS (Ignorar pdf_parts e pdf_images) ---
        if "pdf_parts" in subpastas: subpastas.remove("pdf_parts")
        if "pdf_images" in subpastas: subpastas.remove("pdf_images")

        for arquivo in arquivos:
            if arquivo.lower().endswith(".pdf"):
                caminho_pdf_completo = os.path.join(pasta_atual, arquivo)
                caminho_txt_final = os.path.splitext(caminho_pdf_completo)[0] + ".txt"

                # Verifica se já existe
                if os.path.exists(caminho_txt_final):
                    print(f"[PULAR] Já convertido: {arquivo}")
                    continue

                print(f"[ANALISANDO] {arquivo}...")

                # Triagem OCR
                if not verificar_se_pdf_tem_texto(caminho_pdf_completo):
                    print(f" [IGNORADO] Image Based (Requer OCR).")
                    total_ignorados_imagem += 1
                    continue 

                try:
                    # 1. Abre o PDF
                    os.startfile(caminho_pdf_completo)
                    time.sleep(TEMPO_ABRIR_PDF)

                    # 2. Executa Atalho ALT + T
                    pyautogui.hotkey(*ATALHO_PERSONALIZADO)
                    time.sleep(TEMPO_JANELA_SALVAR)

                    # 3. Cola o caminho e Salva
                    pyperclip.copy(caminho_txt_final)
                    pyautogui.hotkey('ctrl', 'v')
                    time.sleep(0.5)
                    pyautogui.press('enter') # Salvar
                    time.sleep(0.5)
                    pyautogui.press('enter') # Confirmar substituição (se houver)

                    # 4. Espera a conversão
                    time.sleep(TEMPO_CONVERSAO)

                    # -----------------------------------------------------------
                    # 5. FECHAMENTO SEGURO DO PDF
                    # -----------------------------------------------------------
                    print(" -> Fechando arquivo...")
                    
                    # Comando para fechar a aba atual
                    pyautogui.hotkey('ctrl', 'w') 
                    time.sleep(0.5) 
                    
                    # PRECAUÇÃO: Se aparecer "Deseja salvar as alterações no PDF?"
                    # Pressionamos 'n' (Não) para fechar a janela sem salvar o PDF original
                    # Se não houver janela, pressionar 'n' não faz nada no Foxit (seguro)
                    pyautogui.press('n') 
                    
                    # Espera garantir que fechou antes de ir para o próximo
                    time.sleep(TEMPO_FECHAR)
                    # -----------------------------------------------------------

                    total_convertidos += 1
                    print(f" -> SUCESSO.")

                except Exception as erro:
                    print(f" [ERRO] {arquivo}: {erro}")
                    # Em caso de erro, tenta fechar tudo para destrancar
                    pyautogui.hotkey('alt', 'f4')

    print(f"\n--- RELATÓRIO ---")
    print(f"Convertidos: {total_convertidos}")
    print(f"Ignorados (Imagem): {total_ignorados_imagem}")

if __name__ == "__main__":
    converter_ciclo_completo()