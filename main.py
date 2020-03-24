from Tkinter import *
import math
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
                    storeObj=display, q=ichar ,variablesText = variables :self.clear(storeObj, variablesText))

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
            x1 = (-self.y + math.sqrt((self.y ** 2) - (4 * (self.x * self.z)))) / (2 * self.x)
            x2 = (-self.y - math.sqrt((self.y ** 2) - (4 * (self.x * self.z)))) / (2 * self.x)
            display.set("X1="+x1 +" x2="+x2)
        except:
            display.set("ERROR")

    def clear(self, resultText, variablesText):
        self.x = 0
        self.y = 0
        self.z = 0
        resultText.set('')
        variablesText.set('X=')

    def onPressNumber(self, number, text):
        variablesText = ''
        if(self.x == None):
            self.x = number
            variablesText = text.get() + self.x + ' Y='
        elif(self.y == None):
            self.y = number
            variablesText = text.get() + self.y + ' Z='
        elif(self.z == None):
            self.z = number
            variablesText = text.get() + self.z

        text.set(variablesText)


if __name__=='__main__':
 app().mainloop()