import tkinter
import tkinter.messagebox

window = tkinter.Tk()
window.title("GUI")


# create a simple alert box
tkinter.messagebox.showinfo("Alert Message", "This is just an alert message!")

# create a question to get the response from the user [Yes or No Question]
response = tkinter.messagebox.askquestion(
    "Simple Question", "Do you love Python?")
# If user clicks 'Yes' then it returns 'yes' else it returns 'no'
# tkinter.Label(window, text=response).pack()
if response == 'yes':
    tkinter.Label(window, text="You love Python!").pack()
else:
    tkinter.Label(window, text="You don't love Python!").pack()


window.mainloop()
