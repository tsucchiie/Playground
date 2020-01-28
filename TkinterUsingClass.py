from tkinter import * # mengimport modul tkinter

root = Tk() # membuat object dari class tkinter
root.title('Judul Aplikasi') # membuat judul pada GUI

class autorun: # membuat class dengan nama autorun

    # membuat method init/intializer atau dalam bahasa pemrograman lain disebut construct
    # didalamnya terdapat 2 parameter yaitu self dan master
        # [!] parameter self merupakan parameter wajib yang harus ada pada method
        # [!] parameter self diletakan diawal sebelum parameter lain
        # [!] parameter master adalah parameter yang berfungsi menyimpan nilai pada saat object dari class ini di buat
    
    def __init__(self, master):
        
        self.master = master # membuat variable self.master yang isinya adalam parameter master diatas
        
        self.tombol = Button(self.master, text="Klik Saya", command=self.buat).pack() # Membuat button dengan fungsi didalam class

    
    def buat(self): # membuat method buat() yang didalamnya terdapat widget label
       
        self.label = Label(self.master, text="Trigger").pack()  # membuat widget label yang disimpan didalam variable self.label


autorun(root) # mengeksekusi class dalam Tk

