import os

user = []
pswrd = []

length = 5
def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')
senha = ' '
def adduser():
    global senha
    while True:
        r = ' '
        username = str(input('Username: ')).strip()
        if len(user) == 0 or username not in user:
            user.append(username)
            while len(senha) < length:
                senha = str(input('Password: ')).strip()
                if len(senha) < length:
                    print(f'Senha muito pequena')
            senha = ''
            r = str(input('Deseja continuar: [S/N] ')).strip()[0]
            clear()
            if r in 'Ss':
                continue
        elif username in user:
            print('Usuário já existente')

        if r in 'Nn':
            break
adduser()
for i, v in enumerate(user):
    print(f'{i+1} - {v}:', end='')

