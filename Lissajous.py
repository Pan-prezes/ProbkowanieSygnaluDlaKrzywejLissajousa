from tkinter import*
from math import*
from decimal import Decimal
from tkinter import messagebox
import random

window = Tk()
window.geometry('1100x720')

#--------------------------------------------------------------------
#interfejs
#--------------------------------------------------------------------

plot = Canvas(window, height=720, width=720, bg='#d3d3d3')
plot.place(x=0,y=0)

var1=StringVar()
aParameterLabel = Label(window, textvariable=var1)
var1.set("Parametr a: ")
aParameterLabel.place(x=730,y=10)
aParameterEntry = Entry(window)
aParameterEntry.place(x=850,y=10)

var2=StringVar()
bParameterLabel = Label(window, textvariable=var2)
var2.set("Parametr b: ")
bParameterLabel.place(x=730,y=60)
bParameterEntry = Entry(window)
bParameterEntry.place(x=850,y=60)

var3=StringVar()
var33=StringVar()
deltaParameterLabel = Label(window, textvariable=var3)
var3.set("Delta: ")
var33.set(pi/2)
deltaParameterLabel.place(x=730,y=110)
deltaParameterEntry = Entry(window, textvariable=var33)
deltaParameterEntry.place(x=850,y=110)

var34=StringVar()
var334=StringVar()
rotationLabel = Label(window, textvariable=var34)
var34.set("Obrót: ")
var334.set(0.0)
rotationLabel.place(x=990,y=110)
rotationEntry = Entry(window, textvariable=var334, width=5)
rotationEntry.place(x=1040,y=110)


var4=StringVar()
frequencyLabel = Label(window, textvariable=var4)
var4.set("Częstotliwośc: ")
frequencyLabel.place(x=730,y=160)
frequencyEntry = Entry(window)
frequencyEntry.place(x=850,y=160)

var5=StringVar()
samplingLabel = Label(window, textvariable=var5)
var5.set("Próbkowanie: ")
samplingLabel.place(x=730,y=210)
samplingEntry = Entry(window)
samplingEntry.place(x=850,y=210)

var6=StringVar()
timeLabel = Label(window, textvariable=var6)
var6.set("Czas: ")
timeLabel.place(x=730,y=260)
timeEntry = Entry(window)
timeEntry.place(x=850,y=260)

outputText = Text(window)
outputText.width = 379
outputText.height = 400
outputText.place(x=721,y=330)

#====================================================================

#--------------------------------------------------------------------
#wciśnięcie guzika oblicz
#--------------------------------------------------------------------

def computeButtonClicked():
    
    try:
        color = ["red","green","blue","black","navy","orange"]
        paramA = float(Decimal(aParameterEntry.get()))
        paramB = float(Decimal(bParameterEntry.get()))
        delta = float(Decimal(deltaParameterEntry.get()))
        freqency = float(Decimal(frequencyEntry.get()))
        sampling = float(Decimal(samplingEntry.get()))
        time = float(Decimal(timeEntry.get()))
        rotation = float(Decimal(rotationEntry.get()))
        omega = 2.0*pi*freqency
        deltaTime = 1.0/sampling
        interval = 0.0
        rotationInterval = 0.0
        color2 = random.randint(0,5)
        rotationDelta = rotation*0.5*pi/sampling

        while interval <= time:
            outputText.insert(END, str(sin(paramA*omega*interval+delta+rotationInterval)))
            outputText.insert(END, '\t')
            outputText.insert(END, str(sin(paramB*omega*interval)))
            outputText.insert(END, '\n')
            interval = interval + deltaTime
            rotationInterval = rotationInterval + rotationDelta

        i=0.0
        while i < 2*pi:
            plot.create_line(360+340*sin(paramA*omega*i+delta),360+340*sin(paramB*omega*i),360+340*sin(paramA*omega*(i+0.0001)+delta),360+340*sin(paramB*omega*(i+0.0001)),fill=color[color2] ,width=2)
            i = i + 0.0001
    except:
        messagebox.showerror("Błąd!", "Wprowadź poprawne dane!")

#====================================================================

#--------------------------------------------------------------------
#wciśnięcie guzika wyczyść
#--------------------------------------------------------------------

def clearButtonClicked():
    plot.delete(ALL)

#====================================================================

#--------------------------------------------------------------------
#wciśnięcie guzika wyczyść próbki
#--------------------------------------------------------------------

def clearTextButtonClicked():
    outputText.delete("1.0",END)

#====================================================================

computeButton = Button(window, text="Oblicz", width=12, command=computeButtonClicked)
computeButton.place(x=730,y=300)

clearButton = Button(window, text="Wyczyść wykres", width=12, command=clearButtonClicked)
clearButton.place(x=830,y=300)

clearTextButton = Button(window, text="Wyczyść próbki", width=12, command=clearTextButtonClicked)
clearTextButton.place(x=930,y=300)


window.mainloop()