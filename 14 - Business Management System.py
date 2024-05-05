import tkinter as tk
from tkinter import ttk
from ttkthemes import *
from tkmacosx import *
import json
import time

root = tk.Tk()
root.geometry('450x650')
root.title('IBIS VIP')
style = ThemedStyle(root)
style.theme_use('scidpink')

projeler = ['PROJE SEÇİNİZ','IBIS FOR ERA']
departmanlar = ['DEPARTMAN SEÇİNİZ','Mobil Yazılımlar Ar-Ge','Bulut Yazılımlar Ar-Ge','Pazarlama']
def arama():
    if secilen_proje.get()==projeler[1]:
        with open("calisanlar_listesi.json", "r", encoding="utf-8") as dosya:
            datalar = json.load(dosya)
        kisiler_listesi = tk.Listbox(root,background="#E6D3DA")
        kisiler_listesi.place(x=70, y=220,width=310, height=300)
        
        for ix in datalar['calisanlar']:
            if secilen_departman.get() == departmanlar[1]:
                if ix['departman'] == departmanlar[1]:
                   kisiler_listesi.insert(tk.END, ix['ad'] + " " + ix['soyad']+ "   /        "+ ix['dogum_tarihi']+ "   /      "+ secilen_proje.get())
            elif secilen_departman.get() == departmanlar[2]:
                if ix['departman'] == departmanlar[2]:
                   kisiler_listesi.insert(tk.END, ix['ad'] + " " + ix['soyad']+ "   /    "+ ix['dogum_tarihi']+ "   /   "+ secilen_proje.get())
            elif secilen_departman.get() == departmanlar[3]:
                if ix['departman'] == departmanlar[3]:
                   kisiler_listesi.insert(tk.END, ix['ad'] + " " + ix['soyad']+ "   /    "+ ix['dogum_tarihi']+ "   /   "+ secilen_proje.get())

    elif secilen_proje.get() != projeler[1]:
        with open("calisanlar_listesi.json", "r", encoding="utf-8") as dosya:
            datalar = json.load(dosya)
        kisiler_listesi = tk.Listbox(root)
        kisiler_listesi.place(x=70, y=220,width=310, height=300)
        
        for ix in datalar['calisanlar']:    
            if secilen_departman.get() == departmanlar[-1]:
                if ix['departman'] == departmanlar[-1]:
                   kisiler_listesi.insert(tk.END, ix['ad'] + " " + ix['soyad']+ "   /    "+ ix['dogum_tarihi']+ "   /   "+ projeler[-1])

    elif not departmanlar[-1]:
        print("hata")
    elif secilen_proje.get()==projeler[0]:
        print("hata")
    else:
        print("KULLANICI HATASI")

def proje_ekle():
    alan='\n'*43
    alan_kapla=ttk.Label(root,background='#4D40A1',text=alan,width=75,relief='raised')
    alan_kapla.place(x=0,y=0)

    proje_ekle_yazi=ttk.Label(root,text='PROJE EKLE',background="#4D40A1",foreground="#E6D3DA",font=('Verdana',20))
    proje_ekle_yazi.place(x=135,y=50)
    
    proje_adi_yazi=ttk.Label(root,text='Proje Adı',background="#4D40A1",foreground="#E6D3DA",font=('Verdana',12))
    proje_adi_yazi.place(x=50,y=170)
    departman_adi_yazi=ttk.Label(root,text='Departman Adı',background="#4D40A1",foreground="#E6D3DA",font=('Verdana',12))
    departman_adi_yazi.place(x=50,y=300)
    gorev_yazi=ttk.Label(root,text='Görev Açıklaması',background="#4D40A1",foreground="#E6D3DA",font=('Verdana',12))
    gorev_yazi.place(x=50,y=430)
    
    global proje_adi
    global departman_adi
    global gorev_adi
    proje_adi=ttk.Entry(root,background="#4D40A1",font=('Verdana',12),foreground="#4D40A1")
    proje_adi.place(x=50,y=200)
    departman_adi=ttk.Entry(root,background="#4D40A1",font=('Verdana',12),foreground="#4D40A1")
    departman_adi.place(x=50,y=330)
    gorev_adi=tk.Text(root,background="#E6D3DA",font=('Verdana',12),foreground="#4D40A1")
    gorev_adi.place(x=50,y=460,width=330,height=100)

    ekle_buton=ttk.Button(root,text=' EKLE ',width=20,command=proje_ekle_fonk)
    ekle_buton.place(x=50,y=600)

def proje_ekle_fonk():
    if proje_adi.get() and departman_adi.get():
        projeler.append(proje_adi.get())
        departmanlar.append(departman_adi.get())
        
        time.sleep(0.5)
        ana_menu()
        proje_ekle_buton.config(state='disabled')
    else: 
        print('KULLANICI HATASI: eksik var')

