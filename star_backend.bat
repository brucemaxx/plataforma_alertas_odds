@echo off
echo Ativando ambiente virtual...
call .venv\Scripts\activate.bat

echo Definindo PYTHONPATH...
set PYTHONPATH=.

echo Iniciando FastAPI com Uvicorn...
uvicorn main:app --reload

pause
