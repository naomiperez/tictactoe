from tkinter import ttk 
import tkinter.messagebox

root = tkinter.Tk()
# tk.title("Tic Tac Toe")
style = ttk.Style()

# Label styling
style.configure("BW.TLabel", foreground="black", background="white")

l1 = ttk.Label(text="Test", style="BW.TLabel")


pa = tkinter.StringVar()
playerb = tkinter.StringVar()

# frame = Frame(width=768, height=576, bg="", colormap="new")
# frame.pack()

# binds the entry widgets to a StringVar instance
p1 = tkinter.StringVar()
p2 = tkinter.StringVar()

# enter or display a single line of text
player1_name = ttk.Entry(root, textvariable=p1)
player1_name.grid(row=1, column=1, columnspan=8, pady=5)
# enter or display a single line of text
player2_name = ttk.Entry(root, textvariable=p2)
player2_name.grid(row=2, column=1, columnspan=8, pady=20)

bclick = True
flag = 0

# TKinter button options
# command: A function to be called when button is pressed.
# text: Text which appears on the Button.
# image: Image to be apper on the Button.
# style: Style to be used in rendering this button.

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

# controls 
def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, playerb, pa

    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        playerb = p2.get() + " Wins!"
        pa = p1.get() + " Wins!"
        checkForWin()
        flag += 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

    elif(flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)


buttons = tkinter.StringVar()

# button style
# label style
style.configure("BW.TLabel", foreground="black", background="white", font='Helvetica 20', height=1, width=8)

style.configure('TButton', font =
               ('calibri', 70, 'bold'), 
                background = 'gray', height=7, width=2, borderwidth=5)
# style.map('TButton', foreground = [('active', '! disabled', 'green')], 
#                      background = [('active', 'black')]) 

label = ttk.Label(root, text="Player 1:", style='BW.TLabel')
label.grid(row=1, column=0)


label = ttk.Label(root, text="Player 2:", style='BW.TLabel')
label.grid(row=2, column=0, padx=10, pady=10)

button1 = ttk.Button(root, text=" ", command=lambda: btnClick(button1))
button1.grid(row=3, column=0, padx=10, pady=10)

button2 = ttk.Button(root, text=' ', command=lambda: btnClick(button2))
button2.grid(row=3, column=1, padx=10, pady=10)

button3 = ttk.Button(root, text=' ', command=lambda: btnClick(button3))
button3.grid(row=3, column=2, padx=10, pady=10)

button4 = ttk.Button(root, text=' ', command=lambda: btnClick(button4))
button4.grid(row=4, column=0, padx=10, pady=10)

button5 = ttk.Button(root, text=' ', command=lambda: btnClick(button5))
button5.grid(row=4, column=1, padx=10, pady=10)

button6 = ttk.Button(root, text=' ', command=lambda: btnClick(button6))
button6.grid(row=4, column=2, padx=10, pady=10)

button7 = ttk.Button(root, text=' ', command=lambda: btnClick(button7))
button7.grid(row=5, column=0, padx=10, pady=10)

button8 = ttk.Button(root, text=' ', command=lambda: btnClick(button8))
button8.grid(row=5, column=1, padx=10, pady=10)

button9 = ttk.Button(root, text=' ', command=lambda: btnClick(button9))
button9.grid(row=5, column=2, padx=10, pady=10)

tkinter.mainloop()