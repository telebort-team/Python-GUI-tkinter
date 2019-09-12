import tkinter

window = tkinter.Tk()
window.title("GUI")

# Creating 2 frames TOP and BOTTOM
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side="bottom")

# Create buttons
btn1 = tkinter.Button(top_frame, text="Button1", fg="red", bg="blue").pack()
btn2 = tkinter.Button(top_frame, text="Button2", fg="green", bg="yellow").pack()
btn3 = tkinter.Button(bottom_frame, text="Button3", fg="purple", bg="black").pack(side="left")
btn4 = tkinter.Button(bottom_frame, text="Button4", fg="orange", bg="red").pack(side="left")

window.mainloop()
