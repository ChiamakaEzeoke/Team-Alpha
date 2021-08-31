from serialise import serialise, bfs_console, getHeight
from tkinter import *
from algorithms import *



root = Tk()
root.title("Group Alpha")
root.geometry("3840x2340")

canvas = Canvas(root, width=1840, height=450, bg='cyan')

canvas.pack(pady=10)

frame = Frame(root, bg = "orange", width=1000, height=300)
frame.place(x=10, y=750)


textBox=Entry(frame, width=30)
textBox.grid(row=2, column=2)

def init():
    values = [1,2,3,4,5, 6, 7,8, 9]

    coords = [ [720, 20, 780, 80], [500, 140, 560, 200], [950, 140, 1010, 200], [330, 260, 390, 320], [660, 260, 720, 320], [830, 260, 890, 320], [1080, 260, 1140, 320], [210, 380, 270, 440], [460, 380, 520, 440], [540, 380, 600, 440],[790, 380, 850, 440]]

    tree = serialise(values, coords)

    height = getHeight(tree)

    createTree(tree, height)

    return tree


def clear():
    canvas.delete("all")
    init()
    textBox.delete(0, END)
    




def createTree(node, depth):
    if not node:
        return
    # Elements of the node are its label and Edges 
    [x, y, xn, yn] = node.coords
    createOval(x, y ,xn, yn)
    label = createLabel(node.val, x+20, y+25)
    if node.left:
        createEdges(x, y+60, xn-150, yn+50)
        createTree(node.left, depth)
    if node.right:
        createEdges(x+60, y+60, xn+100, yn+50)
        createTree(node.right, depth)

    


def createOval(x, y, xn, yn):
    canvas.create_oval(x, y, xn, yn)




def createLabel(text, x, y):
    return Label(
        root,
        text=text,
        font=("Helvetica", 14)).place(x=x, y=y)



def createEdges(x, y, xn, yn):
    canvas.create_line(x, y, xn, yn)
head = init()


textBox=Entry(frame, width=30)
textBox.grid(row=2, column=2)

def retrieve_input():
    if textBox.get():
        return int(textBox.get())
    messagebox.show('Please enter Input')




def createButtons(canvas, head):
    Button(frame, text='Clear Result', command=clear, width=22, height=4, bg='#ffb3fe', fg="black").grid(row=0,column=0)
    Button(frame, text='Depth First Search', command=lambda: DFS(canvas, head, retrieve_input()), width=22, height=4, bg='#ffb3fe', fg="black").grid(row=0,column=1)
    Button(frame, text='Breath First Search', command=lambda: BFS(canvas, head, retrieve_input()), width=22, height=4, bg='#ffb3fe', fg="black").grid(row=0, column=2)
    Button(frame, text='Depth Limiting Search', command=lambda: DLS(canvas, head, retrieve_input()), width=22, height=4, bg='#ffb3fe', fg="black").grid(row=0, column=3)
    Button(frame, text='Iterative Deepening Search', command=lambda: IDFS(canvas, head, retrieve_input()), width=22, height=4, bg='#ffb3fe', fg="black").grid(row=0, column=4)
    Button(frame, text='Uniform Cost Search', command=lambda: UCS(canvas, head, retrieve_input()), width=22, height=4, bg='#ffb3fe', fg="black").grid(row=0, column=5)


   







head = init()


find = 6

createButtons(canvas, head)





root.mainloop()


