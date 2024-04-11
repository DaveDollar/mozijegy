from tkinter import *
from tkinter import messagebox
from tkinter import ttk, Canvas
from ttkbootstrap import *
from ttkbootstrap import Style, Window
from PIL import Image, ImageTk
import os
import time

def getpath():
    path = os.path.abspath(os.getcwd())
    ujpath = path.replace('\\','/')
    return ujpath
path = getpath()

def on_closing():
    if messagebox.askyesno("Kilépés", "Biztos ki akarsz lépni?"):
        root.destroy()

def filmek():
    global tpl1
    root.iconify()
    tpl1 = Toplevel()
    tpl1.protocol("WM_DELETE_WINDOW", on_closing)
    tpl1.title("Filmek")
    tpl1.geometry("1100x550")
    tpl1.resizable(False, False)
    tpl1.iconbitmap(path+'/imgs/cinema.ico')
    foframe = Frame(tpl1)
    foframe.pack(pady=10)
    cim = Label(foframe, text='Filmek: ', font=('Helvetica', 35, 'bold'), bootstyle="success")
    cim.grid(row=0, column=0)
    style = Style()
    style.configure("Outline.TMenubutton", font=("Helvetica", 15))
    mb = ttk.Menubutton(foframe, text="Válassz filmet!", style='Outline.TMenubutton', direction='below')
    mb.grid(row=0, column=1)
    menu = Menu(mb, tearoff=False)
    menu.add_command(label='A MÉHÉSZ', command=lambda: on_menu_select(0))
    menu.add_command(label='DEMON SLAYER - TO THE HASHIRA TRAINING (KIMETSU NO YAIBA)', command=lambda: on_menu_select(1))
    menu.add_command(label='DŰNE - MÁSODIK RÉSZ', command=lambda: on_menu_select(2))
    menu.add_command(label='MADAME WEB', command=lambda: on_menu_select(3))
    menu.add_command(label='IMÁDLAK UTÁLNI', command=lambda: on_menu_select(4))
    mb.config(menu=menu)
    tpl1.mainloop()

def filmgen(kpath, kcim, ktext):
    global frame1, frame2, frame3
    s = Style()
    s.configure('My.TFrame', background='#00495c')
    frame1 = Frame(tpl1, style='My.TFrame')
    frame1.pack()
    frame2 = Frame(frame1, style='My.TFrame')
    frame2.grid(row=0, column=0, pady=10)
    frame3 = Frame(frame1, style='My.TFrame')
    frame3.grid(row=0, column=1)
    kep = Image.open(path+kpath)
    resized = kep.resize((300, 430))
    global kesz 
    kesz = ImageTk.PhotoImage(resized)
    keplabel = Label(frame2, image=kesz, background='#00495c')
    keplabel.pack(padx=10)
    cim = Label(frame3, text=kcim, font=('Helvetica', 30, "bold"), bootstyle="primary", background='#00495c')
    szoveg = Label(frame3, text=ktext, font=('Helvetica', 18), justify="left", bootstyle="success", background='#00495c')
    cim.pack()
    szoveg.pack(padx=(0,10))
    style = Style()
    style.configure("TButton", font=("Helvetica", 20))
    btn = Button(frame3, text="Foglalás", style="TButton")
    btn.pack(pady=(30,0))


