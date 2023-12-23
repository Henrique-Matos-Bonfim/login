import os
import time

user = []
pswrd = []
mn = [
    'ADICIONAR USUARIO',
    'FAZER LOGIN',
    'VISUALIZAR USUARIO',
    'REMOVER USUARIO',
    'EDITAR USUARIO',
    'SAIR'
]
length = 5
tent = chc = 0

#Limpar o cmd
def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')

#Menu tlgd
def menu():
    global chc
    clear()
    print(f"+{'-'*30}+")
    print(f"|{'MENU':^30}|")
    print(f"+{'-'*30}+")
    for i, v in enumerate(mn):
        print(f'|{f" {i+1} - {v}":30}|')
    print(f"+{'-'*30}+")
    chc = int(input('>>> '))

#
vsenha = senha = ' '
def adduser():
    global senha
    clear()
    while True:
        r = ' '
        username = str(input('Username: ')).strip()
        if len(user) == 0 or username not in user:
            user.append(username)
            while len(senha) < length:
                senha = str(input('Password: ')).strip()
                if len(senha) < length:
                    print(f'Senha muito pequena')
            pswrd.append(senha)
            senha = ''
            r = str(input('Deseja continuar: [S/N] ')).strip()[0]
            clear()
            if r in 'Ss':
                continue
        elif username in user:
            print('Usuário já existente')

        if r in 'Nn':
            break

def listaruser():
    clear()
    print(f"+{'-'*30}+")
    print(f"|{'LISTA USUARIOS':^30}|")
    print(f"+{'-'*30}+")
    for i, v in enumerate(user):
        print(f'|{f" {i+1} - {v}":30}|')
    print(f"+{'-'*30}+")

def login():
    global tent, vsenha
    clear()
    listaruser()
    vuser = str(input('Nome do usuário: '))          
    if vuser in user:
        id_user = user.index(vuser)
        while vsenha != pswrd[id_user]:
            vsenha = str(input('Senha do usuário: '))
            if vsenha == pswrd[id_user]:
                print(f'Seja bem vindo {vuser}')
            else:
                print('Senha incorreta.', end=' ')
                tent+=1
                if tent <3:
                    print('Digite a senha novamente')
                else:
                    print('Acesso bloquado')
                    tent =0
                    break
            input()
    else:
        print('Usuário não encontrado!')
        input()

def remover():
    clear()
    listaruser()
    vuser = str(input('Nome usuário:'))           
    if vuser in user:
        print(f"+{'-'*30}+")
        print(f"|{'LISTA SENHAS':^30}|")
        print(f"+{'-'*30}+")
        for i, v in enumerate(pswrd):
            print(f'|{f" {i+1} - {v}":30}|')
        print(f"+{'-'*30}+")
        vsenha = str(input('Confirme a senha:'))
        if vsenha == pswrd[user.index(vuser)]:
            user.pop(user.index(vuser))
            print(f'Usuário {vuser} removido com sucesso')
            input()
        else:
            clear()
            print('Senha  incorreta')
            print(f'Usuário {user[user.index(vuser)]} não foi removido')
            input()         
    else:
        print('Usuário inexistente!')
        input()
 
def editaruser():
    clear()
    listaruser()
    print('Qual usuário você deseja editar')   
    edit = int(input('>>>'))-1
    nome_a = user[edit]
    nome = str(input('Novo nome: '))
    vsenha = str(input('Confirme a senha do usuário: '))
    if vsenha == pswrd[edit]:
        user[edit] = nome
        print(f'Usuário {nome_a} atualizado para {nome}')
    else:
        print('Senha incorreta')
        print('Nome de usuário não atualizado')
    clear()
    listaruser()
    input()
        

while True:
    menu()

    if chc == 1:
        adduser()
    elif chc ==6:
        print('Fechando')
        break
    if len(user)>0:
        if chc ==2:
            login()
        elif chc ==3:
            listaruser()
            input()
        elif chc ==4:
            remover()
        elif chc ==5:
            editaruser()
    elif len(user)==0:
        print('Não há nenhum usuário cadastrado')
        input()
        clear()

