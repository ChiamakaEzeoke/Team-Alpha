from tkinter import *
# Everything is a widget here, so the first thing we create should be a widget



# This goes first
root = Tk()

########## INTRODUCTION
# # Creatng a label widget 
# myLabel = Label(root, text='Hello World')
# # Shoving it unto the screen
# myLabel.pack()





########## USING THE GRID SYSTEM
# myLabel = Label(root, text='Hello World')
# myLabel2 = Label(root, text='My name is SD')
# myLabel.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)



######### CREATING BUTTONS
# def clickButton():
#     label = Label(root, text='Button click action')
#     label.pack()

# button = Button(root, text='Click Me!', padx=50, pady=10, command=clickButton, fg='white', bg='#800080')
# button.pack()


####### INPUT BOXES WITH PYTHON

# e = Entry(root, width=50, fg='grey')
# e.pack()

# def clickButton():
#     label = Label(root, text='Hello {}'.format(e.get()))
#     label.pack()

# button = Button(root, text='Enter your name!', padx=50, pady=10, command=clickButton, fg='white', bg='#800080')
# button.pack()


# # Event Loop
root.mainloop()