def kisi_ekle():
    alan='\n'*43
    alan_kapla=ttk.Label(root,background='#4D40A1',text=alan,width=75,relief='raised')
    alan_kapla.place(x=0,y=0)

    proje_ekle_yazi=ttk.Label(root,text='KİŞİ EKLE',background="#4D40A1",foreground="#E6D3DA",font=('Verdana',20))
    proje_ekle_yazi.place(x=135,y=50)
    
    d_tarihi_yazi=ttk.Label(root,text='Doğum Tarihi(YIL-AY-GUN)',background="#4D40A1",foreground="#E6D3DA",font=('Verdana',12))
    d_tarihi_yazi.place(x=50,y=170)
    departman_adi_yazi=ttk.Label(root,text='Departman Adı',background="#4D40A1",foreground="#E6D3DA",font=('Verdana',12))
    departman_adi_yazi.place(x=50,y=300)
    proje_adi_yazi=ttk.Label(root,text='Proje Adı',background="#4D40A1",foreground="#E6D3DA",font=('Verdana',12))
    proje_adi_yazi.place(x=250,y=300)
    ad_yazi=ttk.Label(root,text='Adı',background="#4D40A1",foreground="#E6D3DA",font=('Verdana',12))
    ad_yazi.place(x=50,y=430)
    soyad_yazi=ttk.Label(root,text='Soyadı',background="#4D40A1",foreground="#E6D3DA",font=('Verdana',12))
    soyad_yazi.place(x=250,y=430)
    
    global proje_adi
    global departman_adi
    global adi
    global soyadi
    global d_tarihi
    d_tarihi=ttk.Entry(root,background="#4D40A1",font=('Verdana',12),foreground="#4D40A1")
    d_tarihi.place(x=50,y=200)
    departman_adi=ttk.Entry(root,background="#4D40A1",font=('Verdana',12),foreground="#4D40A1")
    departman_adi.place(x=50,y=330,width=150)
    proje_adi=ttk.Entry(root,background="#4D40A1",font=('Verdana',12),foreground="#4D40A1")
    proje_adi.place(x=250,y=330,width=150)
    adi=ttk.Entry(root,background="#E6D3DA",font=('Verdana',12),foreground="#4D40A1")
    adi.place(x=50,y=460,width=150)
    soyadi=ttk.Entry(root,background="#E6D3DA",font=('Verdana',12),foreground="#4D40A1")
    soyadi.place(x=250,y=460,width=150)

    ekle_buton=ttk.Button(root,text=' EKLE ',width=20,command=kisi_ekle_fonk)
    ekle_buton.place(x=50,y=600)
def kisi_ekle_fonk():
    if departman_adi.get() in departmanlar and proje_adi.get() in projeler:
        if d_tarihi.get() and departman_adi.get() and proje_adi.get() and adi.get() and soyadi.get():
            with open("calisanlar_listesi.json", "r", encoding="utf-8") as dosya:
                datalar =json.load(dosya)
            datalar['calisanlar'].append({
            "ad": adi.get().title(), "soyad": soyadi.get().title(),"departman": departman_adi.get(),"dogum_tarihi":d_tarihi.get()})

            with open("calisanlar_listesi.json", "w", encoding="utf-8") as dosya:
                json.dump(datalar, dosya, ensure_ascii=False, indent=4)
            
            time.sleep(0.5)

            ana_menu()
            proje_ekle_buton.config(state='disabled')
    else:
        print("hata")
def ana_menu():
    alan='\n'*43
    alan_kapla=ttk.Label(root,background='#4D40A1',text=alan,width=75,relief='raised')
    alan_kapla.place(x=0,y=0)

    proje_yazi=ttk.Label(root,background='#4D40A1',text='PROJE ADI',font=('Verdana',13),foreground='#E6D3DA')
    proje_yazi.place(x=80,y=35)
    departman_yazi=ttk.Label(root,background='#4D40A1',text='DEPARTMAN ADI',font=('Verdana',13),foreground='#E6D3DA')
    departman_yazi.place(x=230,y=35)

    global secilen_proje
    global secilen_departman
    secilen_proje = tk.StringVar()
    proje_secenek = ttk.OptionMenu(root,secilen_proje, projeler[0], *projeler)
    proje_secenek.place(x=80,y=65)

    secilen_departman = tk.StringVar()
    departman_secenek = ttk.OptionMenu(root,secilen_departman, departmanlar[0], *departmanlar)
    departman_secenek.place(x=230,y=65)

    ara_buton=ttk.Button(root,text='    ARA    ',command=arama)
    ara_buton.place(x=170,y=180)

    global proje_ekle_buton
    global kisi_ekle_buton
    proje_ekle_buton=ttk.Button(root,text='    proje ekle    ',command=proje_ekle)
    proje_ekle_buton.place(x=70,y=550)
    kisi_ekle_buton=ttk.Button(root,text='    kişi ekle    ',command=kisi_ekle)
    kisi_ekle_buton.place(x=305,y=550)

# pink #E6D3DA blue #4D40A1





ana_menu()
root.mainloop()