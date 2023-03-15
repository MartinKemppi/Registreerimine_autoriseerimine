from tkinter import *
from tkinter import messagebox
import os

filename = "logpass.txt"

def create_user():
    login = login_entry.get()
    password = password_entry.get()
    
    # kontrollige, kas sisselogimine on juba olemas
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            for line in f:
                if login in line:
                    messagebox.showerror("Viga", "See sisselogimine on juba olemas.")
                    return
    
    # salvestage kasutaja mandaadid faili
    with open(filename, "a") as f:
        f.write(f"{login},{password}\n")
    
    # näita kinnitusteadet
    messagebox.showinfo("Edu", "Kasutaja loodud edukalt.")
    
def remind_password():
    login = login_entry.get()
    
    # kontrollige, kas sisselogimine on olemas
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            for line in f:
                if login in line:
                    password = line.split(",")[1].strip()
                    print(f"Parool kasutaja: {login} on {password}")
                    return
    
    # näidata veateadet, kui sisselogimist ei leitud
    messagebox.showerror("Viga", "Seda sisselogimist ei eksisteeri.")

def login():
    if login_entry.get()=="": 
        login_entry.configure(bg="red")
    else:
        login_entry.configure(bg="lightblue")
    if password_entry.get()=="": 
        password_entry.configure(bg="red")
    else:
        password_entry.configure(bg="lightblue")
    login = login_entry.get()
    password = password_entry.get()
    
    # kontrollige, kas sisselogimine ja parool sobivad
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            for line in f:
                if login in line:
                    saved_password = line.split(",")[1].strip()
                    if password == saved_password:
                        # kui sisselogimine ja parool ühtivad, kuvage muutmise aken
                        modify_window = Toplevel(aken)
                        modify_window.title("Modify")
                        modify_label = Label(modify_window, text=f"Tere tulemast, {login}!")
                        modify_label.pack()
                        return
                    else:
                        messagebox.showerror("Viga", "Vale parool.")
                        return
    
    # näidata veateadet, kui sisselogimist ei leitud
    messagebox.showerror("Viga", "Seda sisselogimist ei eksisteeri.")

aken=Tk()
aken.geometry("800x400")
aken.title("Automatiseerimine")

lbl=Label(aken,text="Sisesta andmed automatiseerimiseks",font="Arial 10",height=5,width=40)
login_entry=Entry(aken,fg="blue",bg="lightblue",width=15,font="Arial 20",justify=LEFT)
password_entry=Entry(aken,show="*",fg="blue",bg="lightblue",width=15,font="Arial 20",justify=LEFT)
btn0=Button(aken,text="Logi sisse",font="Arial 12",relief=GROOVE,command=login)#SUNKEN, RAISED
btn1=Button(aken,text="Unustasin salasõna",font="Arial 12",relief=GROOVE,command=remind_password)#SUNKEN, RAISED
btn2=Button(aken,text="Loo uus kasutaja",font="Arial 12",relief=GROOVE,command=create_user)#SUNKEN, RAISED

lbl.pack()
login_entry.pack(padx=0,pady=0)
password_entry.pack(padx=1,pady=1)
btn0.place(x=280,y=175)
btn1.place(x=320,y=210)
btn2.place(x=380,y=175)

aken.mainloop()