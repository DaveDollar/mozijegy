from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
from tkinter import ttk, Canvas
from ttkbootstrap import *
from ttkbootstrap import Style, Window
from PIL import Image, ImageTk
import os
import time

global count11,count21,count31,count41,count51,count61,count71,count81,count91,count12,count22,count32,count42,count52,count62,count72,count82,count92,count13,count23,count33,count43,count53,count63,count73,count83,count93,count14,count24,count34,count44,count54,count64,count74,count84,count94,count15,count25,count35,count45,count55,count65,count75,count85,count95,countblock

idopontok = ['11:30', '13:30', '16:30', '17:00', '17:30', '18:00', '19:30', '20:30', '22:30']
count11,count21,count31,count41,count51,count61,count71,count81,count91,count12,count22,count32,count42,count52,count62,count72,count82,count92,count13,count23,count33,count43,count53,count63,count73,count83,count93,count14,count24,count34,count44,count54,count64,count74,count84,count94,count15,count25,count35,count45,count55,count65,count75,count85,count95,countblock = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

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
    global tpl2,mk,seat11,seat21,seat31,seat41,seat51,seat61,seat71,seat81,seat91,seat12,seat22,seat32,seat42,seat52,seat62,seat72,seat82,seat92,seat13,seat23,seat33,seat43,seat53,seat63,seat73,seat83,seat93,seat14,seat24,seat34,seat44,seat54,seat64,seat74,seat84,seat94,seat15,seat25,seat35,seat45,seat55,seat65,seat75,seat85,seat95,seatblock
    tpl2 = Toplevel()
    tpl2.geometry('600x600')
    tpl2.title('Foglalás')
    tpl2.resizable(False, False)
    tpl2.iconbitmap(path+'/imgs/cinema.ico')
    fogcim = Label(tpl2, text='Foglalás', font=('Helvetica', 35, 'bold'), bootstyle="success")
    fogcim.pack(pady=(10,20))
    style1 = Style()
    style1.configure("success.TButton", font=("Helvetica", 15, 'bold'))
    style2 = Style()
    style2.configure("TButton", font=("Helvetica", 13, 'bold'))
    styl3 = Style()
    styl3.configure("TMenubutton", font=("Helvetica", 11))
    style4 = Style()
    style4.configure("warning.TButton", font=("Helvetica", 15, 'bold'))
    style5 = Style()
    style5.configure("info.TButton", font=("Helvetica", 15, 'bold'))
    frame4 = Frame(tpl2, style='My.TFrame')
    frame4.pack()
    frame5 = Frame(tpl2, style='My.TFrame')
    frame5.pack()

    label1 = Label(frame4, text='1.', font=("Helvetica", 20, 'bold'), foreground='white', background='#00495c')
    label1.grid(row=0,column=0, padx=(10,0))

    seat11 = Button(frame4, text='1', style='success.TButton', command=lambda: btnclick(11))
    seat11.grid(row=0, column=1, padx=(10,5), pady=10)

    seat21 = Button(frame4, text='2', style='success.TButton', command=lambda: btnclick(21))
    seat21.grid(row=0, column=2, padx=5, pady=10)

    seat31 = Button(frame4, text='3', style='success.TButton', command=lambda: btnclick(31))
    seat31.grid(row=0, column=3, padx=5, pady=10)

    seat41 = Button(frame4, text='4', style='success.TButton', command=lambda: btnclick(41))
    seat41.grid(row=0, column=4, padx=(5,25), pady=10)

    seat51 = Button(frame4, text='5', style='success.TButton', command=lambda: btnclick(51))
    seat51.grid(row=0, column=5, padx=(25,5), pady=10)

    seat61 = Button(frame4, text='6', style='success.TButton', command=lambda: btnclick(61))
    seat61.grid(row=0, column=6, padx=5, pady=10)

    seat71 = Button(frame4, text='7', style='success.TButton', command=lambda: btnclick(71))
    seat71.grid(row=0, column=7, padx=5, pady=10)

    seat81 = Button(frame4, text='8', style='success.TButton', command=lambda: btnclick(81))
    seat81.grid(row=0, column=8, padx=5, pady=10)

    seat91 = Button(frame4, text='9', style='success.TButton', command=lambda: btnclick(91))
    seat91.grid(row=0, column=9, padx=(5,10), pady=10)

    label2 = Label(frame4, text='2.', font=("Helvetica", 20, 'bold'), foreground='white', background='#00495c')
    label2.grid(row=1,column=0, padx=(10,0))

    seat12 = Button(frame4, text='1', style='success.TButton', command=lambda: btnclick(12))
    seat12.grid(row=1, column=1, padx=(10,5))

    seat22 = Button(frame4, text='2', style='success.TButton', command=lambda: btnclick(22))
    seat22.grid(row=1, column=2, padx=5)

    seat32 = Button(frame4, text='3', style='success.TButton', command=lambda: btnclick(32))
    seat32.grid(row=1, column=3, padx=5)

    seat42 = Button(frame4, text='4', style='success.TButton', command=lambda: btnclick(42))
    seat42.grid(row=1, column=4, padx=(5,25))

    seat52 = Button(frame4, text='5', style='success.TButton', command=lambda: btnclick(52))
    seat52.grid(row=1, column=5, padx=(25,5))

    seat62 = Button(frame4, text='6', style='success.TButton', command=lambda: btnclick(62))
    seat62.grid(row=1, column=6, padx=5)

    seat72 = Button(frame4, text='7', style='success.TButton', command=lambda: btnclick(72))
    seat72.grid(row=1, column=7, padx=5)

    seat82 = Button(frame4, text='8', style='success.TButton', command=lambda: btnclick(82))
    seat82.grid(row=1, column=8, padx=5)

    seat92 = Button(frame4, text='9', style='success.TButton', command=lambda: btnclick(92))
    seat92.grid(row=1, column=9, padx=(5,10))

    label3 = Label(frame4, text='3.', font=("Helvetica", 20, 'bold'), foreground='white', background='#00495c')
    label3.grid(row=2,column=0, padx=(10,0))

    seat13 = Button(frame4, text='1', style='success.TButton', command=lambda: btnclick(13))
    seat13.grid(row=2, column=1, padx=(10,5), pady=10)

    seat23 = Button(frame4, text='2', style='success.TButton', command=lambda: btnclick(23))
    seat23.grid(row=2, column=2, padx=5, pady=10)

    seat33 = Button(frame4, text='3', style='success.TButton', command=lambda: btnclick(33))
    seat33.grid(row=2, column=3, padx=5, pady=10)

    seat43 = Button(frame4, text='4', style='success.TButton', command=lambda: btnclick(43))
    seat43.grid(row=2, column=4, padx=(5,25), pady=10)

    seat53 = Button(frame4, text='5', style='success.TButton', command=lambda: btnclick(53))
    seat53.grid(row=2, column=5, padx=(25,5), pady=10)

    seat63 = Button(frame4, text='6', style='success.TButton', command=lambda: btnclick(63))
    seat63.grid(row=2, column=6, padx=5, pady=10)

    seat73 = Button(frame4, text='7', style='success.TButton', command=lambda: btnclick(73))
    seat73.grid(row=2, column=7, padx=5, pady=10)

    seat83 = Button(frame4, text='8', style='success.TButton', command=lambda: btnclick(83))
    seat83.grid(row=2, column=8, padx=5, pady=10)

    seat93 = Button(frame4, text='9', style='success.TButton', command=lambda: btnclick(93))
    seat93.grid(row=2, column=9, padx=(5,10), pady=10)

    label4 = Label(frame4, text='4.', font=("Helvetica", 20, 'bold'), foreground='white', background='#00495c')
    label4.grid(row=3,column=0, padx=(10,0))

    seat14 = Button(frame4, text='1', style='success.TButton', command=lambda: btnclick(14))
    seat14.grid(row=3, column=1, padx=(10,5))

    seat24 = Button(frame4, text='2', style='success.TButton', command=lambda: btnclick(24))
    seat24.grid(row=3, column=2, padx=5)

    seat34 = Button(frame4, text='3', style='success.TButton', command=lambda: btnclick(34))
    seat34.grid(row=3, column=3, padx=5)

    seat44 = Button(frame4, text='4', style='success.TButton', command=lambda: btnclick(44))
    seat44.grid(row=3, column=4, padx=(5,25))

    seat54 = Button(frame4, text='5', style='success.TButton', command=lambda: btnclick(54))
    seat54.grid(row=3, column=5, padx=(25,5))

    seat64 = Button(frame4, text='6', style='success.TButton', command=lambda: btnclick(64))
    seat64.grid(row=3, column=6, padx=5)

    seat74 = Button(frame4, text='7', style='success.TButton', command=lambda: btnclick(74))
    seat74.grid(row=3, column=7, padx=5)

    seat84 = Button(frame4, text='8', style='success.TButton', command=lambda: btnclick(84))
    seat84.grid(row=3, column=8, padx=5)

    seat94 = Button(frame4, text='9', style='success.TButton', command=lambda: btnclick(94))
    seat94.grid(row=3, column=9, padx=(5,10))

    label5 = Label(frame5, text='5.', font=("Helvetica", 20, 'bold'), foreground='white', background='#00495c')
    label5.grid(row=0,column=0, padx=(10,0))

    seat15 = Button(frame5, text='1', style='success.TButton', command=lambda: btnclick(15))
    seat15.grid(row=0, column=1, padx=(10,5), pady=10)

    seat25 = Button(frame5, text='2', style='success.TButton', command=lambda: btnclick(25))
    seat25.grid(row=0, column=2, padx=5, pady=10)

    seat35 = Button(frame5, text='3', style='success.TButton', command=lambda: btnclick(35))
    seat35.grid(row=0, column=3, padx=5, pady=10)

    seat45 = Button(frame5, text='4', style='success.TButton', command=lambda: btnclick(45))
    seat45.grid(row=0, column=4, padx=4, pady=10)

    seatblock = Button(frame5, text='+', style='success.TButton', command=lambda: btnclick(00))
    seatblock.grid(row=0, column=5, padx=4, pady=10)

    seat55 = Button(frame5, text='5', style='success.TButton', command=lambda: btnclick(55))
    seat55.grid(row=0, column=6, padx=4, pady=10)

    seat65 = Button(frame5, text='6', style='success.TButton', command=lambda: btnclick(65))
    seat65.grid(row=0, column=7, padx=5, pady=10)

    seat75 = Button(frame5, text='7', style='success.TButton', command=lambda: btnclick(75))
    seat75.grid(row=0, column=8, padx=5, pady=10)

    seat85 = Button(frame5, text='8', style='success.TButton', command=lambda: btnclick(85))
    seat85.grid(row=0, column=9, padx=5, pady=10)

    seat95 = Button(frame5, text='9', style='success.TButton', command=lambda: btnclick(95))
    seat95.grid(row=0, column=10, padx=(5,10), pady=10)

    idolabel = Label(tpl2, text='Válassz időpontot!', font=('Helvetica', 20, 'bold'), bootstyle="success")
    idolabel.pack(pady=10)

    frame6 = Frame(tpl2, style='My.TFrame')
    frame6.pack()

    cal = DateEntry(frame6, width=16)
    cal.grid(row=0, column=0, padx=(10,5), pady=10)

    mk = ttk.Menubutton(frame6, text="Óra", style='TMenubutton', direction='below')
    mk.grid(row=0, column=1, padx=(5,10))
    menu1 = Menu(mk, tearoff=False)
    menu1.add_command(label=idopontok[0], command=lambda: idosdef(0))
    menu1.add_command(label=idopontok[1], command=lambda: idosdef(1))
    menu1.add_command(label=idopontok[2], command=lambda: idosdef(2))
    menu1.add_command(label=idopontok[3], command=lambda: idosdef(3))
    menu1.add_command(label=idopontok[4], command=lambda: idosdef(4))
    menu1.add_command(label=idopontok[5], command=lambda: idosdef(5))
    menu1.add_command(label=idopontok[6], command=lambda: idosdef(6))
    menu1.add_command(label=idopontok[7], command=lambda: idosdef(7))
    menu1.add_command(label=idopontok[8], command=lambda: idosdef(8))
    mk.config(menu=menu1)

    foglal = Button(tpl2, text='Foglal', style='success.TButton')
    foglal.pack(pady=(20,0))

    tpl2.mainloop()

