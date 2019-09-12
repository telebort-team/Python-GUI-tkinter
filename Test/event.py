import tkinter

window = tkinter.Tk()
window.title("GUI")


# Takes 1 argument
def say_hi(event):
    tkinter.Label(window, text="Hi").pack()


btn = tkinter.Button(window, text="Click Me!")
btn.bind("<Button-1>", say_hi) # 'bind' takes 2 parameters, 1st is 'event', 2nd is 'function'
# <Button-1> for left click
# <Button-2> for middle click
# <Button-3> for right click

btn.pack()

window.mainloop()