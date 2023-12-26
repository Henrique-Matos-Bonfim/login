import os
import time
from datetime import date
user = []
pswrd = []
data = []
sexo = []
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

def menu():
    global chc
    clear()
    print(f"+{'-'*40}+")
    print(f"|{'MENU':^40}|")
    print(f"+{'-'*40}+")
    for i, v in enumerate(mn):
        print(f'|{f" {i+1} - {v}":40}|')
    print(f"+{'-'*40}+")
    chc = int(input('>>> '))

#
vsenha=senha=sex = ' '
def adduser():
    global senha, sex
    clear()
    while True:
        r = ' '
        username = str(input('Username: ')).strip()
        if len(user) == 0 or username not in user:
            user.append(username)
            while sex not in 'FfMm':
                print('Qual seu sexo [F/M]')
                sex = str(input('>>>')).strip().uppercase()[0]
            sexo.append(sex)
            sex = ''
            while len(senha) < length:
                senha = str(input('Password: ')).strip()
                if len(senha) < length:
                    print(f'Senha muito pequena')
            pswrd.append(senha)
            senha = ''
            dataC = date.today()
            datacad = f'{dataC.day}/{dataC.month}/{dataC.year}'
            data.append(datacad)
            print(datacad)
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
    print(f"+{'-'*40}+")
    print(f"|{'LISTA USUARIOS':^40}|")
    print(f"+{'-'*40}+")
    for i, v in enumerate(user):
        print(f'|{f" {i+1} - {v} - {data[i]} - {sexo[i]}":40}|')
    print(f"+{'-'*40}+")

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
        print(f"+{'-'*40}+")
        print(f"|{'LISTA SENHAS':^40}|")
        print(f"+{'-'*40}+")
        for i, v in enumerate(pswrd):
            print(f'|{f" {i+1} - {v}":40}|')
        print(f"+{'-'*40}+")
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

