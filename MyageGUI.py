from datetime import date
import Tkinter

import tkMessageBox

def submit():

   try:

     a=int(t1.get())

     b=int(t2.get())

     c=int(t3.get())

     t6.insert(0,str(date.today()))

     t6.delete(Tkinter.END)

     birthday=date(a,b,c)

     age=date.today()-birthday

     t4.insert(0,str(age.days))

     t4.delete(Tkinter.END)

     years=age.days/364

     t5.insert(0,str(years))

     t5.delete(Tkinter.END)

   

   except:

     tkMessageBox.showinfo("ERROR","INVALID ENTRY") 

    



root=Tkinter.Tk()

root.title('AGE')

label=Tkinter.Label(root,text='AGE CALCULATOR',font=("heletica",20))

label.place(x=300,y=50,width=300,height=20)





label1=Tkinter.Label(root,text='ENTER YEAR OF BIRTH  :',font=("heletica",10))

label1.place(x=100,y=100,width=300,height=35)



t1=Tkinter.Entry(root)

t1.place(x=350,y=100,width=100,height=25)



label2=Tkinter.Label(root,text='ENTER MONTH OF BIRTH(IN NUMBERS)  :',font=("heletica",10))

label2.place(x=55,y=150,width=300,height=45)



t2=Tkinter.Entry(root)

t2.place(x=350,y=150,width=100,height=25)





label3=Tkinter.Label(root,text='ENTER DATE OF BIRTH  :',font=("heletica",10))

label3.place(x=100,y=200,width=300,height=55)



t3=Tkinter.Entry(root)

t3.place(x=350,y=200,width=100,height=25)



label4=Tkinter.Label(root,text='YOUR AGE IN DAYS :',font=("heletica",10))

label4.place(x=35,y=250,width=300,height=65)



t4=Tkinter.Entry(root)

t4.place(x=250,y=265,width=100,height=25)



label5=Tkinter.Label(root,text='YOUR AGE IN YEARS  :',font=("heletica",10))

label5.place(x=325,y=250,width=300,height=65)



t5=Tkinter.Entry(root)

t5.place(x=550,y=265,width=100,height=25)



label6=Tkinter.Label(root,text='TODAY\'\S DATE:',font=("heletica",10))

label6.place(x=75,y=300,width=300,height=65)



t6=Tkinter.Entry(root)

t6.place(x=285,y=320,width=100,height=25)





b1=Tkinter.Button(root,text='SUBMIT',command=submit)

b1.place(x=500,y=200,width=100,height=20)

b2=Tkinter.Button(root,text='CLOSE',command=exit)
b2.place(x=500,y=500,width=100,height=20)

root.mainloop()
