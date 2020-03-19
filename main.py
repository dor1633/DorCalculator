from Tkinter import *

# look at https://www.simplifiedpython.net/python-calculator/

def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand =YES, fill =BOTH)
    return storeObj

def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand = YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        self.x = None
        self.y = None
        self.z = None
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand = YES, fill =BOTH)
        self.master.title('Calculator')

        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display,
          justify='right'
          , bd=30, bg="powder blue").pack(side=TOP,
                                          expand=YES, fill=BOTH)

        variables = StringVar()
        variables.set('x= ')
        Entry(self, relief=RIDGE, textvariable=variables,
              justify='right'
              , bd=30, bg="snow").pack(side=TOP,
                                              expand=YES, fill=BOTH)

        for clearButton in (["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda
                    storeObj=display, q=ichar: storeObj.set(''))

        for numButton in ("123", "456", "789"):
         FunctionNum = iCalc(self, TOP)
         for number in numButton:
             button(FunctionNum, LEFT, number, lambda text=variables, q=number: self.onPressNumber(q, text))

        EqualButton = iCalc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e,s=self,
                                storeObj=display: s.calc(storeObj), '+')


            else:
                btniEquals = button(EqualButton, LEFT, iEquals,
                                    lambda storeObj=display, s=' %s ' % iEquals: storeObj.set
                                    (storeObj.get() + s))

    def calc(self, display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("ERROR")

    def onPressNumber(self, number, text):
        if(self.x == None):
            self.x = number
        print("number", self.x)
        text.set('mdmdm')


if __name__=='__main__':
 app().mainloop()