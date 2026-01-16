@echo off
TITLE Conversor Automatico PDF para TXT (Foxit)
color 0A

echo ========================================================
echo      PARCEIRO DE PROGRAMACAO - AUTOMACAO FOXIT
echo ========================================================
echo.
echo A preparar o ambiente...
echo.

:: 1. Garante que o comando roda na pasta onde o arquivo esta
cd /d "%~dp0"

:: 2. Executa o script Python
:: CERTIFICA-TE que o nome do arquivo abaixo esta correto!
echo A iniciar o script Python...
echo POR FAVOR: NAO MEXAS NO MOUSE OU TECLADO!
echo.
python foxit_text_extraction.py

:: 3. Pausa final para veres o relatorio
echo.
echo ========================================================
echo                 FIM DO PROCESSO
echo ========================================================
pause