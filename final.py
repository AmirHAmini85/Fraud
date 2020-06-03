#Amir.H.Amini
# code haye choose part
#Amir.H.Amini
#Copy Right 2020 Amir.H.Amini
#Amir.H.Amini
# code haye choose part
#Amir.H.Amini
b=0
m=0
while m==0:
    print('5 barabare ba hajm')
    print('2 barabare ba b.mm & k.m.m')
    print('3 halat & ehtemal')
    print('4 adad sahih')
    print('1 mashin hesab')
    print('6 amal gar')
    print('7 jame')
    print('8 hendese dig')
    print('9 jazr moraba & mokab va ...')
    print('10 bordar')
    ch=int(input('kodom?'))
    if ch==1:
        b='mashin hesab'
        print(b)
        c=int(input('yes=1 no=2'))
        if c==1:
            m=1
        else:
            m=0       
    elif ch==2:
        b='b.mm & k.mm'
        print(b)
        c=int(input('yes=1 no=2'))
        if c==1:
            m=1
        else:
            m=0        
    elif ch==3:
        b='halat & ehtemal'
        print(b)
        c=int(input('yes=1 no=2'))
        if c==1:
            m=1
        else:
            m=0  
    elif ch==4:
        b='adad sahih'
        print(b)
        c=int(input('yes=1 no=2'))
        if c==1:
            m=1
        else:
            m=0    
    elif ch==5:
        b='mashin hesab'
        print(b)
        c=int(input('yes=1 no=2'))
        if c==1:
            m=1
        else:
            m=0     
    elif ch==6:
        b='amal gar'
        print(b)
        c=int(input('yes=1 no=2'))
        if c==1:
            m=1
        else:
            m=0     
    elif ch==7:
        b='jame'
        print(b)
        c=int(input('yes=1 no=2'))
        if c==1:
            m=1
        else:
            m=0   
    elif ch==8:
        b='hendese dig'
        print(b)
        c=int(input('yes=1 no=2'))
        if c==1:
            m=1
        else:
            m=0      
    elif ch==9:
        b='jazr moraba & mokab va ...'
        print(b)
        c=int(input('yes=1 no=2'))
        if c==1:
            m=1
        else:
            m=0     
    elif ch==10:
        b='bordar'
        print(b)
        c=int(input('yes=1 no=2'))
        if c==1:
            m=1
        else:
            m=0
    else:
        print('what? asan nadarim baba')
print(b)
#Amir.H.Amini
# list haye har part
#Amir.H.Amini
#Copy Right 2020 Amir.H.Amini
#Amir.H.Amini
# list haye har part
#Amir.H.Amini
hajm=['0 = mokab','1 = makrot','2 = ostovane','3 = manshor ','4 = heram']
bmmkmm=['0 = b.m.m','1 = k.m.m']
halatehtemal=['0 = tas','1 = darsad']
adadsahih=['0 = garine ','1 = ','3 = ','4 = ','5 = ']
mashinhesab=['0 = ','1 = ','3 = ','4 = ','5 = ']
amalgar=['0 = ','1 = ','3 = ','4 = ','5 = ']
jame=['0 = ','1 = ','3 = ','4 = ','5 = ']
hendesedig=['0 = ','1 = ','3 = ','4 = ','5 = ']
jazrmorabamokab=['0 = ','1 = ','3 = ','4 = ','5 = ']
bordar=['0 = ','1 = ','3 = ','4 = ','5 = ']
if b=='hajm' :
    print(hajm)
    q=int(input('kodom?'))
    print(hajm[q])
elif b=='b.mm & k.mm' :
    print(bmmkmm)
    q=int(input('kodom?'))
elif b=='halat & ehtemal' :
    print(halatehtemal)
    q=int(input('kodom?'))
#Amir.H.Amini
# mashin hesab
#Amir.H.Amini
#Copy Right 2020 Amir.H.Amini
#Amir.H.Amini
# mashin hesab
#Amir.H.Amini
elif b=='mashin hesab':
    from tkinter import*

    def fCalc(src, side):
        appObj = Frame(src, borderwidth=4, bd=2,bg = "#cccccc")
        appObj.pack(side=side, expand=YES, fill=BOTH)
        return appObj

    def button(src, side, text, command=None):
        appObj = Button(src, text=text, command=command)
        appObj.pack(side=side, expand=YES, fill=BOTH)
        return appObj

    class app(Frame):
        def __init__(self, root = Tk(), width=364, height=425):
            Frame.__init__(self)
            self.option_add("*Font", 'arial 20 bold')
            self.pack(expand=YES, fill=BOTH)
            self.master.title("Simple Calculator")
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            root.geometry('%dx%d+%d+%d' % (width, height, x, y))
            display = StringVar()
            Entry(self, relief= RIDGE,      
                        textvariable=display, state=DISABLED, justify='right', bd=20, bg="silver").pack(side=TOP, expand=YES,
                                fill=BOTH)
            clrChar = "Clear"
            button(self, TOP, clrChar, lambda appObj=display, i=clrChar: appObj.set(''))


            for btnNum in ("789/", "456*", "123-", "0.+"):

                FunctionNum = fCalc(self, TOP)
                for fEquals in btnNum:
                    button(FunctionNum, LEFT, fEquals,
                            lambda appObj=display, i=fEquals: appObj.set(appObj.get() + i))
                    EqualsButton = fCalc(self, TOP)
                    
            for fEquals in "=":
                if fEquals == "=":
                    btnEquals = button(EqualsButton, LEFT, fEquals)
                    btnEquals.bind('<ButtonRelease-1>',
                                    lambda e, s=self, appObj=display: s.result(appObj), "+")
                else:
                    btnEquals = button(EqualsButton, LEFT, fEquals,
                            lambda appObj=display, s=" %s "%fEquals: appObj.set(appObj.get()+s))

        def result(self, display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("UNDEFINED")

    if __name__ == '__main__':
        app().mainloop()
    
    