def on_menu_select(choice):
    global frame1, frame2, frame3
    try:
        if frame1.winfo_exists():
            frame1.destroy()
            frame2.destroy()
            frame3.destroy()
            if choice == 0:
                filmgen('/imgs/amehesz.png','A méhész','\nA méhész 2024-es amerikai akcióthriller, melyet Kurt Wimmer\nforgatókönyvéből David Ayer rendezett. A főbb szerepekben\nJason Statham, Emmy Raver-Lampman, JoshHutcherson,  \nBobby Naderi, Minnie Driver, Phylicia Rashad és Jeremy Irons\nlátható. 2024. január 12-én mutatta be az Amazon MGM Studios.')
            elif choice == 1:
                filmgen('/imgs/demonslayer.jpg', 'Demon Slayer: To the Hashira Training', '\nEgy titkos szervezet vigyáz ránk. Ha a Kimetsu no Yaiba, a Demon\nSlayer nem létezne, a földet már démonok uralnák: ők viszont évszá-\nzadok óta küzdenek az egykori emberi lények ellen, akik haláluk után\nrendkívüli képességekre tettek szert: erősek, gyorsan gyógyulnak és\nszinte halhatatlanok.')
            elif choice == 2:
                filmgen('/imgs/dune2.jpg', 'Dűne: Második rész', '\nA távoli jövőben, a bolygóközi királyságok korában játszódó törté-\nnetben két nagyhatalmú uralkodóház harcol az Arrakis bolygó feletti\nhatalomért, mert az ismert univerzumban egyedül az itteni végtelen\nsivatagban bányászható az a fűszer, amely lehetővé teszi a csillag-\nközi utazást. A Harkonnenek ura kiirtatta az Atreides családot.')
            elif choice == 3:
                filmgen('/imgs/mw.jpg','Madame Web', '\nA Madame Web 2024-ben bemutatott amerikai szuperhősfilm\nS. J. Clarkson rendezésében. Gyártója a Columbia Pictures,\nMarvel Entertainment és Di Bonaventura Pictures, forgalmazója\na Sony Pictures Releasing. Ez a film a Sony Pókember univerzu-\nmának negyedik filmje.')
            elif choice == 4:
                filmgen('/imgs/imut.jpg','Imádlak utálni','\nAz Imádlak utálni 2023-as amerikai romantikus filmvígjáték, amelyet\nIlana Wolpert és Will Gluck forgatókönyvéből Gluck rendezett, William\nShakespeare Sok hűhó semmiért című műve alapján. A főbb szerepek-\nben Sydney Sweeney, Glen Powell, Alexandra Shipp, GaTa, Hadley\nRobinson, Michelle Hurd, Dermot Mulroney, Darren Barnet, Bryan\nBrown és Rachel Griffiths látható.')
    except Exception:
        if choice == 0:
                filmgen('/imgs/amehesz.png','A méhész','\nA méhész 2024-es amerikai akcióthriller, melyet Kurt Wimmer\nforgatókönyvéből David Ayer rendezett. A főbb szerepekben\nJason Statham, Emmy Raver-Lampman, JoshHutcherson,  \nBobby Naderi, Minnie Driver, Phylicia Rashad és Jeremy Irons\nlátható. 2024. január 12-én mutatta be az Amazon MGM Studios.')
        elif choice == 1:
            filmgen('/imgs/demonslayer.jpg', 'Demon Slayer: To the Hashira Training', '\nEgy titkos szervezet vigyáz ránk. Ha a Kimetsu no Yaiba, a Demon\nSlayer nem létezne, a földet már démonok uralnák: ők viszont évszá-\nzadok óta küzdenek az egykori emberi lények ellen, akik haláluk után\nrendkívüli képességekre tettek szert: erősek, gyorsan gyógyulnak és\nszinte halhatatlanok.')
        elif choice == 2:
            filmgen('/imgs/dune2.jpg', 'Dűne: Második rész', '\nA távoli jövőben, a bolygóközi királyságok korában játszódó törté-\nnetben két nagyhatalmú uralkodóház harcol az Arrakis bolygó feletti\nhatalomért, mert az ismert univerzumban egyedül az itteni végtelen\nsivatagban bányászható az a fűszer, amely lehetővé teszi a csillag-\nközi utazást. A Harkonnenek ura kiirtatta az Atreides családot.')
        elif choice == 3:
            filmgen('/imgs/mw.jpg','Madame Web', '\nA Madame Web 2024-ben bemutatott amerikai szuperhősfilm\nS. J. Clarkson rendezésében. Gyártója a Columbia Pictures,\nMarvel Entertainment és Di Bonaventura Pictures, forgalmazója\na Sony Pictures Releasing. Ez a film a Sony Pókember univerzu-\nmának negyedik filmje.')
        elif choice == 4:
            filmgen('/imgs/imut.jpg','Imádlak utálni','\nAz Imádlak utálni 2023-as amerikai romantikus filmvígjáték, amelyet\nIlana Wolpert és Will Gluck forgatókönyvéből Gluck rendezett, William\nShakespeare Sok hűhó semmiért című műve alapján. A főbb szerepek-\nben Sydney Sweeney, Glen Powell, Alexandra Shipp, GaTa, Hadley\nRobinson, Michelle Hurd, Dermot Mulroney, Darren Barnet, Bryan\nBrown és Rachel Griffiths látható.')




root = Window(themename='solar')
root.title('MoziTown')
root.geometry('600x600')
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