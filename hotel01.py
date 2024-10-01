#customer page
from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector
class Cust_window:
    def __init__(self,root):
      self.root=root
      self.root.title("Hotel Management System")
      self.root.geometry("1295x550+230+220")

      #variables
      self.var_ref=StringVar()
      x=random.randint(1000,9999)
      self.var_ref.set(x)


      self.var_cust_name=StringVar()
      self.var_mother=StringVar()
      self.var_gender=StringVar()
      self.var_post=StringVar()
      self.var_mobile=StringVar()
      self.var_email=StringVar()
      self.var_nationality=StringVar()
      self.var_address=StringVar()
      self.var_ID_proof=StringVar()
      self.var_ID_number=StringVar()








       #===============Title=================
      lbl_title=Label(self.root,text="Add Customer Details",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
      lbl_title.place(x=0,y=0,width=1295,height=50)

       #===============logo=================
      img2=Image.open("logo.jpg")
      img2=img2.resize((100,40),Image.ANTIALIAS)
      self.photoimg2 =ImageTk.PhotoImage(img2)

      lbimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
      lbimg.place(x=4,y=2,width=100,height=40)

      #=====================Lable frame==========
      lableframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",12,"bold"),pady=2)
      lableframeleft.place(x=5,y=50,width=425,height=450)


      #================lables and entries=================
      #Cust ref
      lbl_cust_ref=Label(lableframeleft,text="Customer ref",font=("ariel",12,"bold"),padx=2,pady=6)
      lbl_cust_ref.grid(row=0,column=0,sticky=W)

      entry_ref=ttk.Entry(lableframeleft,textvariable=self.var_ref,width=29,font=("times new roman",13,"bold"),state="readonly")
      entry_ref.grid(row=0,column=1)

      #custname
      cname=Label(lableframeleft,text="Customer Name",font=("ariel",12,"bold"),padx=2,pady=6)
      cname.grid(row=1,column=0,sticky=W)

      txtcname=ttk.Entry(lableframeleft,textvariable=self.var_cust_name,width=29,font=("times new roman",13,"bold"))
      txtcname.grid(row=1,column=1)

      #mothername
      lblmname=Label(lableframeleft,font=("ariel",12,"bold"),text="Mothername",padx=2,pady=6)
      lblmname.grid(row=2,column=0,sticky=W)

      txtmname=ttk.Entry(lableframeleft,textvariable=self.var_mother,width=29,font=("times new roman",13,"bold"))
      txtmname.grid(row=2,column=1)

      #gender combox
      label_gender=Label(lableframeleft,text="Gender",font=("ariel",12,"bold"),padx=2,pady=6)
      label_gender.grid(row=3,column=0,sticky=W)

      #txtgender=ttk.Entry(lableframeleft,width=29,font=("times new roman",13,"bold"))
      #txtgender.grid(row=3,column=1)
      
      combo_gender=ttk.Combobox(lableframeleft,textvariable=self.var_gender,font=("ariel",12,"bold"),width=27,state="readonly")
      combo_gender["value"]=("Male","Female","Other")
      combo_gender.current(0)
      combo_gender.grid(row=3,column=1)



      #postcode
      lblpostcode=Label(lableframeleft,text="PostCode",font=("ariel",12,"bold"),padx=2,pady=6)
      lblpostcode.grid(row=4,column=0,sticky=W)

      txtpostcode=ttk.Entry(lableframeleft,textvariable=self.var_post,width=29,font=("times new roman",13,"bold"))
      txtpostcode.grid(row=4,column=1)

      #mobileno.
      lblmobile=Label(lableframeleft,text="Mobile Number",font=("ariel",12,"bold"),padx=2,pady=6)
      lblmobile.grid(row=5,column=0,sticky=W)

      txtmobile=ttk.Entry(lableframeleft,textvariable=self.var_mobile,width=29,font=("times new roman",13,"bold"))
      txtmobile.grid(row=5,column=1)

      #email
      lblemail=Label(lableframeleft,text="Email",font=("ariel",12,"bold"),padx=2,pady=6)
      lblemail.grid(row=6,column=0,sticky=W)

      txtemail=ttk.Entry(lableframeleft,textvariable=self.var_email,width=29,font=("times new roman",13,"bold"))
      txtemail.grid(row=6,column=1)

      #nationality
      lblnationality=Label(lableframeleft,text="Nationality",font=("ariel",12,"bold"),padx=2,pady=6)
      lblnationality.grid(row=7,column=0,sticky=W)
      txtnationality=ttk.Entry(lableframeleft,textvariable=self.var_nationality,width=29,font=("times new roman",13,"bold"))
      txtnationality.grid(row=7,column=1)



      #idproof type combobox
      lblidproof=Label(lableframeleft,text="ID Proof Type",font=("ariel",12,"bold"),padx=2,pady=6)
      lblidproof.grid(row=8,column=0,sticky=W)
      txtidproof=ttk.Entry(lableframeleft,textvariable=self.var_ID_proof,width=29,font=("times new roman",13,"bold"))
      txtidproof.grid(row=8,column=1)

      

      #idnumber
      lblidnumber=Label(lableframeleft,text="Id Number",font=("ariel",12,"bold"),padx=2,pady=6)
      lblidnumber.grid(row=9,column=0,sticky=W)

      txtidnumber=ttk.Entry(lableframeleft,textvariable=self.var_ID_number,width=29,font=("times new roman",13,"bold"))
      txtidnumber.grid(row=9,column=1)

      #address
      lbladdress=Label(lableframeleft,text="Address",font=("ariel",12,"bold"),padx=2,pady=6)
      lbladdress.grid(row=10,column=0,sticky=W)

      txtaddress=ttk.Entry(lableframeleft,textvariable=self.var_address,width=29,font=("times new roman",13,"bold"))
      txtaddress.grid(row=10,column=1)
      #============button===========
      Btn_frame=Frame(lableframeleft,bd=2,relief=RIDGE)
      Btn_frame.place(x=0,y=400,width=412,height=40)

      btnAdd=Button(Btn_frame,text="Add",command=self.add_data,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
      btnAdd.grid(row=0,column=0,padx=1)

      btnUpdate=Button(Btn_frame,text="Update",command=self.update,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
      btnUpdate.grid(row=0,column=1,padx=1)
      
      btnDelete=Button(Btn_frame,text="Delete",command=self.mDelete,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
      btnDelete.grid(row=0,column=2,padx=1)
      
      btnReset=Button(Btn_frame,text="Reset",command=self.reset,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
      btnReset.grid(row=0,column=3,padx=1)


    
      #=======table frame search system=====
      table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",padx=2,font=("times new roman",12,"bold"),pady=2)
      table_frame.place(x=435,y=50,width=860,height=450)

      lblsearchby=Label(table_frame,text="Search By",font=("ariel",12,"bold"),bg="black",fg="white")
      lblsearchby.grid(row=0,column=0,sticky=W,padx=2)
      self.search_var=StringVar()
      combo_Search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("ariel",12,"bold"),width=27,state="readonly")
      combo_Search["value"]=("mobile","Ref")
      combo_Search.current(0)
      combo_Search.grid(row=0,column=1,padx=2)
      self.txt_search=StringVar()
      txtsearch=ttk.Entry(table_frame,textvariable=self.txt_search,width=24,font=("times new roman",13,"bold"))
      txtsearch.grid(row=0,column=2,padx=2)

      btnsearch=Button(table_frame,text="search",command=self.search,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
      btnsearch.grid(row=0,column=3,padx=1)

      btnshowall=Button(table_frame,text="Show All",command=self.fetch_data,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
      btnshowall.grid(row=0,column=4,padx=1)

      #=========show datatable=====
      details_table=Frame(table_frame,bd=2,relief=RIDGE)
      details_table.place(x=0,y=50,width=860,height=350)

      scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

      self.cust_details_table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile",
                                                                  "email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=RIGHT,fill=Y)
      scroll_x.config(command=self.cust_details_table.xview)
      scroll_y.config(command=self.cust_details_table.yview)

      self.cust_details_table.heading("ref",text="Refer No")
      self.cust_details_table.heading("name",text="Name")
      self.cust_details_table.heading("mother",text="Mother Name")
      self.cust_details_table.heading("gender",text="Gender")    
      self.cust_details_table.heading("post",text="PostCode")
      self.cust_details_table.heading("mobile",text="Mobile")
      self.cust_details_table.heading("email",text="Email")
      self.cust_details_table.heading("nationality",text="Nationality")
      self.cust_details_table.heading("idproof",text="Id Proof ")
      self.cust_details_table.heading("idnumber",text="Id Number")
      self.cust_details_table.heading("address",text="Address") 

      self.cust_details_table["show"]="headings"

      self.cust_details_table.column("ref",width=100)
     
      self.cust_details_table.column("name",width=100)
      self.cust_details_table.column("mother",width=100)
      self.cust_details_table.column("gender",width=100)    
      self.cust_details_table.column("post",width=100)
      self.cust_details_table.column("mobile",width=100)
      self.cust_details_table.column("email",width=100)
      self.cust_details_table.column("nationality",width=100)
      self.cust_details_table.column("idproof",width=100)
      self.cust_details_table.column("idnumber",width=100)
      self.cust_details_table.column("address",width=100) 



      self.cust_details_table.pack(fill=BOTH,expand=1)
      self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
      self.fetch_data()

    
    def add_data(self):
       if self.var_mobile.get()==""or self.var_mother.get()=="":
          messagebox.showerror("Error","all fields are required",parent=self.root)
       else:
          try:
              conn=mysql.connector.connect(host="localhost",username="root",password="vatsal",database="management")
              my_cursor=conn.cursor()
          
              my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_ref.get(),
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_ID_proof.get(),
                self.var_ID_number.get(),
                self.var_address.get()
                
              ))
              conn.commit()
              self.fetch_data()

              conn.close()
              messagebox.showinfo("success","customer has been added",parent=self.root)
          except Exception as es:
            messagebox.showwarning("warning",f"something went wrong{str(es)}",parent=self.root)

    def fetch_data(self):
       conn=mysql.connector.connect(host="localhost",username="root",password="vatsal",database="management")
       my_cursor=conn.cursor()
       my_cursor.execute("select * from customer")
       rows=my_cursor.fetchall()
       if len(rows)!=0:
          self.cust_details_table.delete(*self.cust_details_table.get_children())
          for i in rows:
             self.cust_details_table.insert("",END,values=i)
          conn.commit()
          conn.close()
    def get_cursor(self,event=""):
       cursor_row=self.cust_details_table.focus()
       content=self.cust_details_table.item(cursor_row)  
       row=content["values"]
       self.var_ref.set(row[0]),
       self.var_cust_name.set(row[1]),
       self.var_mother.set(row[2]),
       self.var_gender.set(row[3]),
       self.var_post.set(row[4]),
       self.var_mobile.set(row[5]),
       self.var_email.set(row[6]),
       self.var_nationality.set(row[7]),
       self.var_ID_proof.set(row[8]),
       self.var_ID_number.set(row[9]),
       self.var_address.set(row[10])
    def update(self):
       if self.var_mobile.get()=="":
          messagebox.showerror("error","please enter mobile number",parent=self.root)
       else:
          conn=mysql.connector.connect(host="localhost",username="root",password="vatsal",database="management")
          my_cursor=conn.cursor()
          my_cursor.execute("update customer set name=%s,mother=%s,gender=%s,postcode=%s,mobile=%s,email=%s,nationality=%s,IDproof=%s,IDnumber=%s,address=%s where Ref=%s ",(
             
             self.var_cust_name.get(),
             self.var_mother.get(),
             self.var_gender.get(),
             self.var_post.get(),
             self.var_mobile.get(),
             self.var_email.get(),
             self.var_nationality.get(),
             self.var_ID_proof.get(),
             self.var_ID_number.get(),
             self.var_address.get(),
             self.var_ref.get()
             
             
          ))
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("update","Customer details has been updated successfully",parent=self.root)
    def mDelete(self):
       mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
       if mDelete>0:
          conn=mysql.connector.connect(host="localhost",username="root",password="vatsal",database="management")
          my_cursor=conn.cursor()
          query="delete from customer where Ref=%s"
          value=(self.var_ref.get(),)
          my_cursor.execute(query,value)
       else:
          if not mDelete:
             return
          
       conn.commit()
       self.fetch_data()
   
       conn.close()
    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_nationality.set(""),
        self.var_ID_proof.set(""),
        self.var_ID_number.set(""),
        self.var_address.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(x)
    def search(self): 
       print("search button clicked") 
       conn=mysql.connector.connect(host="localhost",username="root",password="vatsal",database="management")
       my_cursor=conn.cursor()
       my_cursor.execute("select * from customer where"+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
       rows=my_cursor.fetchall()
       if len(rows)!=0:
          self.cust_details_table.delete(*self.cust_details_table.get_children())
          print("result showed")
          for i in rows:
             self.cust_details_table.insert("",END,values=i)

          conn.commit()   
       else:
          messagebox.showinfo("no result","no matchung record found",parent=self.root) 
       conn.close()  

          
              
       
       





      

        




       
          
          
      
       
           
  
      
      









       


      




      
      

      









if __name__=="__main__":
   root=Tk()
   obj=Cust_window(root)
   root.mainloop()
