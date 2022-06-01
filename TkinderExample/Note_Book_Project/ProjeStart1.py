
from tkinter import *
import tkinter as tk

windows = tk.Tk()
windows.title("Note Book | 1")
windows.geometry("700x250")
windows.resizable(width=False, height=False)
#////////////////////////////////////////////////////////

def retrievedata1 ():
        global list_data
        list_data=[]
        try:
            with open("EnglishWords.txt", "r", encoding="utf-8") as file:
             for f in file:
                listbox1.insert(tk.END, f.strip())
                list_data.append(f.strip())
                print(list_data)
        except:
            pass

def retrievedata2 ():
        global list_data
        list_data1=[]
        try:
            with open("TurkishMeans.txt", "r", encoding="utf-8") as file:
             for fl in file:
                listbox1.insert(tk.END, fl.strip())
                list_data1.append(fl.strip())
                print(list_data1)
        except:
            pass



        
                    


#*****LABELS*****
#-ENTRY LABELS-
lbl_entry1 = Label(text="English Word: ")
lbl_entry1.place(x=20 , y=10)
lbl_entry2 = Label(text="Turkish Mean: ")
lbl_entry2.place(x=20 , y=40 )

#-LİSTBOX LABELS-
lbl_listbox1 = Label(text="English Words")
lbl_listbox1.place(x=375 , y= 10)
lbl_listbox2 = Label(text="Turkish Means")
lbl_listbox2.place(x= 550 , y=10 )

#////////////////////////////////////////////////////////

#*****ENTRYS*****
entry1 = Entry(windows,textvariable=StringVar(), width=30,bg="black",fg="white")
entry1.place(x= 110 , y= 10)

entry2 = Entry(windows, textvariable=StringVar(), width=30,)
entry2.place(x= 110 , y= 40)

#////////////////////////////////////////////////////////

#*****LİSTBOXS*****
listbox1 = Listbox(windows)
listbox1.place(x= 350 , y= 40 )

listbox2 = Listbox(windows)
listbox2.place(x= 530 , y= 40 )

#*****BUTTONS*****
btn_save = Button(windows, text="Save",width=20)
btn_save.place(x= 120 , y= 80 )

btn_delete = Button(windows, text="Delete",width=20)
btn_delete.place(x= 120 , y= 120 )

btn_saveDelete = Button(windows, text="Quit", width=15)
btn_saveDelete.place(x= 135 , y= 160 )


windows.mainloop()