from tkinter import *
from tkinter import messagebox
from ttkbootstrap import *

root = Tk()
root.title('MoziTown')
root.geometry('1200x600')
root.config(bg='#09295c')
root.resizable(False, False)
root.iconbitmap('./imgs/cinema.ico')

logoimg = PhotoImage(file='./imgs/MoziTown1.png')
logo = Label(root, image=logoimg, background='#09295c')
logo.place(relx=0.5, rely=0, anchor=N)

root.mainloop()