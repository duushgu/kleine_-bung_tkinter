from tkinter import*
import tkinter as tk

td=Tk() 
td.minsize(275,480)
td.title('Viel Spaß')
td['bg']='lightblue'

l_a=Label(td,text='Parameter a')
l_a.place(x=30,y=30)
l_b=Label(td,text='Parameter b')
l_b.place(x=30,y=60)
l_c=Label(td,text='Parameter c')
l_c.place(x=30,y=90)
l_d=Label(td,text='Parameter d')
l_d.place(x=30,y=120)
l_e=Label(td,text='Parameter e')
l_e.place(x=30,y=150)
l_ug=Label(td,text='Untergrenze')
l_ug.place(x=30,y=180)
l_og=Label(td,text='Obergrenze')
l_og.place(x=30,y=210)
l_sw=Label(td,text='Schnittweite')
l_sw.place(x=30,y=240)

e_a=Entry(td)
e_a.place(x=115,y=30)
e_b=Entry(td)
e_b.place(x=115,y=60)
e_c=Entry(td)
e_c.place(x=115,y=90)
e_d=Entry(td)
e_d.place(x=115,y=120)
e_e=Entry(td)
e_e.place(x=115,y=150)
e_ug=Entry(td)
e_ug.place(x=115,y=180)
e_og=Entry(td)
e_og.place(x=115,y=210)
e_sw=Entry(td)
e_sw.place(x=115,y=240)


def einlesen():
    global a,b,c,d,e,ug,og,sw 
    a=e_a.get()
    b=e_b.get()
    c=e_c.get()
    d=e_d.get()
    e=e_e.get()
    ug=e_ug.get()
    og=e_og.get()
    sw=e_sw.get()
    try:
        a=float(a)
        b=float(b)
        c=float(c)
        d=float(d)
        e=float(e)
        ug=float(ug)
        og=float(og)
        sw=float(sw)
        print('Daten gelesen')
        return True
    except:
        print('Eingabe Fehler')
        return False 
    
def berechnen():
    global x,y1,y2
    import math
    x=[]
    y1=[]
    y2=[]
    x_werte=-5
    
    ug=e_ug.get() or -5
    og=e_og.get() or 5
    ug=float(ug)
    og=float(og)
    while ug<=x_werte<=og:
        a=e_a.get() or 0.5
        b=e_b.get() or 1
        c=e_c.get() or 1
        d=e_d.get() or 7
        e=e_e.get() or 6 
        a=float(a) 
        b=float(b)
        c=float(c)
        d=float(d)
        e=float(e)
        sw=e_sw.get() or 0.1
        sw=float(sw)
        x.append(x_werte)
        y1.append(a*((x_werte)**3) + b*((x_werte)**2)+c)
        y2.append((d*x_werte)+e)
        x_werte=x_werte+sw
        print(y1)
        print(y2)
    
def zeichnen():
    import matplotlib.pyplot as plt
    plt.plot(x, y1, ".b", label='y1')
    plt.plot(x, y2, ".", color='#FFA500', label='y2')
    plt.title('Darstellung der Funktionen')
    plt.grid()
    plt.xlabel('x', fontsize=10)
    plt.ylabel('y1, y2', fontsize=10)
    plt.legend()
    plt.show()
    
def speichern():
    filename = r'c:\users\gandu\Übung_050126.txt'
    with open(filename, 'w') as fileobj:
        fileobj.write('x\tf1(x)\tf2(x)\n')
        for i in range(len(x)):
            line = f"{x[i]:.3f}\t{y1[i]:.3f}\t{y2[i]:.3f}\n"
            fileobj.write(line)

    with open(filename, 'r') as fileobj:
        print(fileobj.read())
        print('geschpeichert')
        
def beenden():
    td.destroy()
    
b_einlesen=Button(td,text='einlesen',command=einlesen)
b_einlesen.place(x=30,y=350)
b_berechnen=Button(td,text='berechnen',command=berechnen)
b_berechnen.place(x=115,y=350)
b_grafik=Button(td,text='zeichnen',command=zeichnen)
b_grafik.place(x=30,y=380)
b_export=Button(td,text='speichern',command=speichern)
b_export.place(x=115,y=380)
b_end=Button(td,text='beenden',command=beenden, bg='red')
b_end.place(x=115,y=410)

td.mainloop()