def idosdef(n):
    mk.config(text=idopontok[n])

def btnclick(z):
    global count11,count21,count31,count41,count51,count61,count71,count81,count91,count12,count22,count32,count42,count52,count62,count72,count82,count92,count13,count23,count33,count43,count53,count63,count73,count83,count93,count14,count24,count34,count44,count54,count64,count74,count84,count94,count15,count25,count35,count45,count55,count65,count75,count85,count95, countblock
    if z == 11:
        if count11%2==0 or count11==0:
            seat11.config(style='info.TButton')
        else:
            seat11.config(style='success.TButton')
        count11+=1
    elif z == 21:
        if count21%2==0 or count21==0:
            seat21.config(style='info.TButton')
        else:
            seat21.config(style='success.TButton')
        count21+=1
    elif z == 31:
        if count31%2==0 or count31==0:
            seat31.config(style='info.TButton')
        else:
            seat31.config(style='success.TButton')
        count31+=1
    elif z == 41:
        if count41%2==0 or count41==0:
            seat41.config(style='info.TButton')
        else:
            seat41.config(style='success.TButton')
        count41+=1
    elif z == 51:
        if count51%2==0 or count51==0:
            seat51.config(style='info.TButton')
        else:
            seat51.config(style='success.TButton')
        count51+=1
    elif z == 61:
        if count61%2==0 or count61==0:
            seat61.config(style='info.TButton')
        else:
            seat61.config(style='success.TButton')
        count61+=1
    elif z == 71:
        if count71%2==0 or count71==0:
            seat71.config(style='info.TButton')
        else:
            seat71.config(style='success.TButton')
        count71+=1
    elif z == 81:
        if count81%2==0 or count81==0:
            seat81.config(style='info.TButton')
        else:
            seat81.config(style='success.TButton')
        count81+=1
    elif z == 91:
        if count91%2==0 or count91==0:
            seat91.config(style='info.TButton')
        else:
            seat91.config(style='success.TButton')
        count91+=1
    elif z == 12:
        if count12%2==0 or count12==0:
            seat12.config(style='info.TButton')
        else:
            seat12.config(style='success.TButton')
        count12+=1
    elif z == 22:
        if count22%2==0 or count22==0:
            seat22.config(style='info.TButton')
        else:
            seat22.config(style='success.TButton')
        count22+=1
    elif z == 32:
        if count32%2==0 or count32==0:
            seat32.config(style='info.TButton')
        else:
            seat32.config(style='success.TButton')
        count32+=1
    elif z == 42:
        if count42%2==0 or count42==0:
            seat42.config(style='info.TButton')
        else:
            seat42.config(style='success.TButton')
        count42+=1
    elif z == 52:
        if count52%2==0 or count52==0:
            seat52.config(style='info.TButton')
        else:
            seat52.config(style='success.TButton')
        count52+=1
    elif z == 62:
        if count62%2==0 or count62==0:
            seat62.config(style='info.TButton')
        else:
            seat62.config(style='success.TButton')
        count62+=1
    elif z == 72:
        if count72%2==0 or count72==0:
            seat72.config(style='info.TButton')
        else:
            seat72.config(style='success.TButton')
        count72+=1
    elif z == 82:
        if count82%2==0 or count82==0:
            seat82.config(style='info.TButton')
        else:
            seat82.config(style='success.TButton')
        count82+=1
    elif z == 92:
        if count92%2==0 or count92==0:
            seat92.config(style='info.TButton')
        else:
            seat92.config(style='success.TButton')
        count92+=1
    elif z == 13:
        if count13%2==0 or count13==0:
            seat13.config(style='info.TButton')
        else:
            seat13.config(style='success.TButton')
        count13+=1
    elif z == 23:
        if count23%2==0 or count23==0:
            seat23.config(style='info.TButton')
        else:
            seat23.config(style='success.TButton')
        count23+=1
    elif z == 33:
        if count33%2==0 or count33==0:
            seat33.config(style='info.TButton')
        else:
            seat33.config(style='success.TButton')
        count33+=1
    elif z == 43:
        if count43%2==0 or count43==0:
            seat43.config(style='info.TButton')
        else:
            seat43.config(style='success.TButton')
        count43+=1
    elif z == 53:
        if count53%2==0 or count53==0:
            seat53.config(style='info.TButton')
        else:
            seat53.config(style='success.TButton')
        count53+=1
    elif z == 63:
        if count63%2==0 or count63==0:
            seat63.config(style='info.TButton')
        else:
            seat63.config(style='success.TButton')
        count63+=1
    elif z == 73:
        if count73%2==0 or count73==0:
            seat73.config(style='info.TButton')
        else:
            seat73.config(style='success.TButton')
        count73+=1
    elif z == 83:
        if count83%2==0 or count83==0:
            seat83.config(style='info.TButton')
        else:
            seat83.config(style='success.TButton')
        count83+=1
    elif z == 93:
        if count93%2==0 or count93==0:
            seat93.config(style='info.TButton')
        else:
            seat93.config(style='success.TButton')
        count93+=1
    elif z == 14:
        if count14%2==0 or count14==0:
            seat14.config(style='info.TButton')
        else:
            seat14.config(style='success.TButton')
        count14+=1
    elif z == 24:
        if count24%2==0 or count24==0:
            seat24.config(style='info.TButton')
        else:
            seat24.config(style='success.TButton')
        count24+=1
    elif z == 34:
        if count34%2==0 or count34==0:
            seat34.config(style='info.TButton')
        else:
            seat34.config(style='success.TButton')
        count34+=1
    elif z == 44:
        if count44%2==0 or count44==0:
            seat44.config(style='info.TButton')
        else:
            seat44.config(style='success.TButton')
        count44+=1
    elif z == 54:
        if count54%2==0 or count54==0:
            seat54.config(style='info.TButton')
        else:
            seat54.config(style='success.TButton')
        count54+=1
    elif z == 64:
        if count64%2==0 or count64==0:
            seat64.config(style='info.TButton')
        else:
            seat64.config(style='success.TButton')
        count64+=1
    elif z == 74:
        if count74%2==0 or count74==0:
            seat74.config(style='info.TButton')
        else:
            seat74.config(style='success.TButton')
        count74+=1
    elif z == 84:
        if count84%2==0 or count84==0:
            seat84.config(style='info.TButton')
        else:
            seat84.config(style='success.TButton')
        count84+=1
    elif z == 94:
        if count94%2==0 or count94==0:
            seat94.config(style='info.TButton')
        else:
            seat94.config(style='success.TButton')
        count94+=1
    elif z == 15:
        if count15%2==0 or count15==0:
            seat15.config(style='info.TButton')
        else:
            seat15.config(style='success.TButton')
        count15+=1
    elif z == 25:
        if count25%2==0 or count25==0:
            seat25.config(style='info.TButton')
        else:
            seat25.config(style='success.TButton')
        count25+=1
    elif z == 35:
        if count35%2==0 or count35==0:
            seat35.config(style='info.TButton')
        else:
            seat35.config(style='success.TButton')
        count35+=1
    elif z == 45:
        if count45%2==0 or count45==0:
            seat45.config(style='info.TButton')
        else:
            seat45.config(style='success.TButton')
        count45+=1
    elif z == 00:
        if countblock%2==0 or countblock==0:
            seatblock.config(style='info.TButton')
        else:
            seatblock.config(style='success.TButton')
        countblock+=1
    elif z == 55:
        if count55%2==0 or count55==0:
            seat55.config(style='info.TButton')
        else:
            seat55.config(style='success.TButton')
        count55+=1
    elif z == 65:
        if count65%2==0 or count65==0:
            seat65.config(style='info.TButton')
        else:
            seat65.config(style='success.TButton')
        count65+=1
    elif z == 75:
        if count75%2==0 or count75==0:
            seat75.config(style='info.TButton')
        else:
            seat75.config(style='success.TButton')
        count75+=1
    elif z == 85:
        if count85%2==0 or count85==0:
            seat85.config(style='info.TButton')
        else:
            seat85.config(style='success.TButton')
        count85+=1
    elif z == 95:
        if count95%2==0 or count95==0:
            seat95.config(style='info.TButton')
        else:
            seat95.config(style='success.TButton')
        count95+=1


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