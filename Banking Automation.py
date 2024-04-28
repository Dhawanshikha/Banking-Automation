#!/usr/bin/env python
# coding: utf-8

from tkinter import *
from tkinter.ttk import Combobox
from datetime import datetime
import time
from tkinter import messagebox
import sqlite3
from tkinter.ttk import Style, Treeview, Scrollbar

# Create tables with sqlite database
try:
    conobj = sqlite3.connect(database="Banking.sqlite")
    curobj = conobj.cursor()
    curobj.execute("create table accounts(acn integer primary key autoincrement,name text,pass text, email text,mob text,bal float,type text, opendate text)")
    curobj.execute("create table txns(acn int, amt float,updatebal float,type text, txnsdate text)")
    conobj.commit()
    print("Table Created Successfully")
except Exception as e:
    print("Somthing went be wrong might be table already exist!\n\n",e)
    conobj.close()

win = Tk()
win.state("zoomed")
win.configure(bg='light gray')
win.resizable(width=False,height=False)

title = Label(win,text="Banking Automation",font=('arial',60,'bold','underline'),bg='Light Gray')
title.pack()

title = Label(win,text=f"{datetime.now().date()}",font=('arial',19,'bold'),bg='Light Gray')
title.place(relx=.9,rely=.11)


def mainscreen():
    frm=Frame(win)
    frm.configure(bg='lavender',border=True,borderwidth=5)
    frm.place(relx=0,rely=.15,relheight=.85,relwidth=1)

    def login():
        acn = e_acn.get()
        pwd = e_pas.get()
        if len(acn)==0 or len(pwd)==0:
            messagebox.showerror("Login","Empty Fields are not Allowed!")
        else:
            conobj = sqlite3.connect(database="Banking.sqlite")
            curobj = conobj.cursor()
            curobj.execute("select * from accounts where acn=? and pass=?",(acn,pwd))
            tup = curobj.fetchone()
            if tup==None:
                messagebox.showerror("Login","Invalid Account Number or Password")
            else:
                global uname, uacn
                uacn = tup[0]
                uname = tup[1]
                frm.destroy()
                loginscreen()
        
    def fp():
        frm.destroy()
        fpscreen()

    def new():
        frm.destroy()
        newuserscreen()

    def reset():
        e_acn.delete(0,"end")
        e_pas.delete(0,"end")
        e_acn.focus()
    
    lbl_acn = Label(frm,text='Sign in to Your Account.',font=('arial',16,'bold','underline'),bg='lavender')
    lbl_acn.place(relx=.3,rely=.1)
    
    lbl_acn = Label(frm,text='Account No.',font=('arial',20,'bold'),bg='lavender')
    lbl_acn.place(relx=.3,rely=.2)
    
    e_acn = Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.place(relx=.43,rely=.2)
    e_acn.focus()
    
    lbl_pas = Label(frm,text='Password',font=('arial',20,'bold'),bg='lavender')
    lbl_pas.place(relx=.3,rely=.3)
    
    e_pas = Entry(frm,font=('arial',20,'bold'),bd=5,show="*")
    e_pas.place(relx=.43,rely=.3)
    
    login_btn = Button(frm,command=login,font=('arial',20,'bold'),bd=6,text='Sign in')
    login_btn.place(relx=.44,rely=.4)
    
    reset_btn = Button(frm,font=('arial',20,'bold'),bd=6,text='Reset',command=reset)
    reset_btn.place(relx=.55,rely=.4)
    
    fp_btn = Button(frm,command=fp,font=('arial',20,'bold'),bd=6,text='Forget Password',width=15)
    fp_btn.place(relx=.44,rely=.54)
    
    lbl_acn = Label(frm,text="If You don't have an account?",font=('arial',15,'bold','underline'),bg='lavender')
    lbl_acn.place(relx=.3,rely=.69)
    
    new_btn = Button(frm,font=('arial',20,'bold'),bd=6,text='Create New Account',command=new)
    new_btn.place(relx=.44,rely=.76)

