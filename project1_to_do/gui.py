import fun
import PySimpleGUI as sg
import time
import os


if not os.path.exists("todos.txt") :
    with open("todos.txt","w") as file:
        pass



sg.theme("Black")
clock=sg.Text("",key="Clock")
lable =sg.Text("Type In a To-Do")
input_box=sg.InputText(tooltip="Enter To-Do",key="todo")
Add_button =sg.Button("Add" ,size= 10)
list_box=sg.Listbox(fun.get_todos(),key="todos" , enable_events=True ,size=[50,16])
edit_button=sg.Button("Edit")
complete_button=sg.Button("Complete")
exit_button=sg.Button("Exit")


window =sg.Window("MY TO-DO APP",
                  layout=[[clock],
                          [lable],
                          [input_box , Add_button],
                          [list_box, edit_button,complete_button],
                          [exit_button]], 
                          font=("Helvetica",10))

while True :
    event ,values = window.read(timeout=200)
    window["Clock"].update(value=time.strftime("%b %d / %Y  %H: %M: %S"))
    print("1 ",event)
    print("2",values)
    print("3",values["todos"])
    match event :
        case "Add" :
            todos=fun.get_todos()
            new_todo=values["todo"]+"\n"
            todos.append(new_todo)
            fun.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit" :
            try:
                todo_to_edit=values["todos"][0]
                new_todo=values["todo"] 
                todos=fun.get_todos()
                index=todos.index(todo_to_edit)
                todos[index]=new_todo
                fun.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError :
                sg.popup("please select an item first." , font=("Helvetica",10))

              
            
        case "todos" :
            window["todo"].update(value=values["todos"][0])

        case "Complete" :
            try:
                todo_to_complete=values["todos"][0]
                todos=fun.get_todos()
                todos.remove(todo_to_complete)
                fun.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError :
                sg.popup("please select an item first." , font=("Helvetica",10)) 
        case "Exit" :
            break

        case sg.WIN_CLOSED :
            break
        




window.close()
