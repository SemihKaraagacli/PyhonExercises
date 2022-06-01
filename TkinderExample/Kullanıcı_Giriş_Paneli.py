from tkinter import *
from tkinter import messagebox

windows = Tk()
windows.title("*Tkinter Example | 1*")
windows.geometry("300x200")

windows.resizable(width=False,height=False)

lbl = Label(windows)
lbl.place(x=125, y=120)

def console():
    if (ent1.get() == str("Babayaga") and ent2.get() == str("123456789")):

        lbl ['text'] = ("Başarılı Giriş")
        messagebox.showinfo("Başlık", "Başarılı giriş yaptınız.")
    else:
        messagebox.showerror("Hata Başlık", "Hatalı Giriş Yaptınız.")


l1 = Label(text="Kullanıcı Adı", font= "Candara 9 " )
l1.grid(row=0, column=0, pady=5, padx=5)

l2 = Label(text="Şifre", font="Candara 9 ")
l2.grid(row=1, column=0, pady=5, padx=5)


ent1 = Entry(windows,width=25,fg="white", bg="black")
ent1.grid(row=0, column=1, pady=5, padx=5)

ent2 = Entry (windows,textvariable= StringVar(),show="*", fg="white", bg="black", width=25)
ent2.grid(row=1, column=1, pady=5, padx=5)

btn1 = Button(
    windows, 
    text="Giriş", 
    font="Candara 12 bold",
    cursor="hand2",
    activebackground="black",
    activeforeground="red",
    command=console
    )

btn1.place(x=125, y=80)

windows.mainloop()