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
    global frame1, frame2, frame3, s
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
    btn = Button(frame3, text="Foglalás", style="TButton", command=foglalas)
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

def foglalas():
    tpl2 = Toplevel()
    tpl2.geometry('600x600')
    tpl2.title('Foglalás')
    tpl2.resizable(False, False)
    fogcim = Label(tpl2, text='Foglalás', font=('Helvetica', 35, 'bold'), bootstyle="success")
    fogcim.pack(pady=(10,20))
    style1 = Style()
    style1.configure("success.TButton", font=("Helvetica", 15, 'bold'))
    frame4 = Frame(tpl2, style='My.TFrame')
    frame4.pack()
    frame5 = Frame(tpl2, style='My.TFrame')
    frame5.pack()

    label1 = Label(frame4, text='1.', font=("Helvetica", 20, 'bold'), foreground='white', background='#00495c')
    label1.grid(row=0,column=0, padx=(10,0))

    seat11 = Button(frame4, text='1', style='success.TButton')
    seat11.grid(row=0, column=1, padx=(10,5), pady=10)

    seat21 = Button(frame4, text='2', style='success.TButton')
    seat21.grid(row=0, column=2, padx=5, pady=10)

    seat31 = Button(frame4, text='3', style='success.TButton')
    seat31.grid(row=0, column=3, padx=5, pady=10)

    seat41 = Button(frame4, text='4', style='success.TButton')
    seat41.grid(row=0, column=4, padx=(5,25), pady=10)

    seat51 = Button(frame4, text='5', style='success.TButton')
    seat51.grid(row=0, column=5, padx=(25,5), pady=10)

    seat61 = Button(frame4, text='6', style='success.TButton')
    seat61.grid(row=0, column=6, padx=5, pady=10)

    seat71 = Button(frame4, text='7', style='success.TButton')
    seat71.grid(row=0, column=7, padx=5, pady=10)

    seat81 = Button(frame4, text='8', style='success.TButton')
    seat81.grid(row=0, column=8, padx=5, pady=10)

    seat91 = Button(frame4, text='9', style='success.TButton')
    seat91.grid(row=0, column=9, padx=(5,10), pady=10)

    label2 = Label(frame4, text='2.', font=("Helvetica", 20, 'bold'), foreground='white', background='#00495c')
    label2.grid(row=1,column=0, padx=(10,0))

    seat12 = Button(frame4, text='1', style='success.TButton')
    seat12.grid(row=1, column=1, padx=(10,5))

    seat22 = Button(frame4, text='2', style='success.TButton')
    seat22.grid(row=1, column=2, padx=5)

    seat32 = Button(frame4, text='3', style='success.TButton')
    seat32.grid(row=1, column=3, padx=5)

    seat42 = Button(frame4, text='4', style='success.TButton')
    seat42.grid(row=1, column=4, padx=(5,25))

    seat52 = Button(frame4, text='5', style='success.TButton')
    seat52.grid(row=1, column=5, padx=(25,5))

    seat62 = Button(frame4, text='6', style='success.TButton')
    seat62.grid(row=1, column=6, padx=5)

    seat72 = Button(frame4, text='7', style='success.TButton')
    seat72.grid(row=1, column=7, padx=5)

    seat82 = Button(frame4, text='8', style='success.TButton')
    seat82.grid(row=1, column=8, padx=5)

    seat92 = Button(frame4, text='9', style='success.TButton')
    seat92.grid(row=1, column=9, padx=(5,10))

    label3 = Label(frame4, text='3.', font=("Helvetica", 20, 'bold'), foreground='white', background='#00495c')
    label3.grid(row=2,column=0, padx=(10,0))

    seat13 = Button(frame4, text='1', style='success.TButton')
    seat13.grid(row=2, column=1, padx=(10,5), pady=10)

    seat23 = Button(frame4, text='2', style='success.TButton')
    seat23.grid(row=2, column=2, padx=5, pady=10)

    seat33 = Button(frame4, text='3', style='success.TButton')
    seat33.grid(row=2, column=3, padx=5, pady=10)

    seat43 = Button(frame4, text='4', style='success.TButton')
    seat43.grid(row=2, column=4, padx=(5,25), pady=10)

    seat53 = Button(frame4, text='5', style='success.TButton')
    seat53.grid(row=2, column=5, padx=(25,5), pady=10)

    seat63 = Button(frame4, text='6', style='success.TButton')
    seat63.grid(row=2, column=6, padx=5, pady=10)

    seat73 = Button(frame4, text='7', style='success.TButton')
    seat73.grid(row=2, column=7, padx=5, pady=10)

    seat83 = Button(frame4, text='8', style='success.TButton')
    seat83.grid(row=2, column=8, padx=5, pady=10)

    seat93 = Button(frame4, text='9', style='success.TButton')
    seat93.grid(row=2, column=9, padx=(5,10), pady=10)

    label4 = Label(frame4, text='4.', font=("Helvetica", 20, 'bold'), foreground='white', background='#00495c')
    label4.grid(row=3,column=0, padx=(10,0))

    seat14 = Button(frame4, text='1', style='success.TButton')
    seat14.grid(row=3, column=1, padx=(10,5))

    seat24 = Button(frame4, text='2', style='success.TButton')
    seat24.grid(row=3, column=2, padx=5)

    seat34 = Button(frame4, text='3', style='success.TButton')
    seat34.grid(row=3, column=3, padx=5)

    seat44 = Button(frame4, text='4', style='success.TButton')
    seat44.grid(row=3, column=4, padx=(5,25))

    seat54 = Button(frame4, text='5', style='success.TButton')
    seat54.grid(row=3, column=5, padx=(25,5))

    seat64 = Button(frame4, text='6', style='success.TButton')
    seat64.grid(row=3, column=6, padx=5)

    seat74 = Button(frame4, text='7', style='success.TButton')
    seat74.grid(row=3, column=7, padx=5)

    seat84 = Button(frame4, text='8', style='success.TButton')
    seat84.grid(row=3, column=8, padx=5)

    seat94 = Button(frame4, text='9', style='success.TButton')
    seat94.grid(row=3, column=9, padx=(5,10))

    label5 = Label(frame5, text='5.', font=("Helvetica", 20, 'bold'), foreground='white', background='#00495c')
    label5.grid(row=0,column=0, padx=(10,0))

    seat15 = Button(frame5, text='1', style='success.TButton')
    seat15.grid(row=0, column=1, padx=(10,5), pady=10)

    seat25 = Button(frame5, text='2', style='success.TButton')
    seat25.grid(row=0, column=2, padx=5, pady=10)

    seat35 = Button(frame5, text='3', style='success.TButton')
    seat35.grid(row=0, column=3, padx=5, pady=10)

    seat45 = Button(frame5, text='4', style='success.TButton')
    seat45.grid(row=0, column=4, padx=4, pady=10)

    seatblock = Button(frame5, text='+', style='success.TButton')
    seatblock.grid(row=0, column=5, padx=4, pady=10)

    seat55 = Button(frame5, text='5', style='success.TButton')
    seat55.grid(row=0, column=6, padx=4, pady=10)

    seat65 = Button(frame5, text='6', style='success.TButton')
    seat65.grid(row=0, column=7, padx=5, pady=10)

    seat75 = Button(frame5, text='7', style='success.TButton')
    seat75.grid(row=0, column=8, padx=5, pady=10)

    seat85 = Button(frame5, text='8', style='success.TButton')
    seat85.grid(row=0, column=9, padx=5, pady=10)

    seat95 = Button(frame5, text='9', style='success.TButton')
    seat95.grid(row=0, column=10, padx=(5,10), pady=10)
    
    mk = ttk.Menubutton(tpl2, text="Válassz termet!", style='Outline.TMenubutton', direction='below')
    mk.pack(pady=20)
    menu1 = Menu(mk, tearoff=False)
    menu1.add_command(label='1-es terem', command=lambda: on_menu_select(0))
    menu1.add_command(label='2-es terem', command=lambda: on_menu_select(1))
    menu1.add_command(label='3-as terem', command=lambda: on_menu_select(2))
    mk.config(menu=menu1)

    foglal = Button(tpl2, text='Foglal', style='success.TButton')
    foglal.pack()

    tpl2.mainloop()

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