def newuserscreen():
    frm=Frame(win)
    frm.configure(bg='lavender',border=True,borderwidth=5)
    frm.place(relx=0,rely=.15,relheight=.85,relwidth=1)
    
    def back():
        frm.destroy()
        mainscreen()

    def reset():
        e_name.delete(0,"end")
        e_pas.delete(0,"end")
        e_mail.delete(0,"end")
        e_no.delete(0,"end")
        e_name.focus()
    
    def OpenAcnDB():
        name = e_name.get()
        pwd = e_pas.get()
        email = e_mail.get()
        mob = e_no.get()
        ac_type = cb_type.get()
        bal = 0
        opendate = time.ctime()

        conobj = sqlite3.connect(database="Banking.sqlite")
        curobj = conobj.cursor()
        curobj.execute("insert into accounts (name,pass,email,mob,type,bal,opendate) values(?,?,?,?,?,?,?)",(name,pwd,email,mob,ac_type,bal,opendate))
        conobj.commit()
        curobj.close()
        
        curobj = conobj.cursor()
        curobj.execute("select max(acn) from accounts")
        tup = curobj.fetchone()
        conobj.close()
        messagebox.showinfo("Open Account",f"Account Opend with Account number : {tup[0]}")

    new_btn = Button(frm,font=('arial',20,'bold'),bd=5,text='Back',command=back)
    new_btn.place(relx=0,rely=0)
    
    lbl_name = Label(frm,text='Name',font=('arial',20,'bold'),bg='lavender')
    lbl_name.place(relx=.3,rely=.2)
    
    e_name = Entry(frm,font=('arial',20,'bold'),bd=5)
    e_name.place(relx=.43,rely=.2)
    e_name.focus()
    
    lbl_pas = Label(frm,text='Password',font=('arial',20,'bold'),bg='lavender')
    lbl_pas.place(relx=.3,rely=.3)
    
    e_pas = Entry(frm,font=('arial',20,'bold'),bd=5)
    e_pas.place(relx=.43,rely=.3)
    
    lbl_mail = Label(frm,text='Email',font=('arial',20,'bold'),bg='lavender')
    lbl_mail.place(relx=.3,rely=.4)
    
    e_mail = Entry(frm,font=('arial',20,'bold'),bd=5)
    e_mail.place(relx=.43,rely=.4)
    
    lbl_no = Label(frm,text='Phone No.',font=('arial',20,'bold'),bg='lavender')
    lbl_no.place(relx=.3,rely=.5)
    
    e_no = Entry(frm,font=('arial',20,'bold'),bd=5)
    e_no.place(relx=.43,rely=.5)
    
    lbl_type = Label(frm,text='Type',font=('arial',20,'bold'),bg='lavender')
    lbl_type.place(relx=.3,rely=.6)
    
    cb_type = Combobox(frm,font=('arial',20,'bold'),values=['Saving','Current'])
    cb_type.current(0)
    cb_type.place(relx=.43,rely=.6)
    
    open_btn = Button(frm,font=('arial',20,'bold'),bd=6,text='Sign up',command=OpenAcnDB)
    open_btn.place(relx=.44,rely=.7)
    
    reset_btn = Button(frm,font=('arial',20,'bold'),bd=6,text='Reset',command=reset)
    reset_btn.place(relx=.55,rely=.7)

def fpscreen():
    frm=Frame(win)
    frm.configure(bg='lavender',border=True,borderwidth=5)
    frm.place(relx=0,rely=.15,relheight=.85,relwidth=1)

    def back():
        frm.destroy()
        mainscreen()

    def reset():
        e_acn.delete(0,"end")
        e_mail.delete(0,"end")
        e_no.delete(0,"end")
        e_acn.focus()

    def getpassDB():
        acn = e_acn.get()
        mail = e_mail.get()
        no = e_no.get()
        
        conobj = sqlite3.connect(database="Banking.sqlite")
        curobj = conobj.cursor()
        curobj.execute("select pass from accounts where acn=? and email=? and mob=?",(acn,mail,no))
        tup = curobj.fetchone()
        if tup==None:
            messagebox.showerror("Forget Password","Account Does not Exist!")
        else:
            messagebox.showinfo("Forget Password",f"{uname}, your Account Password : {tup[0]}")
        conobj.close()
        
        
    new_btn = Button(frm,font=('arial',20,'bold'),bd=5,text='Back',command=back)
    new_btn.place(relx=0,rely=0)

    lbl_acn = Label(frm,text='Account No.',font=('arial',20,'bold'),bg='lavender')
    lbl_acn.place(relx=.3,rely=.2)
    
    e_acn = Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.place(relx=.43,rely=.2)
    e_acn.focus()

    lbl_mail = Label(frm,text='Email',font=('arial',20,'bold'),bg='lavender')
    lbl_mail.place(relx=.3,rely=.3)
    
    e_mail = Entry(frm,font=('arial',20,'bold'),bd=5)
    e_mail.place(relx=.43,rely=.3)
    
    lbl_no = Label(frm,text='Phone No.',font=('arial',20,'bold'),bg='lavender')
    lbl_no.place(relx=.3,rely=.4)
    
    e_no = Entry(frm,font=('arial',20,'bold'),bd=5)
    e_no.place(relx=.43,rely=.4)

    getpass_btn = Button(frm,command=getpassDB,font=('arial',20,'bold'),bd=6,text='Get Password',bg='green',fg='white')
    getpass_btn.place(relx=.44,rely=.5,width=280,height=50)
    
    reset_btn = Button(frm,font=('arial',20,'bold'),bd=6,text='Reset',command=reset)
    reset_btn.place(relx=.55,rely=.6)

