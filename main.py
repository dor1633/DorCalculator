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
        self.a = 0
        self.b = 0
        self.c = 0
        self.currVariableInEquationIndex = 1
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

        for numButton in ("123", "456", "789"):
         FunctionNum = iCalc(self, TOP)
         for number in numButton:
             button(FunctionNum, LEFT, number, lambda text=variables, q=number: self.onPressNumber(q, text))

        erase = iCalc(self, TOP)
        button(erase, LEFT, 'C', lambda storeObj=display, q='C', variablesText=variables: self.clear(storeObj, variablesText))
        btniEquals = button(erase, LEFT, '=')
        btniEquals.bind('<ButtonRelease-1>', lambda e, variablesText=variables,
                        storeObj=display: self.onPressEqualButton(variablesText))

    def onPressEqualButton(self, variablesText):
        addedText = ''
        if (self.currVariableInEquationIndex < 3):
            if(self.currVariableInEquationIndex == 1):
                addedText = ' Y='
            elif (self.currVariableInEquationIndex == 2):
                addedText = ' Z='
            self.currVariableInEquationIndex += 1
        elif (self.currVariableInEquationIndex == 3):
            print("noder")

        variablesText.set(variablesText.get() + addedText)
        # try:
        #     x1 = (-self.b + math.sqrt((self.b ** 2) - (4 * (self.a * self.c)))) / (2 * self.a)
        #     x2 = (-self.b - math.sqrt((self.b ** 2) - (4 * (self.a * self.c)))) / (2 * self.a)
        #     display.set("X1="+x1 +" X2=" + x2)
        # except:
        #     display.set("ERROR")

    def clear(self, resultText, variablesText):
        self.a = 0
        self.b = 0
        self.c = 0
        resultText.set('')
        variablesText.set('X=')

    def onPressNumber(self, number, text):
        variablesText = ''
        intNumber = int(number)
        if(self.currVariableInEquationIndex == 1):
            self.a = (self.a * 10) + intNumber
            print(self.a)
            print(intNumber)
            variablesText = text.get() + str(number)
        elif(self.currVariableInEquationIndex == 2):
            self.b *= 10 + intNumber
            variablesText = text.get() + str(number)
        elif(self.currVariableInEquationIndex == 3):
            self.c *= 10 + intNumber
            variablesText = text.get() + str(number)

        text.set(variablesText)


if __name__=='__main__':
 app().mainloop()