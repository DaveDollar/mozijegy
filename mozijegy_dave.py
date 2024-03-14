from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkbootstrap import *
from ttkbootstrap import Style, Window
from PIL import Image, ImageTk

def filmek():
    tpl1 = Toplevel()
    tpl1.title("Filmek")
    tpl1.geometry("1000x600")
    tpl1.resizable(False, False)
    tpl1.iconbitmap('J:\Python\mozijegy\imgs\cinema.ico')
    cim = Label(tpl1, text='Filmek:', font=('Helvetica', 25))
    cim.pack(pady=10)
    style = Style()
    style.configure("Outline.TMenubutton", font=("Helvetica", 18))
    mb = ttk.Menubutton(tpl1, text="Válassz filmet!", style='Outline.TMenubutton', direction='below')
    mb.pack()
    menu = Menu(mb, tearoff=False)
    menu.add_command(label='Option 1', command=lambda: on_menu_select('Option 1'))
    menu.add_command(label='Option 2', command=lambda: on_menu_select('Option 2'))
    menu.add_command(label='Option 3', command=lambda: on_menu_select('Option 3'))
    mb.config(menu=menu)
    tpl1.mainloop()

def on_menu_select(choice):
    print("Selected:", choice)

root = Window(themename='solar')
root.title('MoziTown')
root.geometry('1000x600')
root.resizable(False, False)
root.iconbitmap('J:\Python\mozijegy\imgs\cinema.ico')


logoimg = Image.open('J:\Python\mozijegy\imgs\MoziTown.png')
resized_logo = logoimg.resize((500,500))
displaylogo = ImageTk.PhotoImage(resized_logo)
logo = Label(root, image=displaylogo)
logo.pack()


mystyle = Style()
mystyle.configure("success.Outline.TButton", font=("Helvetica", 24))

belepes = Button(root, text="Belépés", bootstyle="success", style="success.Outline.TButton", command=filmek)
belepes.pack()

root.mainloop()