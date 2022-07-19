from tkinter import*
root = Tk()
root.geometry('500x500')#creating a window for ui
root.title("BOOKS")
#adding labels to ui
label_0 = Label(root, text="SEARCH BOOKS",width=20,font=("bold", 20))
label_0.place(x=90,y=53)
label_1 = Label(root, text="ENTER BOOK NAME",width=20,font=("bold", 10))
label_1.place(x=80,y=130)
label_2 = Label(root, text="BOOK STATUS: ",width=20,font=("bold", 10))
label_2.place(x=80,y=250)
#books available dict in library
books_available = {
    "ALL INDIA REPORTER 1981,G.R":(37,308),
    "ALL INDIA REPORTER 2008 VOL 95 – BOMBAY SECTION":(63,299),
    "SCALE VOL 1 – 1998,G.RAMASWAMY":(107,204),
    "MADRAS LAW JOURNAL VOL 1 1991,R.NARAYANASWAMY":(135,120),
    "CRIMES VOL 4 1998,G.RAMASWAMY":(181,80),
    "CONSUMER PROTECTION REPORTER VOL 1 2013":(210,180),
    "SERVICES LAW REPORTER VOL 65 1990(2)":(254,308),
    "CURRENT CENTRAL LEGISTLATION VOL 38 2012":(280,268),
    "SALES TAX CASES VOL 31 1973":(328,243),
    "VAT SERVICES AND TAX CASES VOL 44 2011":(355,75),
    "ALL INDA TAX TRIBUNAL JUDGEMENTS VOL 92 2005":(398,24),
    "COMPANY LAW JOURNAL VOL 6 SUPP 2004":(426,98)
}
#dropdown menu display
def show():
    label.config( text = books_available[clicked.get()] )
clicked = StringVar()
clicked.set( "PLEASE SELECT A BOOK FROM THE LIST" )#default
lb = OptionMenu( root , clicked , *books_available )#adding books dict to list
lb.place(x=240,y=130)
Button(root, text='SUBMIT',width=20,bg='brown',fg='white',command=show).place(x=180,y=200)
label = Label( root , text = " " )#label to display result
label.place(x=100,y=270)
root.mainloop()
