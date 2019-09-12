import tkinter

window = tkinter.Tk()
window.title("GUI")

tkinter.Label(window, text="Username").grid(row=0) # position (0, 0)
tkinter.Entry(window).grid(row=0, column=1) # position (0, 1)

tkinter.Label(window, text="Password").grid(row=1) # position (1, 0)
tkinter.Entry(window).grid(row=1, column=1) # position (1, 1)

tkinter.Checkbutton(window, text="Keep Me Logged In").grid(columnspan=2) # 'columnspan' tells to take the width of 2 columns
# you can also use 'rowspan' in the similar manner

window.mainloop()