# Eu não sei POO ainda então nem vou tentar meter uma classe aqui, vou usar funções mesmo
# Abrir sites

import pyautogui as pa

pa.PAUSE = 0.5

def abrir_chrome():
    pa.press('win')
    pa.write('chrome')
    pa.press('enter')
    pa.hotkey('ctrl', 'l')

    # E se aparecer a janela de escolher usuário? Boa pergunta, eu também não sei resolver (ainda), mas no meu caso eu só desativei ela

def abrir_github():
    abrir_chrome() # Não precisamos inventar a roda com ela já pronta (filosofei nessa)
    pa.write('https://github.com/')
    pa.press('enter')

def abrir_youtube():
    abrir_chrome()
    pa.write('https://www.youtube.com/')
    pa.press('enter')