import PySimpleGUI as sg

sg.PySimpleGUI.SYMBOL_TITLEBAR_MINIMIZE = '.'
sg.PySimpleGUI.SYMBOL_TITLEBAR_MAXIMIZE = 'O'
sg.PySimpleGUI.SYMBOL_TITLEBAR_CLOSE    = 'x'

layout = [
    [sg.Titlebar(
        title='TITLE',
        icon=sg.EMOJI_BASE64_HAPPY_IDEA,
        text_color='white',
        background_color='blue',
        font=('Courier New', 40, 'bold'),
    )],
    [sg.Button('Minimize'), sg.Button('Exit')],
]

window = sg.Window('Title', layout, finalize=True,
    # use_custom_titlebar=True,
    # titlebar_background_color='blue',
    # titlebar_text_color='white',
    # titlebar_font=('Courier New', 40, 'bold'),
    # titlebar_icon=sg.EMOJI_BASE64_HAPPY_IDEA,
)

while True:

    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Minimize':
        window.minimize()

window.close()