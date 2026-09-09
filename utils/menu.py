# Mini menu (pai ta inspirado hj)

from services.sites import chrome, github, youtube

def mensagem(msg): # Pra que? Não sei, só deu vontade mesmo
    print('=' * 100)
    print(msg)
    print('=' * 100)

def menu():
    mensagem('\nSeja bem vindo ao meu menu de automações, digite "P" para prosseguir e "C" para cancelar ! \n')
    while True:
        continuar = input('Deseja continuar? [P/C]: ').upper()
        if continuar == "P":
            mensagem('\nEscolha uma das opções abaixo: \n[1] Abrir Chrome\n[2] Abrir Youtube\n[3] Abrir github\n')
            escolha = int(input('Escolha: '))
            if escolha == 1:
                chrome()
            elif escolha == 2:
                youtube()
            elif escolha == 3:
                github()
            else:
                print('Opção inválida !')
        elif continuar == 'C':
            print('Cancelando programa !')
            break
        else:
            print('Opção inváida, cancelando programa')
            break
        
    