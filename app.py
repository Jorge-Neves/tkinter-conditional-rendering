#Import the required library
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Define the geometry of the window
win.geometry("650x450")

#Define function to hide the widget
def hide_widget(widget):
   widget.pack_forget()

#Define a function to show the widget
def show_widget(widget):
   widget.pack()


#Create a button Widget
button_hide= Button(win, text= "Hide", command= lambda:hide_widget(label))
button_hide.pack(pady=20)

button_show= Button(win, text= "Show", command= lambda:show_widget(label))
button_show.pack(pady=20)

#Create an Label Widget
label= Label(win, text= "Showing the Message", font= ('Helvetica bold', 14))
label.pack(pady=20)


win.mainloop()
