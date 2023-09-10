import functions
import PySimpleGUI as sg



# label within the window
label = sg.Text("Type in a to-do")
# input box created
input_box = sg.InputText(tooltip="Enter todo",key="todo")
# button created
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key= "todos",
                        enable_events = True, size = [45,10])

edit_button = sg.Button("Edit")

window = sg.Window('My To-do App', layout=[[label], [input_box, add_button],[list_box,edit_button]], font =('Helvetica',20))

while True:
    #displays window 
    event,values = window.read()
    print(1,event)
    print(2,values)
    print(3,values["todos"])
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values["todo"] + "\n"
        todos.append(new_todo)
        window['todos'].update(values=todos)
        functions.write_todos(todos)

    if event == "Edit":
        todo_to_edit = values["todos"][0]
        new_todo = values['todo']
        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        functions.write_todos(todos)
        window["todos"].update(values = todos)

    if event == "todos":
       window['todo'].update(value=values['todos'][0]) 
    if sg.WIN_CLOSED:
        break

#exits the program
window.close()
