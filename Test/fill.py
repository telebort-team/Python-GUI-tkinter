import tkinter

window = tkinter.Tk()
window.title("GUI")

tkinter.Label(window, text="Sufficient width", fg="white", bg="purple").pack()

tkinter.Label(window, text="Taking all available X width", fg="white", bg="green").pack(fill="x")

tkinter.Label(window, text="Taking all available Y height", fg="white", bg="black").pack(side="left", fill="y")

window.mainloop()