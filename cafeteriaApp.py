from tkinter import *
import random
import time;


root = Tk()
root.geometry("1600x800+0+0")
root.title("MIT Cafeteria")
text_Input=StringVar()
operator=""
Tops=Frame(root,width=1600,height=50,bd=10,bg='powder blue',relief='sunken')
Tops.pack(side=TOP)
#Left Frame
f1=Frame(root,width=800,height=700,bg='white',relief='sunken')
f1.pack(side=LEFT)
#Right Frame
f2=Frame(root,width=300,height=700,bg="powder blue",relief='raise')
f2.pack(side=RIGHT)
#time
localtime=time.asctime(time.localtime(time.time()))
#info
lblInfo=Label(Tops,font=('arial',50,'bold'),text="MIT CAFETERIA",fg="Steel blue",bd= 10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel blue",bd= 10,anchor='w')
lblInfo.grid(row=1,column=0)

# For the Calculator
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")
def btnEqualto():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
def Ref():
    x=random.randint(128930,750840390)
    randomRef= str(x)
    rand.set(randomRef)

    CoCoffee=0
    if  Coffee.get() != "":
        CoCoffee = float(Coffee.get())
    CoMocha = 0
    if Mocha.get() != "":
        CoMocha = float(Mocha.get())
    """CoExpresso=float(Expresso.get())
    CoCappucino=float(Cappucino.get())
    CoIcedTea=float(IcedTea.get())
    CoPizza=float(Pizza.get())
    CoMilkshake=float(Milkshake.get())
    CoFries=float(Fries.get())
    CoBurger=float(Burger.get())"""
    CostofCoffee= CoCoffee*10.0
    CostofMocha=CoMocha*30.0
    """CostofExpresso=CoExpresso*40.0
    CostofIcedTea=CoIcedTea*40.0
    CostofPizza=CoPizza*50.0
    CostofMilkshake=CoMilkshake*20.0
    CostofFries=CoFries*70.0
    CostofBurger=CoBurger*80.0"""


    Cost= str('%.2f' % (CostofCoffee+CostofMocha))
    GST_=((CostofCoffee+CostofMocha)*0.2)
    Service_Tax=((CostofCoffee+CostofMocha)/99)
    GST=str('%.2f'% GST_)
    Service_Tax="Rs.", str('%2.f' % Service_Tax)
    Cost_=(CostofCoffee+CostofMocha)
    OverAll= str('%.2f' % (Cost_))

    ServiceTax.set(Service_Tax)
    Cost.set(Cost_)
    Tax.set(GST)
    Total.set(OverAll)




def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Coffee.set("")
    Mocha.set("")
    """Expresso.set("")

    Cappucino.set("")
    IcedTea.set("")
    Pizza.set("")
    Milkshake.set("")
    Fries.set("")"""

    Cost.set("")
    GST.set("")
    ServiceTax.set("")
    TotalCost.set("")


txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",justify='right')

txtDisplay.grid(columnspan=4)
btn7=Button(f2,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text='7',bg="powder blue",command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text='8',bg="powder blue",command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text='9',bg="powder blue",command=lambda:btnClick(9)).grid(row=2,column=2)
Addition=Button(f2,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text='+',bg="powder blue",command=lambda:btnClick('+')).grid(row=2,column=3)
btn4=Button(f2,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text='4',bg="powder blue",command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text='5',bg="powder blue",command=lambda:btnClick(5)).grid(row=3,column=1)
btn6 =Button(f2,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text='6',bg="powder blue",command=lambda:btnClick(6)).grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text='-',bg="powder blue",command=lambda:btnClick('-')).grid(row=3,column=3)
btn3=Button(f2,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text='3',bg="powder blue",command=lambda:btnClick(3)).grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text='2',bg="powder blue",command=lambda:btnClick(2)).grid(row=4,column=1)
btn1=Button(f2,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text='1',bg="powder blue",command=lambda:btnClick(1)).grid(row=4,column=2)
Multiply=Button(f2,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text='*',bg="powder blue",command=lambda:btnClick('*')).grid(row=4,column=3)
btn0=Button(f2,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text='0',bg="powder blue",command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text='CLR',bg="powder blue",command=lambda: btnClearDisplay()).grid(row=5,column=1)
btnEquals=Button(f2,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text='=',bg="powder blue",command=btnEqualto).grid(row=5,column=2)
Division=Button(f2,padx=16,pady=16,fg="black",font=('arial',20,'bold'),text='/',bg="powder blue",command=lambda:btnClick("/")).grid(row=5,column=3)
#.........................................................................................................................................................................................................
rand=StringVar()
Coffee=StringVar()
Mocha=StringVar()
"""Expresso=StringVar()
Drinks=StringVar()
Cappucino=StringVar()
IcedTea=StringVar()
Burger=StringVar()
Pizza=StringVar()
Milkshake=StringVar()
Fries=StringVar()"""
Cost=StringVar()
GST=StringVar()
ServiceTax=StringVar()
TotalCost=StringVar()

