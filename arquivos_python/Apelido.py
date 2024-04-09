#Apelido
# Passo 1: Entrar no sistema da empresa 
    # https://app.acessorias.com/index.php

import pyautogui
import time
import tabula

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3

# abrir o navegador (microsoft edge)
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(5)
# entrar no link especificado
pyautogui.write("https://app.acessorias.com/index.php")
pyautogui.press("enter")
time.sleep(2)

# Passo 2: Fazer login
# selecionar o campo (autopreenchimento)
pyautogui.click(x=1623, y=856)

time.sleep(2)

# Passo 3: Importar a base de contatos pra cadastrar
import pandas as pd

tabela = pd.read_csv("dados.csv") # "EMPRESASID.csv = Relatorio Padrão Ajustavel.csv"

print(tabela)

# Passo 4: Cadastramentos
for linha in tabela.index:
    # clicar no primeiro campo de preenchimento
    pyautogui.click(x=75, y=306)

    time.sleep(5)

    pyautogui.click(x=456, y=244) 
    # pegar da tabela o valor do campo que a gente quer preencher
    empresa = tabela.loc[linha, "ID"]
    apelido = tabela.loc[linha, "APELIDO"]
    # preencher o campo e repetição 
    pyautogui.write(str(tabela.loc[linha, "ID"]))  #"EMPRESA = Coluna 1"
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(x=507, y=347) #clica na empresa primeira
    time.sleep(4)
    pyautogui.click(x=1653, y=369) #clica no campo do apelido
    time.sleep(2)
    pyautogui.write(str(tabela.loc[linha, "APELIDO"])) #escreve apelido
    time.sleep(2)
    pyautogui.click(x=1280, y=474) #clica em "salvar" botão
    time.sleep(4)



