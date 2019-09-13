import tkinter

window = tkinter.Tk()
window.title("GUI")

# create the 'Canvas' area of width and height 500px
canvas = tkinter.Canvas(window, width=500, height=500)
canvas.pack()

# 'create_line' is used to create a line. Parameters:-
# (start_x, start_y, end_x, end_y)
line1 = canvas.create_line(25, 25, 250, 150)
# parameter:- (fill = color_name)
line2 = canvas.create_line(25, 250, 250, 150, fill="red")


# 'create_rectangle' is used to create rectangle. Parameters:-
# (start_x, start_y, width, height, fill)
rect = canvas.create_rectangle(500, 25, 175, 75, fill="green")

# 'delete' shapes with delete method passing the name of the variable
canvas.delete(line1)

# 'delete' all shapes
# canvas.delete(tkinter.ALL)


window.mainloop()