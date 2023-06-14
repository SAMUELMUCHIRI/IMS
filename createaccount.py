import PySimpleGUI as sg
sg.PySimpleGUI.SYMBOL_TITLEBAR_MINIMIZE = '.'
sg.PySimpleGUI.SYMBOL_TITLEBAR_MAXIMIZE = 'O'
sg.PySimpleGUI.SYMBOL_TITLEBAR_CLOSE    = 'x'

def login():
    sg.theme("DarkGreen3")
    layout = [
        [sg.Text("Log In", size=(15, 1), font=40)],
        [sg.Text("Username", size=(15, 1), font=16), sg.InputText(key='-usrnm-', font=16)],
        [sg.Text("Password", size=(15, 1), font=16), sg.InputText(key='-pwd-', password_char='*', font=16)],
        [sg.Button('Ok'), sg.Button('Cancel'),sg.Button('Create Account')]
    ]

    window = sg.Window("Intern Magement System Login", layout )
   

    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        elif event == 'Minimize':
            window.minimize()
        else:
            if event == "Ok":
                if values['-usrnm-'] == 'username' and values['-pwd-'] == 'password':
                    sg.popup("Welcome!")
                    break
                else:
                    sg.popup("Invalid login. Try again")

    window.close()

login()