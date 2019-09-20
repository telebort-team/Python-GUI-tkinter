import tkinter

window = tkinter.Tk()
window.title("GUI")

label1 = tkinter.Label(window, text="Welcome to Telebort")
label1.pack()

picture = tkinter.PhotoImage(file="logo_500x312.png")
tkinter.Label(window, image=picture).pack()

label2 = tkinter.Label(
    window,
    text="You can change the foreground and background colours",
    fg="orange",
    bg="black"
)
label2.pack()

label3 = tkinter.Label(
    window,
    text="You can make text bigger",
    font=("Courier", 50)
)
label3.pack()

label4 = tkinter.Label(
    window,
    text="You can also set text align and border",
    anchor="e",
)
label4.pack(fill='x')

window.mainloop()
