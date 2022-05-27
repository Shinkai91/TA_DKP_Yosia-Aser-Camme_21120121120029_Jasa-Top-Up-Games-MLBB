from cProfile import label
from http import server
from tkinter.ttk import Progressbar
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
import datetime as dt

w=Tk()
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
w.overrideredirect(1)
s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)

class Loginregisteruser:
    def main_screen(self):
        Label(text="SELAMAT DATANG DI JB-in Aja",bg='blue',width='300',height='2',font= ('courier new',13,"bold"),fg='white').pack()       
        Button(text='Login',bg= "grey",fg='white',height= '2',width= '30',command = self.login).place(x=420, y=270)
        Button(text='Register',bg = 'grey',fg='white',height= '2',width= '30',command=self.register).place(x=420, y=320)
    
    def __init__(self,gui,header):
        self.gui = gui
        self.gui.geometry('1041x583')
        self.gui.title(header)
        self.gui.resizable(0,0)
        self.main_screen()

    def login(self):
        screen1 = Toplevel(app)
        screen1.title("Login JB-in aja")
        screen1.geometry('350x160')
        screen1.resizable(0,0)
        Label(screen1, text= "Email").pack()
        self.entryUser = Entry(screen1, width=30)
        self.entryUser.pack()
        Label(screen1, text = "Password").pack()
        self.entryPass = Entry(screen1,show='*',width=30)
        self.entryPass.pack()
        self.check = IntVar()
        self.showPass = Checkbutton(screen1, text = "Show Password", variable=self.check,command=self.open_password).pack(expand=False,fill=BOTH,padx=10,pady=5)
        self.showPass
        self.btnlogin = Button(screen1, text="Login", bg= 'white',fg='black',command=self.do_login).pack(side=LEFT,expand=True,fill= BOTH, padx= 10,pady=5)
 
    def register(self):
        global screen1
        screen1 = Toplevel(app)
        screen1.title("Register JB-in aja")
        screen1.geometry('350x200')
        screen1.resizable(0,0)
        Label(screen1, text= "Username").pack()
        self.entryUserName = Entry(screen1, width=30)
        self.entryUserName.pack()
        Label(screen1, text= "Email").pack()
        self.entryUser = Entry(screen1, width=30)
        self.entryUser.pack()
        Label(screen1, text = "Password").pack()
        self.entryPass = Entry(screen1,show='*',width=30)
        self.entryPass.pack()
        self.check = IntVar()
        self.showPass = Checkbutton(screen1, text = "Show Password", variable=self.check,command=self.open_password).pack(expand=False,fill=BOTH,padx=10,pady=5)
        self.showPass
        self.btnregister = Button(screen1, text="Register", bg= 'white',fg='black', command=self.register_user).pack(side=LEFT,expand=True,fill= BOTH, padx= 10,pady=5)
        self.btnlogin = Button(screen1, text="Login", bg= 'white',fg='black',command=self.login).pack(side=LEFT,expand=True,fill= BOTH, padx= 10,pady=5)

    def register_user(self):
        get_name = self.entryUserName.get()
        get_email = self.entryUser.get()
        get_password = self.entryPass.get()
        
        if get_name == "":
            msg.showerror('Registrasi Gagal','Username Tidak Boleh Kosong',parent=self.gui)
            self.delete_uname()
        elif len(get_name) >0 and len(get_name) <=7:
            msg.showerror('Registrasi Gagal','Username Terlalu Pendek',parent=self.gui)
            self.delete_uname()
        elif len(get_email) >0 and len(get_email) <=10:
            msg.showerror('Registrasi Gagal','Email Terlalu Pendek',parent=self.gui)
            self.delete_email()
        elif get_email == "":
            msg.showerror('Registrasi Gagal','Email Tidak Boleh Kosong',parent=self.gui)
            self.delete_email()
        elif "@gmail.com" not in get_email:
            msg.showerror("Registrasi Gagal",'Harap Menyertakan Domain (@gmail.com)',parent=self.gui)
            self.delete_email()
        elif " " in get_email:
            msg.showerror("Registrasi Gagal",'Alamat Email Tidak Boleh Menggunakan Spasi',parent=self.gui)
            self.delete_email()
        elif get_password == "":
            msg.showerror('Registrasi Gagal','Password Tidak Boleh Kosong',parent=self.gui)
            self.delete_pass()
        elif len(get_password)  <=8 and len(get_password) >0:
            msg.showerror('Registrasi Gagal','Password Terlalu Pendek',parent=self.gui)
            self.delete_pass()
        else :
            file = open('database.txt','a')
            file.write("\n"+get_name+","+get_email+","+get_password)
            file.close()
            self.entryUserName.delete(0,END)
            self.entryUser.delete(0,END)
            self.entryPass.delete(0,END)
            msg.showinfo('Success','Registry Successed',parent=self.gui)
    
    def do_login(self):
        get_username = self.entryUser.get()
        get_password = self.entryPass.get()
        sukses = False
        file = open('database.txt','r')
        
        for i in file :
            id,email,password = i.split(",")
            password = password.strip()
            if get_username == email and get_password == password:
                sukses = True
                break
        if (sukses):
            msg.showinfo("Login Success","Selamat Datang Di JB-in Diamond %s"%(id),parent=self.gui)
            self.sec_screen()
            return 
        elif get_username == '' or get_password == '':
            msg.showwarning("Login Gagal","Email atau Password Tidak Boleh Kosong",parent=self.gui)
            self.entryUser.focus_set()
        else :
            msg.showerror('Login Gagal','Email atau Password Salah',parent=self.gui)
            self.delete_data()
    
   
    def open_password(self):
        Show = self.check.get()

        if Show == 1:
            self.entryPass['show']=''
        else :
            self.entryPass['show']='*'
    
    def sec_screen(self):
        global screen2
        screen2 = Toplevel(app)
        screen2.title("JB-in aja")
        screen2.geometry('400x450')
        screen2.resizable(0,0)
              
        Label(screen2,text="DIAMOND MOBILE LEGENDS" ,bg='blue',width='300',height='2',font= ('courier new',13, "bold"),fg='white').pack()
        Label(screen2, text='').pack()
        Label(screen2,text= "User id\t\t:",).place(x=30, y=70)
        self.entryID = Entry(screen2, font = ("times new roman", 10))
        self.entryID.place(x=140, y=70)
        
        self.radio = StringVar(value="...")
        Label(screen2, text = "Server\t\t:").place(x=30, y=90)
        self.entrySrv1 = Radiobutton(screen2, text = 'Asian', variable=self.radio,value="Asian",command=self.asia_srv)
        self.entrySrv1.place(x = 140, y = 90)
        self.entrySrv2 = Radiobutton(screen2, text = 'Europe', variable=self.radio,value="Europe",command=self.euro_srv)
        self.entrySrv2.place(x = 140, y = 110)
        self.entrySrv3 = Radiobutton(screen2, text = 'America', variable=self.radio,value="America",command=self.amer_srv)
        self.entrySrv3.place(x = 140, y = 130)
        
        Label(screen2, text='Region\t\t:').place(x=30, y=160)
        Label (screen2, text ="Price List\t\t:").place(x=30, y=180)
        self.radiobtn = IntVar()
        self.radio1 = Radiobutton(screen2, text="133 DM - 31K",variable = self.radiobtn,value=31000).place(x = 140, y = 180)
        self.radio2 = Radiobutton(screen2,text="266 DM - 63K",variable = self.radiobtn,value=63000).place(x = 140, y = 200)
        self.radio3 = Radiobutton(screen2,text="400 DM - 94K",variable = self.radiobtn,value=94000).place(x = 140, y = 220)
        self.radio4 = Radiobutton(screen2,text="670 DM - 156K",variable = self.radiobtn,value=156000).place(x = 260, y = 180)
        self.radio5 = Radiobutton(screen2,text="1342 DM - 311K",variable = self.radiobtn,value=311000).place(x = 260, y = 200)
        self.radio6 = Radiobutton(screen2,text="2700 DM - 622K",variable = self.radiobtn,value=622000).place(x = 260, y = 220)
       
        Label(screen2,text="Payment Method\t:").place(x=30, y=250)
        self.strpym = StringVar(value='...') 
        self.combobox1 = ttk.Combobox(screen2,width = 17,font = ("times new roman", 10), textvariable = self.strpym, state ="readonly")
        self.combobox1.place(x=140, y=250)
        self.combobox1['values'] = ('Gopay','Dana','OVO')
        
        btn = Button(screen2, text="Pay", command=self.payment,bg= 'lightgreen',state=ACTIVE)
        btn.place(x=270 ,y= 247)
        
        self.btnsub = Button(screen2, text="Order",font=('helvetica',13,'bold'),bg = "green",fg = "white",command = self.btn_sub,state = ACTIVE)
        self.btnsub.place(x = 320, y = 380)

    def payment(self):
        pym = self.strpym.get()

        if pym == 'Gopay' :
            Label(screen2,text= "No Handphone\t\t:",).place(x=30, y=280)
            self.entrynum = Entry(screen2, font = ("times new roman", 10))
            self.entrynum.place(x=140, y=280)
        elif pym == 'Dana':
            Label(screen2,text= "No Handphone\t\t:",).place(x=30, y=280)
            self.entrynum = Entry(screen2, font = ("times new roman", 10))
            self.entrynum.place(x=140, y=280)
        else :
            Label(screen2,text= "No Handphone\t\t:",).place(x=30, y=280)
            self.entrynum = Entry(screen2, font = ("times new roman", 10))
            self.entrynum.place(x=140, y=280)

    def btn_sub(self):
        id = self.entryID.get()
        srv = self.radio.get()
        nom = self.radiobtn.get()
        pym = self.strpym.get()
        date = dt.datetime.now()
        py = self.entrynum.get()

        if id == "":
            msg.showwarning("Peringatan","ID Tidak Boleh Kosong!",parent=self.gui)
            return
        if len(id) <= 6:
            msg.showwarning("Peringatan","ID Terlalu Pendek!",parent=self.gui)
            return
        if srv == "...":
            msg.showwarning("Peringatan","Server Tidak Boleh Kosong!",parent=self.gui)
            return
        if nom == 0:
            msg.showwarning("Peringatan","Harap Pilih Nominal Diamond!",parent=self.gui)
            return
        if pym == "...":
            msg.showwarning("Peringatan","Harap Pilih Metode Pembayaran!",parent=self.gui)
            return
        if py == "":
            msg.showwarning("Peringatan","No HP Tidak Boleh Kosong!",parent=self.gui)
            return
        if len(py) <= 10:
            msg.showwarning("Peringatan","No HP Terlalu Pendek!",parent=self.gui)
            return
        else :
            msg.showinfo("Top Up Diamond Mobile Legends Bang-Bang",f"User id\t\t\t: {self.entryID.get()} \nServer\t\t\t: {self.radio.get()} \nTanggal Pemesanan\t: {date:%A, %d %B %Y} \nMetode Pembayaran\t: {self.strpym.get()} \nNomor\t\t\t: {self.entrynum.get()} \nTotal Pembayaran\t\t: Rp.{self.radiobtn.get()},- \nStatus Pembayaran\t: Sedang Diproses!" )
            self.close_gui()

    def asia_srv(self):
        self.region = StringVar(value="...")
        self.region1 = ttk.Combobox(screen2,width=17,font=('times new romance',10),textvariable=self.region,state="readonly")
        self.region1.place(x=140, y=160)
        self.region1['values'] = ('Japan','Indonesia','China','Thailand','Philippines')
   
    def euro_srv(self):
        self.region = StringVar(value="...")
        self.region1 = ttk.Combobox(screen2, width=17,font=('times new romance',10),textvariable=self.region,state="readonly")
        self.region1.place(x=140, y=160)
        self.region1['values'] = ('Russia','Germany','Spain','France','Ukraine')
    
    def amer_srv(self):
        self.region = StringVar(value="...")
        self.region1 = ttk.Combobox(screen2,width=17,font=('times new romance',10),textvariable=self.region,state="readonly")
        self.region1.place(x=140, y=160)
        self.region1['values'] = ('South America','North America')

    def delete_data(self):
        self.entryUser.delete(0,END)
        self.entryPass.delete(0,END)
        self.entryUser.focus_set()
    
    def delete_uname(self): 
        self.entryPass.focus_set()
        self.entryUser.focus_set()
        self.entryUserName.delete(0,END)
        self.entryUserName.focus_set()
    
    def delete_email(self):
        self.entryUser.delete(0,END)
        self.entryPass.focus_set()
        self.entryUserName.focus_set()
        self.entryUser.focus_set()

    def delete_pass(self):
        self.entryPass.delete(0,END)
        self.entryUserName.focus_set()
        self.entryUser.focus_set()
        self.entryPass.focus_set()
        
    def close_gui(self):
        self.gui.destroy()

