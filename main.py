
import pyautogui
import time
import pandas

# pyautogui.click = clicar em algum lugar
# pyautogui.press = apertar uma tecla
# pyautogui.write = escrever um texto

pyautogui.PAUSE = 0.5    


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=218, y=84)

#digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(2)
pyautogui.press("enter")

#esperar 3 segundas

time.sleep(3)

# passo 2: Fazer login

pyautogui.click(x=507, y=594)
time.sleep(3)
pyautogui.write("jamillepersi@hotmail.com")

#preencher a senha   
pyautogui.press("tab")
pyautogui.write("amorade")

#botao logar

pyautogui.press("tab")
pyautogui.press("enter")

#esperar 3 segundos

pyautogui.sleep(3)

# passo 3: Immportar a base de dados

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# passo 4: Cadastrar 1 produto

for linha in tabela.index: #para cada linha da minha tabela
    pyautogui.click(x=509, y=415)

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    
    if obs != "nam":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)

# passo 5: Repetir para todos  os produtos



#pyautogui = importar dados para o python