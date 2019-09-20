import tkinter

window = tkinter.Tk()
window.title("Command Dashboard")

form = tkinter.Frame(window)
form.pack()

username_form = tkinter.Frame(form)
username_form.pack()
password_form = tkinter.Frame(form)
password_form.pack()

tkinter.Label(username_form, text="Username:").grid(row=0)
tkinter.Entry(username_form).grid(row=0, column=1)

tkinter.Label(password_form, text="Password:").grid(row=1)
tkinter.Entry(password_form).grid(row=1, column=1)




window.mainloop()