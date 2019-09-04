from tkinter import*

window=Tk()
canvas=Canvas(window,bg="white",width=500,height=300)
canvas.grid(row=0,column=0,columnspan=4)

id=canvas.create_rectangle(200,100,300,200,fill="red")

def left():
    canvas.move(id,-5,0)
def right():
    canvas.move(id,5,0)
def up():
    canvas.move(id,0,5)
def down():
    canvas.move(id,0,-5)

Button(window,text="<-(left)",command=left).grid(row=1,column=0)
Button(window,text="->(right)",command=right).grid(row=1,column=1)
Button(window,text="^(up)",command=up).grid(row=1,column=2)
Button(window,text="v(down)",command=down).grid(row=1,column=3)

window.mainloop()