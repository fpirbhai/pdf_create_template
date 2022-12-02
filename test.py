import PySimpleGUI as sg
import time

label1 = sg.Text('Welcome')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
button = sg.Button('Click me')
window = sg.Window('Autoclick', layout=[[label1],
                                        [label, input_box],
                                        [button]])
count = 1
while True:
    print(f'{count} - running...')
    count = count+1
    time.sleep(5)

