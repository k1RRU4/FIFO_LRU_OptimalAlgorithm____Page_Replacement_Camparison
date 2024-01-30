from tkinter import *
import tkinter 
import numpy as np
import random

def gridtab(bloc,pages):
    c=len(pages)
    index=0
    for ligne in range(bloc):
     for colonne in range(c+1):
        if(ligne==0 and colonne==0):
           Button(Mafenetre, text=' ',bg='#7AEEE7', borderwidth=1,width=7).grid(row=ligne, column=colonne)  
        elif(ligne==0 and colonne!=0):
            Button(Mafenetre, text=pages[index],bg='#7AEEE7', borderwidth=1,width=7).grid(row=ligne, column=colonne)
            listmessage.insert(END,' '+str(pages[index])) 
            index += 1
        elif (ligne!=0 and colonne==0):
            Button(Mafenetre, text='Bloc'+str(ligne),bg='#7AEEE7', borderwidth=1,width=7).grid(row=ligne, column=colonne)
        else:
            Button(Mafenetre, text='  ',bg='#FFFFFF', borderwidth=1,width=7).grid(row=ligne, column=colonne)
    

def addmemory(memory,c,cl):
    for ligne in range(size):
            try:
                if(cl>=0 and cl==ligne):
                    Button(Mafenetre, text=memory[ligne],bg='#FFFFFF', borderwidth=1,width=7).grid(row=ligne+1, column=c+1)
                else:   
                    Button(Mafenetre, text=memory[ligne],bg='#FFFFFF', borderwidth=1,width=7).grid(row=ligne+1, column=c+1)
            except:
                Button(Mafenetre, text='  ',bg='#FFFFFF', borderwidth=1,width=7).grid(row=ligne+1, column=c+1)

def FIFO():
    count = 0
    memory = []
    global DP
    DP = 0
    cl=-1
    D=False
    fifoIndex = 0
    c=0   
    for page in pages:
        if memory.count(page) == 0 and count < size:   #la page n'est pas chargée en mémoire et il y a de la place 
            memory.append(page) 
            cl=count
            count += 1 
            DP += 1 
        elif memory.count(page) == 0 and count == size:  #il n ya pas de la place dans la mémoire
            memory[fifoIndex] = page
            cl=fifoIndex
            fifoIndex = (fifoIndex + 1) % size
            DP += 1 
        elif memory.count(page) > 0:    #la page est déjà chargée dans la memoire 
            cl=-1
        addmemory(memory,c,cl)     
        c=c+1
    defaut_de_page = DP
    label_defaut.configure(text=f"Defaut de page = {defaut_de_page}")
    return DP

def lrupage(memory,list):
    max=len(list)
    for MI,i in enumerate(memory):
        index=len(list) - list[::-1].index(i) - 1
        if (index<max):
            max=index
            lruIndex= MI  
    return lruIndex
def LRU():
    count = 0
    memory = []
    global DP
    DP = 0
    c=0
    cl=-1
    for i,page in enumerate(pages):
        if memory.count(page) == 0 and count < size:
            memory.append(page)
            cl=count  
            count += 1 
            DP += 1 
        elif memory.count(page) == 0 and count == size:
            lruIndex=lrupage(memory,pages[:i])
            cl=lruIndex
            memory[lruIndex] =page
            DP += 1
        else :
            cl=-1 
        addmemory(memory,c,cl)     
        c=c+1
    defaut_de_page = DP
    label_defaut.configure(text=f"Defaut de page = {defaut_de_page}")
    return DP


def Optimalpage(memory,list):
    min=0
    for MI,i in enumerate(memory):
        try:
            index=list.index(i)
        except:
            index=len(list)+1
        if (index>min):
            min=index
            OptimalIndex= MI  
    return OptimalIndex
  
def Optimal():
    count = 0
    memory = []
    global DP
    DP = 0
    cl=1
    c=0
    for i,page in enumerate(pages):
        if memory.count(page) == 0 and count < size:
            memory.append(page)
            cl=count  
            count += 1 
            DP += 1 
        elif memory.count(page) == 0 and count == size:
            OptimalIndex=Optimalpage(memory,pages[i+1:])
            cl=OptimalIndex
            memory[OptimalIndex] =page
            DP += 1 
        else:
            cl=-1
        addmemory(memory,c,cl)     
        c=c+1
    defaut_de_page = DP
    label_defaut.configure(text=f"Defaut de page = {defaut_de_page}")
    return DP

 


fenetre = Tk() 
fenetre.title("Pagination")

Mafenetre=Frame(fenetre)
Mafenetre.pack(pady=20)
pages=np.random.randint(0,10,random.randint(10,10))
pages=list(pages)
size = int(4)

commande=Frame(fenetre)
commande.pack()


messageframe=Frame(fenetre)
messageframe.pack()

scroll=Scrollbar(messageframe,orient=VERTICAL)
listmessage=Listbox(messageframe,width=30,height=10,bg='#FFFFFF')
listmessage.pack(pady=20)

fifo=Button(commande,text='FIFO',command=FIFO ,width=10,borderwidth=1)
fifo.config()
fifo.pack()



lru=Button(commande,text='LRU',command=LRU ,width=10,borderwidth=1)
lru.config()
lru.pack()

opt=Button(commande,text="OPTIMAL",command=Optimal ,width=10,borderwidth=1)
opt.config()
opt.pack()

def RST():
    for ligne in range(size):
         for colonne in range(len(pages)):
             Button(Mafenetre, text='  ',bg='#FFFFFF', borderwidth=1,width=7).grid(row=ligne+1, column=colonne+1)
    
rst=Button(commande,text='RESET',command=RST ,width=10)
rst.config()
rst.pack()

label_defaut = tkinter.Label(text="Defaut de page = ")
label_defaut.place(x=450,y=250)

gridtab(size+1,pages)
fenetre.mainloop()              
         

