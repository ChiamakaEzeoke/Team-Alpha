from tkinter import * 

root = Tk()

root.attributes('-fullscreen', True)  
frame = Frame(root, bg = "orange")
frame.pack(fill= BOTH, expand= True, padx= 10, pady=20)

treeFrame = Frame(frame, bg='grey', padx=20, pady=20)
treeFrame.pack(side = LEFT, expand = True, fill = BOTH)
text = Label(treeFrame, text= 'Tree Visualisation')
text.grid(row=0, column=5, columnspan=12)

valuesFrame = Frame(frame, bg='white', padx=20, pady=20)
valuesFrame.pack(side = RIGHT, expand = True, fill = BOTH)

inputTree = Text(valuesFrame, height = 5, width = 52, padx=20, pady=20)
inputTree.grid(row=0, column=0)


canvas = Canvas(treeFrame, width=1840, height=540)

LabelA = Label(treeFrame,text='A',font=("Helvetica", 18)).grid(row=1, column=0)
# root node
NodeA = canvas.create_oval(720, 20, 780, 80)





# f.pack(side=LEFT, expand = 1)

# f3 = Frame(f, bg = "red", width = 500)
# f3.pack(side=LEFT, expand = 1, pady = 50, padx = 50)

# f2 = Frame(root, bg = "black", height=100, width = 100)
# f2.pack(side=LEFT, fill = Y)

# b = Button(f2, text = "test")
# b.pack()

# b = Button(f3, text = "1", bg = "red")
# b.grid(row=1, column=3)
# b2 = Button(f3, text = "2")
# b2.grid(row=1, column=4)
# b3 = Button(f3, text = "2")
# b3.grid(row=2, column=0)

root.mainloop()