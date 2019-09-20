import tkinter

window = tkinter.Tk()
window.title('Learn Entry')

tkinter.Label(window, text='Username:').pack()
username = tkinter.Entry(window)
username.pack()

tkinter.Label(window, text='Password:').pack()
password = tkinter.Entry(window, show='*')
password.pack()


window.mainloop()