lblItems=Label(f1,font=('arial',16,'bold'),text="Items",bd=16,anchor='w')
lblItems.grid(row=0,column=0)
txtItems=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg='powder blue',justify="right")
txtItems.grid(row=0,column=1)

lblCoffee=Label(f1,font=('arial',16,'bold'),text="Coffee",bd=16,anchor='w')
lblCoffee.grid(row=1,column=0)
txtCoffee=Entry(f1,font=('arial',16,'bold'),textvariable=Coffee,bd=10,insertwidth=4,bg='powder blue',justify="right")
txtCoffee.grid(row=1,column=1)

lblMocha=Label(f1,font=('arial',16,'bold'),text="Mocha",bd=16,anchor='w')
lblMocha.grid(row=2,column=0)
txtMocha=Entry(f1,font=('arial',16,'bold'),textvariable=Mocha,bd=10,insertwidth=4,bg='powder blue',justify="right")
txtMocha.grid(row=2,column=1)


"""lblExpresso=Label(f1,font=('arial',16,'bold'),text="Expresso",bd=16,anchor='w')
lblExpresso.grid(row=3,column=0)
txtExpresso=Entry(f1,font=('arial',16,'bold'),textvariable=Expresso,bd=10,insertwidth=4,bg='powder blue',justify="right")
txtExpresso.grid(row=3,column=1)

lblCappucino=Label(f1,font=('arial',16,'bold'),text="Cappucino",bd=16,anchor='w')
lblCappucino.grid(row=4,column=0)
txtCappucino=Entry(f1,font=('arial',16,'bold'),textvariable=Cappucino,bd=10,insertwidth=4,bg='powder blue',justify="right")
txtCappucino.grid(row=4,column=1)

lblIcedTea=Label(f1,font=('arial',16,'bold'),text="Iced Tea",bd=16,anchor='w')
lblIcedTea.grid(row=5,column=0)
txtIcedTea=Entry(f1,font=('arial',16,'bold'),textvariable=IcedTea,bd=10,insertwidth=4,bg='powder blue',justify="right")
txtIcedTea.grid(row=5,column=1)

lblBurger=Label(f1,font=('arial',16,'bold'),text="Burger",bd=16,anchor='w')
lblBurger.grid(row=6,column=0)
txtBurger=Entry(f1,font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg='powder blue',justify="right")
txtBurger.grid(row=6,column=1)

lblPizza=Label(f1,font=('arial',16,'bold'),text="Pizza",bd=16,anchor='w')
lblPizza.grid(row=7,column=0)
txtPizza=Entry(f1,font=('arial',16,'bold'),textvariable=Pizza,bd=10,insertwidth=4,bg='powder blue',justify="right")
txtPizza.grid(row=7,column=1)

lblMilkshake=Label(f1,font=('arial',16,'bold'),text="MilkShake",bd=16,anchor='w')
lblMilkshake.grid(row=8,column=0)
txtMilkshake=Entry(f1,font=('arial',16,'bold'),textvariable=Milkshake,bd=10,insertwidth=4,bg='powder blue',justify="right")
txtMilkshake.grid(row=8,column=1)

lblFries=Label(f1,font=('arial',16,'bold'),text="Fries",bd=16,anchor='w')
lblFries.grid(row=9,column=0)
txtFries=Entry(f1,font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg='powder blue',justify="right")
txtFries.grid(row=9,column=1)"""

#Buttons




#Cafe info........................................................................................................................................................................................
lblCost=Label(f1,font=('arial',16,'bold'),text="Cost",bd=16,anchor='w')
lblCost.grid(row=1,column=2)
txtCost=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg='powder blue',justify="right")
txtCost.grid(row=1,column=3)

lblGST=Label(f1,font=('arial',16,'bold'),text="GST",bd=16,anchor='w')
lblGST.grid(row=2,column=2)
txtGST=Entry(f1,font=('arial',16,'bold'),textvariable=GST,bd=10,insertwidth=4,bg='powder blue',justify="right")
txtGST.grid(row=2,column=3)

lblServiceTax=Label(f1,font=('arial',16,'bold'),text="Service Tax",bd=16,anchor='w')
lblServiceTax.grid(row=3,column=2)
txtServiceTax=Entry(f1,font=('arial',16,'bold'),textvariable=ServiceTax,bd=10,insertwidth=4,bg='powder blue',justify="right")
txtServiceTax.grid(row=3,column=3)

lblTotalCost=Label(f1,font=('arial',16,'bold'),text="Total Cost",bd=16,anchor='w')
lblTotalCost.grid(row=4,column=2)
txtTotalCost=Entry(f1,font=('arial',16,'bold'),textvariable=ServiceTax,bd=10,insertwidth=4,bg='powder blue',justify="right")
txtTotalCost.grid(row=4,column=3)
#Buttons.....................................................................................................................................................................................................................
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=4)
btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=3)
btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=2)


































































root.mainloop()
