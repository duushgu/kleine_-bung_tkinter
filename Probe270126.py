from tkinter import*
import math, random
import matplotlib.pyplot as plt

#Formular
gui=Tk()
gui.minsize(230,385)
gui.configure(bg='lightblue')
gui.title('Spielplatz')

#Label
Label(gui, width=10, text='Parameter a:').place(x=30,y=120)
Label(gui, width=10,text='Parameter b:').place(x=30,y=150)
Label(gui, width=10,text='Schrittweite:').place(x=30,y=180)
Label(gui,width=10, text='Punktzahl:').place(x=30,y=210)
hi=Label(gui, text='Viel Spaß!',width=23)
funk=Label(gui, text='f(x)=20*a*sin(x+10)+b*x**3',width=23)

#Label place
hi.place(x=30,y=30)
funk.place(x=30,y=60)

#Entry
e_a=Entry(gui, width=12)
e_b=Entry(gui, width=12)
e_sw=Entry(gui, width=12)
e_p=Entry(gui, width=12)

#Startwerte
e_a.insert(0,1)
e_b.insert(0,1)
e_sw.insert(0,0.01)
e_p.insert(0,10000)

#Entry Place
e_a.place(x=120,y=120)
e_b.place(x=120,y=150)
e_sw.place(x=120,y=180)
e_p.place(x=120,y=210)

#Funktionen
def prüfen():
    global a,b,sw,p
    try:
        a=float(e_a.get())
        b=float(e_b.get())
        sw=float(e_sw.get())
        p=int(e_p.get())
        print('Eingabe gelesen')
        hi.config(text='Kein Problem!')
        b2['state']=NORMAL
        return True
    except:
        hi.config(text='Prüfen Sie noch Eingabe')
        print('Eingabe Fehler')
        return False 

#Auswertung
def funktion():
    global x,y,ns,ext_x,ext_y
    
    #Funktion
    i=-3
    x=[]
    y=[]
    while i<=3:
        x.append(i)
        y.append(a*20*math.sin(i+10)+b*i**3)
        i+=sw
    
    #Nullstellen
    ns=[]
    for n in range(len(y)-1):
        if y[n]==0 or y[n]*y[n+1]<0:
            x0=x[n]-y[n]*(x[n+1]-x[n])/(y[n+1]-y[n])
            ns.append(x0)
            
    #Extrempunkte
    dy = [(y[i+1]-y[i])/sw for i in range(len(y)-1)]
    ext_y=[]
    ext_x=[]
    extrema=[]
    for i in range(len(dy)-1):
        if dy[i]*dy[i+1]<0:
          x0=x[i]-dy[i]*sw/(dy[i+1]-dy[i])
          y0=a*20*math.sin(x0+10)+b*x0**3
          ext_x.append(x0)
          ext_y.append(y0)
          extrema.append((x0,y0))
        
    hi.config(text='Diskrete Werte sind bereit!')
    print('Nullstellen: ', ns)
    print('y Werte der Extrema: ',extrema)
    
    b3['state']=NORMAL
    b4['state']=NORMAL
    b5['state']=NORMAL

#Graph
def diagramm():
    plt.plot(x,y,label='Funktion')
    
    #Nullstelen
    plt.scatter(ns, [0]*len(ns),color='red',label='Nullstellen')
    
    #Extremstellen
    plt.scatter(ext_x,ext_y,color='orange',label='Extrema')
    
    #Achsen(vertical und horizontal)
    plt.axhline(0,color='green')
    plt.axvline(0,color='green')
    
    plt.title("Graphische Darstellung")
    plt.xlabel("x-Werte")
    plt.ylabel("y-Werte")
    plt.grid()
    plt.legend()
    plt.show()
    hi.config(text='Schauen Sie den Graph.')
    print('gezeichnet')

#Fläche berechnen
def fläche():
    global a,b,p,y,x,ns
    
    #Grenze
    xmax=max(ns)
    xmin=min(ns)
    ymax=max(y)
    ymin=min(y)
    
    #Bezugsfläche
    b_fl=(xmax-xmin)*(ymax-ymin)
    print('Bezugsfläche',b_fl)
    
    p_in=0
    for k in range(p):
        rx=random.uniform(xmin,xmax)
        ry=random.uniform(ymin,ymax)
        f=a*20*math.sin(rx+10)+b*rx**3
        if (ry>0 and ry<f) or (ry<0 and ry>f):
            p_in+=1
    erg=b_fl*(p_in/p)
    print('Fläche: ',erg)
    hi.config(text='Fläche: '+str(round(erg,2)))
    
#Daten Externe
def export():
    f=open('Übung_230226.txt','w')
    f.write('x-Werte ; y-Werte'+'\n')
    for l in range(len(x)):
        f.write(str(round(x[l],3)) + ' ; ' + str(round(y[l],3)) + '\n')
    f.close()
    print('exportiert')
    hi.config(text='Datei gespeichert!')

#Ende
def schließen():
    gui.destroy()

#Button
Button(gui,text='Starten',command=prüfen, width=10).place(x=30,y=270) #Es ist in aktiv Button
b2=Button(gui,text='Berechnen',command=funktion,width=10,state='disabled')
b3=Button(gui,text='Zeichnen',command=diagramm,width=10,state='disabled')
b4=Button(gui,text='Fläche',command=fläche,width=10,state='disabled')
b5=Button(gui,text='Export',command=export,width=10,state='disabled')
Button(gui,text='Beenden',command=schließen,width=10, bg='red').place(x=120,y=330)

#Button place
b2.place(x=120,y=270)
b3.place(x=30,y=300)
b4.place(x=120,y=300)
b5.place(x=30,y=330)

gui.mainloop()