# Pegar a posição do mouse e a cor:

import pyautogui as pa

def pegar_posicao():
    print('=' * 100)
    print('Bem vindo, abaixo está a posição atual do seu mouse, quando achar a posição que precisar aperte CTRL + C\n')
    print('Dica: se após o CRTL + C ainda continuar mudando a posição clique no terminal uma vez e volte para a posição desejada e tente denovo')
    print('=' * 100)
    pa.displayMousePosition()

pegar_posicao()