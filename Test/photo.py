import tkinter

window = tkinter.Tk()
window.title("GUI")

# takes image from the directory and store as variable
icon = tkinter.PhotoImage(file="images/haha.png")

# display the picture using a 'Label' by passing the 'picture' to 'image' parameter
label = tkinter.Label(window, image=icon)
label.pack()

window.mainloop()
