import tkinter

window = tkinter.Tk()

# Rename the title of the window
window.title("GUI")

# Pack si used to show the object in the window
label = tkinter.Label(window, text="Hello World!")
label.pack()

window.mainloop()