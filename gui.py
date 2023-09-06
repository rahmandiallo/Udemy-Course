import functions
import PySimpleGUI as sg



# label within the window
label = sg.Text("Type in a to-do")
# input box created
input_box = sg.InputText(tooltip="Enter todo",key="todo")
# button created
add_button = sg.Button("Add")

window = sg.Window("My To-do App", 
                    layout=[[label], [input_box, add_button]],
                    font=("Helvetica",20)) 

while True:
    #displays window 
    event,values = window.read()
    print(event)
    print(values)
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values["todo"] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
    if sg.WIN_CLOSED:
        break

#exits the program
window.close()
