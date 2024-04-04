from tkinter import *
from tkinter import messagebox
from tkinter import ttk, Canvas
from ttkbootstrap import *
from ttkbootstrap import Style, Window
from PIL import Image, ImageTk
import os

def getpath():
    path = os.path.abspath(os.getcwd())
    ujpath = path.replace('\\','/')
    return ujpath
path = getpath()

def filmek():
    global tpl1
    tpl1 = Toplevel()
    tpl1.title("Filmek")
    tpl1.geometry("1100x600")
    tpl1.resizable(False, False)
    tpl1.iconbitmap(path+'/imgs/cinema.ico')
    cim = Label(tpl1, text='Filmek:', font=('Helvetica', 30, 'bold'), bootstyle="success")
    cim.pack(pady=10)
    style = Style()
    style.configure("Outline.TMenubutton", font=("Helvetica", 18))
    mb = ttk.Menubutton(tpl1, text="Válassz filmet!", style='Outline.TMenubutton', direction='below')
    mb.pack(pady=(0,10))
    menu = Menu(mb, tearoff=False)
    menu.add_command(label='A MÉHÉSZ', command=on_menu_select)
    menu.add_command(label='DEMON SLAYER - TO THE HASHIRA TRAINING (KIMETSU NO YAIBA)', command=lambda: on_menu_select(1))
    menu.add_command(label='DŰNE - MÁSODIK RÉSZ', command=lambda: on_menu_select(2))
    menu.add_command(label='MADAME WEB', command=lambda: on_menu_select(3))
    menu.add_command(label='IMÁDLAK UTÁLNI', command=lambda: on_menu_select(4))
    mb.config(menu=menu)
    tpl1.mainloop()


def on_menu_select():
    try:
        frame1.winfo_exists()
    except NameError:
        s = Style()
        s.configure('My.TFrame', background='aqua')
        frame1 = Frame(tpl1, style='My.TFrame')
        frame1.pack()
        frame2 = Frame(frame1)
        frame2.grid(row=0, column=0, pady=10)
        frame3 = Frame(frame1)
        frame3.grid(row=0, column=1)
        canvas = Canvas(frame2, width=300, height=430, bg='white')
        canvas.pack(padx=10)
        meheszkep = Image.open(path+'/imgs/amehesz.png')
        resized_mehesz = meheszkep.resize((300, 430))
        global keszmehesz  
        keszmehesz = ImageTk.PhotoImage(resized_mehesz)
        canvas.create_image(0, 0, anchor='nw', image=keszmehesz)
        meheszcim = Label(frame3, text='A méhész', font=('Helvetica', 30, "bold"), bootstyle="primary")
        meheszszoveg = Label(frame3, text="\nA méhész 2024-es amerikai akcióthriller, melyet Kurt Wimmer\nforgatókönyvéből David Ayer rendezett. A főbb szerepekben\nJason Statham, Emmy Raver-Lampman, Josh Hutcherson,  \nBobby Naderi, Minnie Driver, Phylicia Rashad és Jeremy Irons\nlátható. 2024. január 12-én mutatta be az Amazon MGM Studios.", font=('Helvetica', 18), justify="left", bootstyle="success")
        meheszcim.pack()
        meheszszoveg.pack()



root = Window(themename='solar')
root.title('MoziTown')
root.geometry('1100x600')
root.resizable(False, False)
root.iconbitmap(path+'/imgs/cinema.ico')


logoimg = Image.open(path+'/imgs/MoziTown.png')
resized_logo = logoimg.resize((500,500))
displaylogo = ImageTk.PhotoImage(resized_logo)
logo = Label(root, image=displaylogo)
logo.pack()


mystyle = Style()
mystyle.configure("success.Outline.TButton", font=("Helvetica", 24))

belepes = Button(root, text="Belépés", bootstyle="success", style="success.Outline.TButton", command=filmek)
belepes.pack()

root.mainloop()