from feet_inches import parse, convert
import PySimpleGUI as sg

sg.theme('DarkAmber')

input_box = sg.InputText(tooltip="enter a number", key="number1")
input_box2 = sg.InputText(tooltip="enter a number", key="number2")
text_box = sg.Text("enter feet")
text_box2 = sg.Text("enter inches")
answer_text_box = sg.Text("", key="answer")
convert_button = sg.Button('Convert', key='convert')
exit_button = sg.Button('Exit', key='exit')

layout = [
    [text_box, input_box],
    [text_box2, input_box2],
    [convert_button, exit_button, answer_text_box]
]

window = sg.Window('Convertor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'convert':
        try:
            feet = float(values['number1'])
            inches = float(values['number2'])

            result = convert(feet, inches)

            window['answer'].update(f"Result: {result:.2f} meters")
        except ValueError:
            sg.popup('Enter a number')
    elif event == 'exit':
        exit("exit")
window.close()
