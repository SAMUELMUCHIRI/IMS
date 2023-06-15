import PySimpleGUI as sg

def get_codes(filename):

    with open(filename, 'rt') as f:
        lines = f.readlines()

    codes = []
    for line in lines:
        a, b = line.split(',')
        codes.append((a.strip(), b.strip()))

    return codes

def login(codes):

    sg.theme('SandyBeach')

    layout = [
        [sg.Text('Enter admin username and password')],
        [sg.Text('username', size =(7, 1)), sg.InputText()],
        [sg.Text('password', size =(7, 1)), sg.InputText()],
        [sg.Submit(), sg.Cancel()],
    ]

    window = sg.Window('Admin loggin', layout, margins=(10, 10))

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Cancel'):
            print('Login Cancelled')
            success = None
        elif event == 'Submit':
            if (values[0], values[1]) in codes:
                success = True
                print("Login Successful")
            else:
                success = False
                print("Login Failed")
        break

    window.close()
    return success

password_file = 'psw.txt'
codes = get_codes(password_file)
success = login(codes)