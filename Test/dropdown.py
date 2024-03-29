import tkinter

window = tkinter.Tk()
window.title("GUI")


def function():
    pass


# Creating a root menu to insert all the sub menus
root_menu = tkinter.Menu(window)
window.config(menu=root_menu)

# creating sub menus in the root menu
# initializes a new su menu in the root menu
file_menu = tkinter.Menu(root_menu)
# creates the name of the sub menu
root_menu.add_cascade(label="File", menu=file_menu)
# adds an option to the sub menu 'command' parameter is used to do some action
file_menu.add_command(label="New file...", command=function)
file_menu.add_command(label="Open files", command=function)
file_menu.add_separator()  # adds a line after the 'Open files' option
file_menu.add_command(label="Exit", command=window.quit)

# create another sub menu
edit_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=function)
edit_menu.add_command(label="Redo", command=function)


window.mainloop()
