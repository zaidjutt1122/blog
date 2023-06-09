from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image,ImageTk
import pymysql

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registeration Window")
        self.root.geometry("1350x700+0+0")
        self.bg=ImageTk.PhotoImage(file="images/mg.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        self.root.config(bg="white")

        #left img
        self.left=ImageTk.PhotoImage(file="images/mgg.jpeg")
        left=Label(self.root,image=self.left,).place(x=80,y=100,width=400,height=500)
        
        title=Label(left,text="If you are Already register \n Please SignIn Here", font=("times new roman",20,"bold"), bg="white",fg="gray").place(x=120,y=190)
        

        #Register frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="Register Here", font=("times new roman",20,"bold"), bg="white",fg="green").place(x=50,y=30)
        #______Row1
        f_name=Label(frame1,text="First Name", font=("times new roman",15,"bold"), bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15), bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name", font=("times new roman",15,"bold"), bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15), bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        #______Row2
        contact=Label(frame1,text="Contact Number", font=("times new roman",15,"bold"), bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15), bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email", font=("times new roman",15,"bold"), bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15), bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)

        #______Row3
        question=Label(frame1,text="Security Question", font=("times new roman",15,"bold"), bg="white",fg="gray").place(x=50,y=240)
        self.cmd_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly', justify=CENTER)
        self.cmd_quest['values']=("Select","Your Favorite Colors","Your Birth Place","Your Best Friend")
        self.cmd_quest.place(x=50,y=270,width=250)
        self.cmd_quest.current(0)

        answer=Label(frame1,text="Answer", font=("times new roman",15,"bold"), bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15), bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)


        #______Row4
        password=Label(frame1,text="Password", font=("times new roman",15,"bold"), bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15), bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)

        cpassword=Label(frame1,text="Confirm Password", font=("times new roman",15,"bold"), bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15), bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)


        #____Terms
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree the Terms and Condition", variable=self.var_chk,onvalue=1,offvalue=0, bg="white", font=("times new roman",12)).place(x=50,y=380)

        self.btn=Button(frame1,text="Register", font=("times new roman",20),bd=0, bg="green", cursor="hand2", command=self.register_data)
        self.btn.place(x=50,y=420)

        btn_login=Button(self.root,text="Sign In",command=self.login_window,cursor="hand2",font=("times new roman",20),bd=0, bg="green").place(x=200,y=460,width=180)

    def login_window(self):
        self.root.destroy()
        import login


    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmd_quest.current(0)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmd_quest.get()=="select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields are Required", parent=self.root)
        
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Confirm Password does not match", parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our Terms and Condition", parent=self.root)

        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s",self.txt_email.get())
                row=cur.fetchone()

                if row!=None:
                    messagebox.showerror("Error","User already exit,Please try with another email", parent=self.root)

                else:
                    cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                            (self.txt_fname.get(),
                             self.txt_lname.get(),
                             self.txt_contact.get(),
                             self.txt_email.get(),
                             self.cmd_quest.get(),
                             self.txt_answer.get(),
                             self.txt_password.get()
                            ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Succesfully", parent=self.root)
                    self.clear()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}", parent=self.root)
            

root = Tk()

obj = Register(root)

root.mainloop()

        

