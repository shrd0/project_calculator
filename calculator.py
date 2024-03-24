from tkinter import *
#create buttons
def button(source,side,text,command=None):
    obj=Button(source,text=text,command=command)
    obj.pack(side=side,expand=YES,fill=BOTH)
    return obj

#create the frame
def frame(source, side):
    obj=Frame(source,borderwidth=2,bd=2,bg="yellow")
    obj.pack(side=side,expand=YES,fill=BOTH)
    return obj

#create a class
class Calculator(Frame):

    #add constructor
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font','arial 23 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Mathematical and Statistical Calculator')

        #addding number values display widget
        display=StringVar()
        Entry(self,relief=RIDGE,textvariable=display,justify='right',bd=10,bg="#fff").pack(side=TOP,expand=YES,fill=BOTH)

        #clear button
        for clearbutton in (["d"]):
            clear=frame(self,TOP)
            for ic in clearbutton:
                button(clear,LEFT,"CLEAR",lambda obj=display,q=ic:obj.set(''))

        #1234567890 number and +,-.*./ buttons
        for nButton in ("+123","-456","*789","/.0%"):
            fNum=frame(self,TOP)
            for iE in nButton:
                button(fNum,LEFT,iE,lambda obj=display,q=iE:obj.set(obj.get()+q))

        EqualButton = frame(self,TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualButton, LEFT,iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e,s=self,storeObj=display: s.calc(storeObj), '+')
            else:
                btniEquals=button(EqualButton, LEFT, iEquals,lambda storeObj=display, s=' %s ' % iEquals: storeObj.set(storeObj.get() + s))


    def calc(self,display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("error...... Try Again")

if __name__=='__main__':
    Calculator().mainloop()
