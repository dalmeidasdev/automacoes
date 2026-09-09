# Eu não sei POO ainda então nem vou tentar meter uma classe aqui, vou usar funções mesmo
# Abrir sites

import pyautogui as pa
# import time

pa.PAUSE = 0.5

def chrome():
    pa.press('win')
    pa.write('chrome')
    pa.press('enter')
    # Essa parte de baixo agora não é obrigatória já que a maioria já vem clicada mas é sempre bom garantir
    pa.moveTo(190, 65)
    # Se no seu pc não der tempo de clicar descomente essa linha
    # time.sleep(2)
    pa.click()

    # E se aparecer a janela de escolher usuário? Boa pergunta, eu também não sei resolver (ainda), mas no meu caso eu só desativei ela

def github():
    chrome() # Não precisamos inventar a roda com ela já pronta (filosofei nessa)
    pa.write('https://github.com/')
    pa.press('enter')

def youtube():
    chrome()
    pa.write('https://www.youtube.com/')
    pa.press('enter')