def new_win():
    global app
    app = Tk()
    logo = PhotoImage(file="logo.png")
    app.iconphoto(True,logo)
    bg = PhotoImage(file='Back.png')
    a_label = Label(app, image=bg)
    a_label.place(x=0, y=0, relheight=1, relwidth=1)
    start = Loginregisteruser(app,"JB-in Aja")
    app.mainloop()

def bar():
    l4=Label(w,text='Loading...',fg='white',bg=a)
    lst4=('Calibri (Body)',10)
    l4.config(font=lst4)
    l4.place(x=18,y=210)
    import time
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.03)
        r=r+1
    w.destroy()
    new_win()

progress.place(x=-10,y=235)
a='#249794'
bg = PhotoImage(file='logo.png')
a_label = Label(w, image=bg)
a_label.place(x=0, y=0, relheight=1, relwidth=1)
b1=Button(w,width=10,height=1,text='Get Started',command=bar,border=0,fg=a,bg='white')
b1.place(x=170,y=200)

l1=Label(w,text='JB-in Aja',fg='white',bg=a)
lst1=('Calibri (Body)',18,'bold')
l1.config(font=lst1)
l1.place(x=100,y=80)

l3=Label(w,text='Tempat Top Up Murah',fg='white',bg=a)
lst3=('Calibri (Body)',13)
l3.config(font=lst3)
l3.place(x=100,y=110)
w.mainloop()
