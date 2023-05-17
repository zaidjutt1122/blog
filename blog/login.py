from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Sytem")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        #Image
        self.bg=ImageTk.PhotoImage(file="images/gm.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #Login Frame
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,width=500,height=340)

        title=Label(Frame_login,text="Login Here", font=("impact",35,"bold"),fg="dark orange",bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text="Accountant Employee Login Area", font=("Goudy old style",15,"bold"),fg="black",bg="white").place(x=90,y=100)
        
        lbl_email=Label(Frame_login,text="Enter your email", font=("goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_email=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=90,y=170,width=350,height=35)

        lbl_pass=Label(Frame_login,text="Password", font=("goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)


        forget_btn=Button(Frame_login,text="Register new Account?",command=self.register_window,cursor="hand2", bg="white",fg="dark orange",bd=0, font=("times new roman",12)).place(x=90,y=280)
        Login_btn=Button(self.root,command=self.login_function,cursor="hand2",text="Login", fg="white",bg="dark orange",font=("times new roman",20)).place(x=300,y=470,width=180,height=40)

    def register_window(self):
        self.root.destroy()
        import register


    def login_function(self):
        if self.txt_email.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","All Fields are required", parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
                cur=con.cursor()
                cur.execute("Select * from employee where email=%s and password=%s",(self.txt_email.get(),self.txt_pass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Email/Password", parent=self.root)

                else:
                    messagebox.showinfo("Success","Welcome", parent=self.root)
                    self.root.destroy()
                    import home
                    con.close()
            
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to:{str(es)}", parent=self.root)



        #elif self.txt_email.get()!="zaid" or self.txt_pass.get()!="123":
            #messagebox.showerror("Error","Invalid Email/Password", parent=self.root)
        #else:
            #messagebox.showinfo("Welcome",f"Welcome {self.txt_email.get()}\nYour Password: {self.txt_pass.get()}", parent=self.root)   


    

root = Tk()
obj = Login(root)
root.mainloop()