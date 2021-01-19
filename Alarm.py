from tkinter import *
from tkinter.ttk import Combobox
import time
from math import cos,sin,pi
import pygame


class MyApp():
    def __init__(self, root):
        self.size=300
        self.parent=root

        self.frameAlarm=Frame(root)
        self.frameJam = Frame(root)
        self.framePemberitahuan=Frame(root)

        self.alarmHidup = False
        self.teksJam = StringVar()
        self.antrianAlarm = []
        self.hidupMati = BooleanVar(False)
        self.fileMusik = 'Samsung alarm sound with dancing lizard meme.mp3'
        self.teksTombolAtur = StringVar(value='atur')

        self.teksTombol = StringVar(value='set')

        self.buatFrameJam()
        self.buatJarum()
        self.buatTeksAngka()
        self.buatTeks()
        self.update_clock()
        


    def buatTeks(self):
        self.teks = Label(text="Juan Eka Saputra (19.83.0387)", font="agency 12 bold")
        self.teks.pack()
        self.teks = Label(text="Doni Candra Awali (19.83.0369)", font="agency 12 bold")
        self.teks.pack()

        self.teksPemberitahuan = Label(self.framePemberitahuan, text='Tidak ada alarm terpasang.', bg="white")
        self.teksPemberitahuan.grid(row=0, column=0)

        self.tombolAtur= Button(self.framePemberitahuan, textvariable=self.teksTombolAtur, command=self.jendelaPembuatAlarm)
        self.tombolAtur.grid(row=0, column=1)

        self.framePemberitahuan.pack()
        self.buatmerkjam()

    def buatFrameJam(self):
        root.title("Alarm MI-CEK")
        self.w = Canvas(self.frameJam,width=320, height=320, relief= "sunken", border=10)
        self.w.pack()
        self.frameJam.pack()


    def buatJarum(self):
        self.w.create_line(0, 0, 0, 0, fill="red", tags="second", width=3)
        self.w.create_line(0, 0, 0, 0, fill="black", tags="minute", width=6)
        self.w.create_line(0, 0, 0, 0, fill="black", tags="hour", width=6)

    def buatTeksAngka(self):
        Label(self.frameJam, text="XII").place(x=160, y=13)
        Label(self.frameJam, text="XI").place(x=80, y=28)
        Label(self.frameJam, text="X").place(x=31, y=90)
        Label(self.frameJam, text="IX").place(x=15, y=155)
        Label(self.frameJam, text="VIII").place(x=31, y=230)
        Label(self.frameJam, text="VII").place(x=80, y=285)
        Label(self.frameJam, text="VI").place(x=160, y=303)
        Label(self.frameJam, text="V").place(x=240, y=285)
        Label(self.frameJam, text="IV").place(x=291, y=230)
        Label(self.frameJam, text="III").place(x=310, y=155)
        Label(self.frameJam, text="II").place(x=291, y=90)
        Label(self.frameJam, text="I").place(x=240, y=28)
    def buatmerkjam(self):
        Label(text="MI-CEK", font='agency 12 bold').place(x=135, y=250, )
    def update_clock(self):
        s=time.localtime()[5]
        m=time.localtime()[4]
        h=time.localtime()[3]

        self.jam = time.strftime("%H", time.localtime())
        self.menit = str(int(time.strftime("%M", time.localtime()))-1)
        detik = time.strftime("%S", time.localtime())

        cocok = self.jam + ' : ' + self.menit

        if len(self.antrianAlarm):
            self.teksPemberitahuan.config(text="alarm selanjutnya -> "+self.antrianAlarm[0])
            if cocok == self.antrianAlarm[0] and (detik == '00'):
                self.teksTombol.set('stop')
                self.antrianAlarm.pop(0)
                self.alarmHidup = True
                self.teksTombolAtur.set('stop')

                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load(self.fileMusik)
                pygame.mixer.music.play()
        else :
            self.teksPemberitahuan.config(text='Time Is Money bro :p')

        if self.alarmHidup and pygame.mixer.music.get_busy() == False:
            self.perintahSetAlarm()

        degrees = 6*s
        angle = degrees*pi*2/360
        ox = 165
        oy = 165
        x = ox + self.size*sin(angle)*0.45
        y = oy - self.size*cos(angle)*0.45
        self.w.coords("second", (ox,oy,x,y))

        degrees1 = 6*m
        angle1 = degrees1*pi*2/360
        ox1 = 165
        oy1 = 165
        x1 = ox1 + self.size*sin(angle1)*0.4
        y1 = oy1 - self.size*cos(angle1)*0.4
        self.w.coords("minute", (ox1,oy1,x1,y1))

        degrees2 = 30*h
        angle2 = degrees2*pi*2/360
        ox2 = 165
        oy2 = 165
        x2 = ox2 + self.size*sin(angle2)*0.2
        y2 = oy2 - self.size*cos(angle2)*0.2
        self.w.coords("hour",(ox2,oy2,x2,y2))

        self.parent.after(1000, self.update_clock)

    def jendelaPembuatAlarm(self):
        if self.teksTombolAtur.get()=='stop':
            self.perintahSetAlarm()
        else :
            self.windowAlarm = Toplevel(self.parent)
            self.windowAlarm.wm_title("Mengatur alarm")

            self.frameHapus = Frame(self.windowAlarm)
            self.framLayar = Frame(self.windowAlarm)
            self.frameAlarm = Frame(self.windowAlarm)

            self.layarAlarm()
            self.scrollBar()
            self.buatComboBox()
            self.buatTombol()
            self.updateLayar()

    def buatComboBox(self):
        Label(self.frameAlarm, text='Jam : ').grid(row=0,column=0)
        self.alarmJam = StringVar()
        self.comboJam = Combobox(self.frameAlarm, textvariable=self.alarmJam,
                                state='readonly', width=2)
        self.comboJam['values'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15',
                                     '16','17','18','19','20','21','21','22','23')
        self.comboJam.current(0)
        self.comboJam.grid(row=0,column=1)

        Label(self.frameAlarm, text='  Menit : ').grid(row=0,column=2)
        self.alarmMenit = StringVar()
        self.comboMenit = Combobox(self.frameAlarm, textvariable=self.alarmMenit,
                                state='readonly', width=2)
        self.comboMenit['values'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15',
                                     '16','17','18','19','20','21','21','22','23','24','25','26','27','28','29','30',
                                     '31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46',
                                      '47','48','49','50','51','52','53','54','55','56','57','58','59')
        self.comboMenit.current(0)
        self.comboMenit.grid(row=0,column=3)

        self.frameAlarm.pack(pady=3)

    def buatTombol(self):
        self.tombolSet = Button(self.frameAlarm,textvariable=self.teksTombol,command=self.perintahSetAlarm).grid(row=0,column=4)
        self.kolomHapus = Entry(self.frameHapus, width=5)
        self.kolomHapus.grid(row=0,column=0)
        self.tombolSet = Button(self.frameHapus, text='Hapus', command=self.perintahHapus).grid(row=0, column=1)

        self.frameHapus.pack()

    def perintahSetAlarm(self):
        if self.teksTombol.get() == 'set' :
            masukan = self.comboJam.get()+' : '+self.comboMenit.get()
            tidakAda = True
            for i in self.antrianAlarm :
                if i == masukan :
                    tidakAda=False
            if tidakAda :
                self.tentukanUrutan(angka=masukan)
            self.updateLayar()
        else :
            self.teksTombol.set('set')
            self.teksTombolAtur.set('atur')
            self.alarmHidup=False
            try :
                pygame.mixer.music.stop()
            except :
                pass

    def layarAlarm(self):
        self.layar = Text(self.framLayar, height=5, width=35, state=DISABLED)
        self.layar.grid(row=0,column=0)
        self.framLayar.pack()

    def updateLayar(self):
        masukan=''
        for i in range(len(self.antrianAlarm)) :
            masukan += str(i+1)+". "+ self.antrianAlarm[i]+'\n'
        self.layar.config(state=NORMAL)
        self.layar.delete('1.0',END)
        self.layar.insert(END, masukan)
        self.layar.config(state=DISABLED)

    def perintahHapus(self):
        try:
            for i in range(len(self.antrianAlarm)) :
                if int(self.kolomHapus.get())-1 == i :
                    self.antrianAlarm.pop(i)
                    self.updateLayar()
                    break
        except :
            pass

    def tentukanUrutan(self, angka=0):
        if angka != 0 :
            self.antrianAlarm.append(angka)
        jarakJamPositif = []
        jarakJamNegatif = []
        convertInt = []
        antrianBaruPositif = []
        antrianBaruNegatif = []

        for i in self.antrianAlarm :
            angka = ''
            for j in i :
                if j != ':' and j != ' ' :
                    angka += j
            convertInt.append(angka)
            jarak = int(self.jam + self.menit) - int(angka)
            jarak *= -1

            if jarak <= 0:
                jarakJamPositif.append(jarak)
            elif jarak > 0 :
                jarakJamNegatif.append(jarak)

        jarakJamPositif.sort()
        jarakJamNegatif.sort()

        for i in jarakJamPositif :
            for j in range(len(convertInt)) :
                jarak = int(self.jam + self.menit) - int(convertInt[j])
                jarak *= -1
                if i == jarak :
                    antrianBaruPositif.append(self.antrianAlarm[j])

        for i in jarakJamNegatif :
            for j in range(len(convertInt)) :
                jarak = int(self.jam + self.menit) - int(convertInt[j])
                jarak *= -1
                if i == jarak :
                    antrianBaruNegatif.append(self.antrianAlarm[j])

        self.antrianAlarm = antrianBaruNegatif+antrianBaruPositif

    def scrollBar(self):
        scroll = Scrollbar(self.framLayar)
        scroll.grid(row=0,column=1, sticky=N+S)
        scroll.config(command=self.layar.yview)
        self.layar.config(yscrollcommand=scroll.set)

root = Tk()
app = MyApp(root)
mainloop()
