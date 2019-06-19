from tkinter import*
from sqlforGUI import*

window=Tk()
def addCustomer():
    def ab():
        cref=Customer(None,None,None,None)
        cref.name=e1.get()
        cref.age=e2.get()
        cref.hobby=e3.get()
        cref.aim=e4.get()
        db=DBase()
        db.addCustomer(cref)
        winx=Toplevel(win1)
        mes=Message(winx,text="ADDED SUCCESSFULLY")
        mes.pack()
        bend = Button(winx, text="exit", command=win1.destroy)
        bend.pack()


    win1=Toplevel(window)
    l1=Label(win1,text="Name")
    l1.pack()
    e1=Entry(win1)
    e1.pack()
    l2=Label(win1,text="Age")
    l2.pack()
    e2=Entry(win1)
    e2.pack()
    l3=Label(win1,text="hobby")
    l3.pack()
    e3=Entry(win1)
    e3.pack()
    l4=Label(win1,text="Aim")
    l4.pack()
    e4=Entry(win1)
    e4.pack()
    bf=Button(win1,text="ADD",command=ab)
    bf.pack()


def updateCustomer():
    def ab():
        cref=Customer(None,None,None,None)
        cref.id=e5.get()
        cref.name=e1.get()
        cref.age=e2.get()
        cref.hobby=e3.get()
        cref.aim=e4.get()
        db=DBase()
        db.updatCustomer(cref)
        winx=Toplevel(win2)
        mes=Message(winx,text="UPDATED SUCCESSFULLY")
        mes.pack()
        bend = Button(winx, text="exit", command=win2.destroy)
        bend.pack()


    win2=Toplevel(window)
    l5 = Label(win2, text="Id of the customer to be updated")
    l5.pack()
    e5=Entry(win2)
    e5.pack()
    l1=Label(win2,text="Name")
    l1.pack()
    e1=Entry(win2)
    e1.pack()
    l2=Label(win2,text="Age")
    l2.pack()
    e2=Entry(win2)
    e2.pack()
    l3=Label(win2,text="hobby")
    l3.pack()
    e3=Entry(win2)
    e3.pack()
    l4=Label(win2,text="Aim")
    l4.pack()
    e4=Entry(win2)
    e4.pack()

    bf=Button(win2,text="UPDATE",command=ab)
    bf.pack()


def DeleteCustomer():
    def delete():
        v=e1.get()
        db=DBase()
        db.deleteCustomer(v)
        winx=Toplevel(win3)
        mes=Message(winx,text="deleted SUCCESSFULLY")
        mes.pack()
        bend = Button(winx, text="exit", command=win3.destroy)
        bend.pack()

    win3=Toplevel()
    l1=Label(win3,text="ID to be deleted")
    l1.pack()
    e1=Entry(win3)
    e1.pack()
    b1=Button(win3,text="DELETE",command=delete)
    b1.pack()


def showALL():
    win4=Toplevel(window)
    db=DBase()
    r1=db.showall()
    m=Message(win4,text=r1)
    m.pack()
    bend = Button(window, text="exit", command=win4.destroy)
    bend.pack()

b1=Button(window,text="ADD CUSTOMER",command=addCustomer)
b1.pack()
b2=Button(window,text="UPDATE CUSTOMER",command=updateCustomer)
b2.pack()
b3=Button(window,text="DELETE CUSTOMER",command=DeleteCustomer)
b3.pack()
b4=Button(window,text="SHOW ALL CUSTOMER",command=showALL)
b4.pack()
bend=Button(window,text="exit",command=window.destroy)
bend.pack()


window.mainloop()