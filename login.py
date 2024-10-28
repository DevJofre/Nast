from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

login = [
    [sg.Text('Usuario'), sg.Input(key='usuario')],
    [sg.Text('Senha  '), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

janela = sg.Window('Tela de Login', login)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'jofre' and valores['senha'] == '123':
            print('Bem-Vindo a Dev Aprender!')
