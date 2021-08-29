from tkinter import *

def click(event):
    '''self.widget.cget("text") gives us the text that is written in the particular button widget
    here text is argument in place of text we can write whatever written there while creating button like padx pady etc...'''
    global cval
    text = event.widget.cget("text")
    if text == "=":
        if cval.get().isdigit():
            value = int(cval.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"

        cval.set(value)
        screen.update()

    elif text == "C":
        cval.set("")
        screen.update()

    else:
        cval.set(cval.get() + text)
        screen.update()


root=Tk()
root.geometry("400x515")
root.maxsize(400,515)
root.minsize(400,515)
root.title("swapan's calculator")

cval=StringVar()
cval.set("")

screen=Entry(root,font="lucida 40 bold",textvar=cval,borderwidth=8,relief=SUNKEN)
screen.pack(padx=7,side=TOP)

f=Frame(root,pady=20)

button=Button(f,text="7",borderwidt=7,font="lucida 30 bold",padx=10)
button.grid(row=0,column=0)
button.bind("<Button-1>",click)

button=Button(f,text="8",borderwidt=7,font="lucida 30 bold",padx=10)
button.grid(row=0,column=2,padx=7)
button.bind("<Button-1>",click)

button=Button(f,text="9",borderwidt=7,font="lucida 30 bold",padx=10)
button.grid(row=0,column=3)
button.bind("<Button-1>",click)

button=Button(f,text="/",borderwidt=7,font="lucida 30 bold",padx=15)
button.grid(row=0,column=4,padx=7)
button.bind("<Button-1>",click)

#
button=Button(f,text="4",borderwidt=7,font="lucida 30 bold",padx=10)
button.grid(row=2,column=0,pady=6)
button.bind("<Button-1>",click)

button=Button(f,text="5",borderwidt=7,font="lucida 30 bold",padx=10)
button.grid(row=2,column=2,padx=7,pady=6)
button.bind("<Button-1>",click)

button=Button(f,text="6",borderwidt=7,font="lucida 30 bold",padx=10)
button.grid(row=2,column=3,pady=6)
button.bind("<Button-1>",click)

button=Button(f,text="*",borderwidt=7,font="lucida 30 bold",padx=12)
button.grid(row=2,column=4,padx=7,pady=6)
button.bind("<Button-1>",click)

#
button=Button(f,text="1",borderwidt=7,font="lucida 30 bold",padx=10)
button.grid(row=3,column=0,pady=6)
button.bind("<Button-1>",click)

button=Button(f,text="2",borderwidt=7,font="lucida 30 bold",padx=10)
button.grid(row=3,column=2,padx=7,pady=6)
button.bind("<Button-1>",click)

button=Button(f,text="3",borderwidt=7,font="lucida 30 bold",padx=10)
button.grid(row=3,column=3,pady=6)
button.bind("<Button-1>",click)

button=Button(f,text="+",borderwidt=7,font="lucida 30 bold",padx=10)
button.grid(row=3,column=4,padx=7,pady=6)
button.bind("<Button-1>",click)

#
button=Button(f,text="C",borderwidt=7,font="lucida 30 bold",padx=10)
button.grid(row=4,column=0,pady=6)
button.bind("<Button-1>",click)

button=Button(f,text="0",borderwidt=7,font="lucida 30 bold",padx=10)
button.grid(row=4,column=2,padx=7,pady=6)
button.bind("<Button-1>",click)

button=Button(f,text="-",borderwidt=7,font="lucida 30 bold",padx=10)
button.grid(row=4,column=3,pady=6)
button.bind("<Button-1>",click)

button=Button(f,text="=",borderwidt=7,font="lucida 30 bold",padx=10)
button.grid(row=4,column=4,padx=7,pady=6)
button.bind("<Button-1>",click)

f.pack()


root.mainloop()