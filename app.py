# Import the required library
from tkinter import *

# Create an instance of tkinter frame
Root = Tk()

# Define the geometry of the window
Root.geometry("650x450")


# Define function to hide the widget
def hide_widget(widget):
    widget.pack_forget()


# Define a function to show the widget
def show_widget(widget):
    widget.pack()


# Create a button Widget
button_hide = Button(Root, text="Hide", command=lambda: hide_widget(second_frame))
button_hide.pack(pady=20)

button_show = Button(Root, text="Show", command=lambda: show_widget(second_frame))
button_show.pack(pady=20)

second_frame = Frame(Root)
second_frame.pack()

# Create a Label Widget
label = Label(second_frame, text="Showing the Message", font=('Helvetica bold', 14))
label.pack(pady=20)

Root.mainloop()
