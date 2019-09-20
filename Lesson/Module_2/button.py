import tkinter

window = tkinter.Tk()
window.title("Learn Button")

tkinter.Label(window, text='Click the button and wait for the magic!').pack()
btn1 = tkinter.Button(window, text='Click me!')
btn1.pack()

btn2 = tkinter.Button(
    window,
    text='Change size',
    width=20,
    height=10,
    fg='white',
    bg='black'
)
btn2.pack()

btn3 = tkinter.Button(
    window,
    text='Change colour',
    activebackground='green',
    activeforeground='red',
    bg='red',
    fg='green',
    width=20,
    height=10,
)
btn3.pack()

picture = tkinter.PhotoImage(file='logo_500x312.png')
btn4 = tkinter.Button(
    window,
    image=picture,
    bg='gray',
)
btn4.pack()

window.mainloop()
