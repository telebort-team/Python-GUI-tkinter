import tkinter

window = tkinter.Tk()
window.title("Learn Label")

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
    text="You can also set border and padding",
    bd=4,
    relief='solid',
    padx=20,
    pady=20
)
label3.pack()

label4 = tkinter.Label(
    window,
    text="You can make text bigger",
    font=("Courier", 50),
    bg="gray"
)
label4.pack()

window.mainloop()