def loginscreen():
    frm=Frame(win)
    frm.configure(bg='lavender',border=True,borderwidth=5)
    frm.place(relx=0,rely=.15,relheight=.85,relwidth=1)

    def logout():
        frm.destroy()
        mainscreen()

    def details():
        ifrm=Frame(frm,highlightbackground='black', highlightthickness=3)
        ifrm.configure(bg='white')
        ifrm.place(relx=.25,rely=.15,relwidth=.7,relheight=.7)

        lbl = Label(ifrm,text=f'Hello {uname}, Review your Account Information',font=('arial',20,'bold'),bg='white',fg='gray')
        lbl.pack()

        conobj=sqlite3.connect(database="Banking.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select * from accounts where acn=?",(uacn,))
        tup=curobj.fetchone()
        conobj.close()

        lbl_acn = Label(ifrm,text=f"Account Number\t\t {tup[0]}",font=('arial',17,'bold'),bg='white')
        lbl_acn.place(relx=.2,rely=.3)

        lbl_bal = Label(ifrm,text=f"Account Balance\t\t {tup[6]}",font=('arial',17,'bold'),bg='white')
        lbl_bal.place(relx=.2,rely=.4)

        lbl_type = Label(ifrm,text=f"Account Type\t\t {tup[5]}",font=('arial',17,'bold'),bg='white')
        lbl_type.place(relx=.2,rely=.5)

        lbl_date = Label(ifrm,text=f"Account Open Date\t {tup[7]}",font=('arial',17,'bold'),bg='white')
        lbl_date.place(relx=.2,rely=.6)

    def profile():
        ifrm=Frame(frm,highlightbackground='black', highlightthickness=3)
        ifrm.configure(bg='white')
        ifrm.place(relx=.25,rely=.15,relwidth=.7,relheight=.7)

        lbl = Label(ifrm,text='Manage Your Profile, Ensure your Details are Up-to-Date',font=('arial',20,'bold'),bg='white',fg='gray')
        lbl.pack()

        def updateDB():
            name=e_name.get()
            pwd=e_pas.get()
            email=e_mail.get()
            mob=e_no.get()
            
            conobj=sqlite3.connect(database="Banking.sqlite")
            curobj=conobj.cursor()
            curobj.execute("update accounts set name=?,pass=?,email=?,mob=? where acn=?",(name,pwd,email,mob,uacn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Update Profile","Record Updated")
            global uname
            uname=name
            ifrm.destroy()
            loginscreen()

        lbl_name = Label(ifrm,text='Name',font=('arial',20,'bold'),bg='white')
        lbl_name.place(relx=.1,rely=.2)
        
        e_name = Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_name.place(relx=.1,rely=.29)
        
        lbl_pas = Label(ifrm,text='Password',font=('arial',20,'bold'),bg='white')
        lbl_pas.place(relx=.53,rely=.2)
        
        e_pas = Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_pas.place(relx=.53,rely=.29)
        
        lbl_mail = Label(ifrm,text='Email',font=('arial',20,'bold'),bg='white')
        lbl_mail.place(relx=.1,rely=.45)
    
        e_mail = Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_mail.place(relx=.1,rely=.53)
        
        lbl_no = Label(ifrm,text='Phone Number',font=('arial',20,'bold'),bg='white')
        lbl_no.place(relx=.53,rely=.45)
        
        e_no = Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_no.place(relx=.53,rely=.53)

        btn = Button(ifrm,font=('arial',18,'bold'),bd=6,text='Update Profile',command=updateDB)
        btn.place(relx=.64,rely=.69)

        conobj=sqlite3.connect(database="Banking.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select * from accounts where acn=?",(uacn,))
        tup=curobj.fetchone()
        conobj.close()

        e_name.insert(0,tup[1])
        e_pas.insert(0,tup[2])
        e_mail.insert(0,tup[3])
        e_no.insert(0,tup[4])

    def deposit():
        ifrm=Frame(frm,highlightbackground='black', highlightthickness=3)
        ifrm.configure(bg='white')
        ifrm.place(relx=.25,rely=.15,relwidth=.7,relheight=.7)

        def deposDB():
            amt = float(e_amt.get())
            conobj = sqlite3.connect(database="Banking.sqlite")
            curobj = conobj.cursor()
            curobj.execute("select bal from accounts where acn=?",(uacn,))
            bal=curobj.fetchone()[0]
            curobj.close()
            curobj = conobj.cursor()
            curobj.execute("update accounts set bal=bal+? where acn=?",(amt,uacn))
            curobj.execute("insert into txns values(?,?,?,?,?)",(uacn,amt,bal+amt,"Creadit",time.ctime()))
            conobj.commit()
            conobj.close()

            messagebox.showinfo("Deposit",f"Amount Credited, Updated Balance : {bal+amt}")
            
        lbl = Label(ifrm,text='Welcome to the Deposit Screen, Add Amount to your Account',font=('arial',20,'bold'),bg='white',fg='gray')
        lbl.pack()

        lbl_amt = Label(ifrm,text='Amount',font=('arial',20,'bold'),bg='white')
        lbl_amt.place(relx=.2,rely=.3)
        
        e_amt = Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=.35,rely=.3)
        e_amt.focus()

        btn = Button(ifrm,command=deposDB,font=('arial',18,'bold'),bd=6,text='Deposit')
        btn.place(relx=.53,rely=.45)

    def withdraw():
        ifrm=Frame(frm,highlightbackground='black', highlightthickness=3)
        ifrm.configure(bg='white')
        ifrm.place(relx=.25,rely=.15,relwidth=.7,relheight=.7)

        def withdrawDB():
            amt = float(e_amt.get())
            conobj = sqlite3.connect(database="Banking.sqlite")
            curobj = conobj.cursor()
            curobj.execute("select bal from accounts where acn=?",(uacn,))
            bal=curobj.fetchone()[0]
            curobj.close()
            if bal>=amt:
                curobj = conobj.cursor()
                curobj.execute("update accounts set bal=bal-? where acn=?",(amt,uacn))
                curobj.execute("insert into txns values(?,?,?,?,?)",(uacn,amt,bal-amt,"Debited",time.ctime()))
                conobj.commit()
                messagebox.showinfo("Withdraw",f"Amount Debited, Updated Balance : {bal-amt}")
            else:
                messagebox.showwarning("Withdraw",f"Insufficient Balance : {bal}")
            conobj.close()
        
        lbl = Label(ifrm,text='Welcome to the Withdraw Screen, Access your Cash Now',font=('arial',20,'bold'),bg='white',fg='gray')
        lbl.pack()
        
        lbl_amt = Label(ifrm,text='Amount',font=('arial',20,'bold'),bg='white')
        lbl_amt.place(relx=.2,rely=.3)
        
        e_amt = Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=.35,rely=.3)
        e_amt.focus()

        btn = Button(ifrm,command=withdrawDB,font=('arial',18,'bold'),bd=6,text='Withdraw')
        btn.place(relx=.51,rely=.45)

    def transfer():
        ifrm=Frame(frm,highlightbackground='black', highlightthickness=3)
        ifrm.configure(bg='white')
        ifrm.place(relx=.25,rely=.15,relwidth=.7,relheight=.7)\

        def trans():
            to = e_to.get()
            amt = float(e_amt.get())
            conobj = sqlite3.connect(database="Banking.sqlite")
            curobj = conobj.cursor()
            curobj.execute("select * from accounts where acn=?",(to,))
            tup=curobj.fetchone()
            curobj.close()
            if tup==None:
                messagebox.showerror("Transfer","Account does not Exist!")
            else:
                curobj = conobj.cursor()
                curobj.execute("select bal from accounts where acn=?",(uacn,))
                bal=curobj.fetchone()[0]
                if bal>=amt:
                    curobj = conobj.cursor()
                    curobj.execute("update accounts set bal=bal+? where acn=?",(amt,to))
                    curobj.execute("update accounts set bal=bal-? where acn=?",(amt,uacn))
                    curobj.execute("insert into txns values(?,?,?,?,?)",(to,amt,bal+amt,"Credit",time.ctime()))
                    curobj.execute("insert into txns values(?,?,?,?,?)",(uacn,amt,bal-amt,"Debit",time.ctime()))
                    conobj.commit()
                    conobj.close()
                    messagebox.showinfo("Transfer",f"Rs. {amt} is transfer to {to} Account Number.")
                else:
                    messagebox.showinfo("Transfer",f"Insufficient Balance : {bal}")
                
        lbl = Label(ifrm,text='Send Amount another Accounts, Transfer Funds Effortlessly',font=('arial',20,'bold'),bg='white',fg='gray')
        lbl.pack()

        lbl_to = Label(ifrm,text='To',font=('arial',20,'bold'),bg='white')
        lbl_to.place(relx=.2,rely=.3)
        
        e_to = Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_to.place(relx=.35,rely=.3)
        e_to.focus()

        lbl_amt = Label(ifrm,text='Amount',font=('arial',20,'bold'),bg='white')
        lbl_amt.place(relx=.2,rely=.45)
        
        e_amt = Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=.35,rely=.45)
        
        btn = Button(ifrm,font=('arial',18,'bold'),bd=6,text='Transfer',command=trans)
        btn.place(relx=.52,rely=.59)

    def history():
        ifrm=Frame(frm,highlightbackground='black', highlightthickness=3)
        ifrm.configure(bg='white')
        ifrm.place(relx=.25,rely=.15,relwidth=.7,relheight=.7)

        lbl = Label(ifrm,text='Transaction History, Review your Financial Activity',font=('arial',20,'bold'),bg='white',fg='gray')
        lbl.pack()
        
        tv = Treeview(ifrm)
        tv.place(x=100,y=100,height=200,width=800)

        style = Style()
        style.configure("Treeview.Heading",font=('arial',12,'bold'))

        sb = Scrollbar(ifrm,orient="vertical",command=tv.yview)
        sb.place(x=900,y=100,height=200)
        tv.configure(yscrollcommand=sb.set)
        
        tv['columns'] = ('date','amount','type','upbal')
        tv.column('date',width=250,anchor='c')
        tv.column('amount',width=150,anchor='c')
        tv.column('type',width=150,anchor='c')
        tv.column('upbal',width=150,anchor='c')

        tv.heading('date',text='Trans. Date')
        tv.heading('amount',text='Amount')
        tv.heading('type',text='Trans. Type')
        tv.heading('upbal',text='Updated Balance')

        tv['show'] = 'headings'

        conobj=sqlite3.connect(database="Banking.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select * from txns where acn=?",(uacn,))
        
        for row in curobj:
            tv.insert("",'end',values=(row[4],row[1],row[3],row[2]))
    
    logout_btn = Button(frm,command=logout,font=('arial',20,'bold'),bd=6,text='Sign Out')
    logout_btn.place(relx=.9,rely=.0)

    lbl_wel = Label(frm,text=f'Welcome {uname}, What can we do for you today? (please select an option)',font=('arial',20,'bold'),bg='lavender')
    lbl_wel.place(relx=.07,rely=.0)

    detail_btn = Button(frm,command=details,font=('arial',20,'bold'),bd=6,text='Details',width=15)
    detail_btn.place(relx=.0,rely=.15)

    prof_btn = Button(frm,command=profile,font=('arial',20,'bold'),bd=6,text='Update Profile',width=15)
    prof_btn.place(relx=.0,rely=.3)

    deposit_btn = Button(frm,command=deposit,font=('arial',20,'bold'),bd=6,text='Deposit',width=15)
    deposit_btn.place(relx=.0,rely=.45)

    withdraw_btn = Button(frm,command=withdraw,font=('arial',20,'bold'),bd=6,text='Withdraw',width=15)
    withdraw_btn.place(relx=.0,rely=.6)

    trans_btn = Button(frm,command=transfer,font=('arial',20,'bold'),bd=6,text='Transfer',width=15)
    trans_btn.place(relx=.0,rely=.75)

    his_btn = Button(frm,command=history,font=('arial',20,'bold'),bd=6,text='History',width=15)
    his_btn.place(relx=.0,rely=.89)

mainscreen()
win.mainloop()

