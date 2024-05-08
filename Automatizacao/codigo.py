import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.9 

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#entrar no site do sistema.
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3) 

pyautogui.click(x=524, y=378)
pyautogui.write("ana.paraujosanto@gmail.com")

pyautogui.press("tab") 

pyautogui.write("123")

pyautogui.press("tab")   
pyautogui.press("enter")

time.sleep(2)

caminho_arquivo = r"C:\Users\ana\Documents\PythonHashtag\Automatizacao\produtos.csv"

tabela = pd.read_csv(caminho_arquivo)

for linha in tabela.index:

    pyautogui.click(x=459, y=261)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))

    pyautogui.press("tab")

    pyautogui.write( str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)