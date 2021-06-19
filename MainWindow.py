from tkinter import *
from Nodes import *
from SearchAlgorithms import *

nodeK = Nodes([790, 380, 850, 440], None, None, "K")
nodeJ = Nodes([540, 380, 600, 440], None, None, "J")
nodeI = Nodes([460, 380, 520, 440], None, None, "I")
nodeH = Nodes([210, 380, 270, 440], None, None, "H")
nodeG = Nodes([1080, 260, 1140, 320], None, None, "G")
nodeF = Nodes([830, 260, 890, 320], None, None, "F")
nodeE = Nodes([660, 260, 720, 320], nodeJ, nodeK, "E")
nodeD = Nodes([330, 260, 390, 320], nodeH, nodeI, "D")
nodeC = Nodes([950, 140, 1010, 200], nodeF, nodeG, "C")
nodeB = Nodes([500, 140, 560, 200], nodeD, nodeE, "B")
nodeA = Nodes([720, 20, 780, 80], nodeB, nodeC, "A")
currentNode = nodeA
nodeToFind = nodeK


def InitializeWindow(canvas, root):
    # canvas.create_oval/create_line(x1, y1, x2, y2)

    LabelA = Label(
        root,
        text='A',
        font=("Helvetica", 14)).place(x=740, y=45)

    # root node
    NodeA = canvas.create_oval(720, 20, 780, 80)

    LeftEdgeA = canvas.create_line(720, 80, 550, 130)
    RightEdgeA = canvas.create_line(780, 80, 950, 130)

    LabelB = Label(
        root,
        text='B',
        font=("Helvetica", 14)).place(x=520, y=160)

    # node b starts from the x2 of LeftEdgeA - 50
    NodeB = canvas.create_oval(500, 140, 560, 200)

    LeftEdgeB = canvas.create_line(500, 200, 380, 250)
    RightEdgeB = canvas.create_line(560, 200, 660, 250)

    LabelC = Label(
        root,
        text='C',
        font=("Helvetica", 14)).place(x=970, y=165)

    # node c starts from x2 of RightEdgeA
    NodeC = canvas.create_oval(950, 140, 1010, 200)

    LeftEdgeC = canvas.create_line(950, 200, 880, 250)
    RightEdgeC = canvas.create_line(1010, 200, 1080, 250)

    LabelD = Label(
        root,
        text='D',
        font=("Helvetica", 14)).place(x=350, y=285)

    # node d starts from x2 of LeftEdgeB - 50
    NodeD = canvas.create_oval(330, 260, 390, 320)

    LeftEdgeD = canvas.create_line(330, 320, 260, 370)
    RightEdgeD = canvas.create_line(390, 320, 460, 370)

    LabelE = Label(
        root,
        text='E',
        font=("Helvetica", 14)).place(x=680, y=285)

    # node e starts from x2 of RightEdgeB
    NodeE = canvas.create_oval(660, 260, 720, 320)

    LeftEdgeE = canvas.create_line(660, 320, 590, 370)
    RightEdgeE = canvas.create_line(720, 320, 790, 370)

    LabelF = Label(
        root,
        text='F',
        font=("Helvetica", 14)).place(x=850, y=285)

    # node f starts from x2 of LeftEdgeC - 50
    NodeF = canvas.create_oval(830, 260, 890, 320)

    LabelG = Label(
        root,
        text='G',
        font=("Helvetica", 14)).place(x=1100, y=285)

    # node g starts from x2 of RightEdgeC
    NodeG = canvas.create_oval(1080, 260, 1140, 320)

    LabelH = Label(
        root,
        text='H',
        font=("Helvetica", 14)).place(x=230, y=405)

    # node h starts from x2 LeftEdgeD - 50
    NodeH = canvas.create_oval(210, 380, 270, 440)

    LabelI = Label(
        root,
        text='I',
        font=("Helvetica", 14)).place(x=485, y=405)

    # node I starts from x2 of RightEdgeD
    NodeI = canvas.create_oval(460, 380, 520, 440)

    LabelJ = Label(
        root,
        text='J',
        font=("Helvetica", 14)).place(x=560, y=405)

    # node J starts from x2 of LeftEdgeE - 50
    NodeJ = canvas.create_oval(540, 380, 600, 440)

    LabelK = Label(
        root,
        text='K',
        font=("Helvetica", 14)).place(x=810, y=405)
    # node k starts from x2 of RightEdgeE
    NodeK = canvas.create_oval(790, 380, 850, 440)


def Reset():
    canvas.delete("all")
    InitializeWindow(canvas, root)


def DepthFirstSearch():
    DFS(canvas, currentNode, nodeToFind)


def BreathFirstSearch():
    BFS(canvas, currentNode, nodeToFind)


def DepthLimitedSearch():
    DLS(canvas, currentNode, nodeToFind, 0)


def IteravtiveDepthFirstSearch():
    IDFS(canvas, currentNode, nodeToFind, 0)


root = Tk()
root.title("Supper!")
root.geometry("3840x2340")

canvas = Canvas(root, width=1840, height=540)
canvas.pack(pady=10)

clear_button = Button(root, text="Reset", width=10, height=2, bg="green", fg="white", command=Reset)
clear_button.place(x=10, y=750)

dfs_button = Button(root, text="Depth First Search", width=22, height=2, bg="black", fg="white",
                    command=DepthFirstSearch)
dfs_button.place(x=100, y=750)

bfs_button = Button(root, text="Breath First Search", width=22, height=2, bg="black", fg="white",
                    command=BreathFirstSearch)
bfs_button.place(x=270, y=750)

dls_button = Button(root, text="Depth Limited Search", width=22, height=2, bg="black", fg="white",
                    command=DepthLimitedSearch)
dls_button.place(x=440, y=750)

iterative_dfs_button = Button(root, text="Iterative Depth First Search", width=25, height=2, bg="black", fg="white",
                              command=IteravtiveDepthFirstSearch)
iterative_dfs_button.place(x=610, y=750)

InitializeWindow(canvas, root)

root.mainloop()
