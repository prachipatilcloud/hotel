from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime

class RoomBooking:
   def __init__(self,root):
      self.root=root
      self.root.title("Hotel Management System")
      self.root.geometry("1295x550+230+220")

      #================Variables==================
      self.var_contact=StringVar()
      self.var_checkin=StringVar()
      self.var_checkout=StringVar()
      self.var_roomtype=StringVar()
      self.var_roomavailable=StringVar()
      self.var_meal=StringVar()
      self.var_noofdays=StringVar()
      self.var_paidtax=StringVar()
      self.var_actualtotal=StringVar()
      self.var_total=StringVar()


       #===============Title=================
      lbl_title=Label(self.root,text="ROOM BOOKING Details",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
      lbl_title.place(x=0,y=0,width=1295,height=50)

       #===============logo=================
      img2=Image.open("logo.jpg")
      img2=img2.resize((100,40),Image.ANTIALIAS)
      self.photoimg2 =ImageTk.PhotoImage(img2)

      lbimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
      lbimg.place(x=4,y=2,width=100,height=40)

      #=====================Lable frame==========
      lableframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOM BOOKING Details",padx=2,font=("times new roman",12,"bold"),pady=2)
      lableframeleft.place(x=5,y=50,width=425,height=450)

     #================lables and entries=================
      #Cust contact
      lbl_cust_contact=Label(lableframeleft,text="Customer Contact",font=("ariel",12,"bold"),padx=2,pady=6)
      lbl_cust_contact.grid(row=0,column=0,sticky=W)

      entry_contact=ttk.Entry(lableframeleft,textvariable=self.var_contact,font=("times new roman",13,"bold"),width=20)
      entry_contact.grid(row=0,column=1,sticky=W)

      #===============Fetch Data Button====================================
      btnFetchData=Button(lableframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
      btnFetchData.place(x=347,y=4)

      #Check_in_Date
      check_in_date=Label(lableframeleft,font=("arial",12,"bold"),text="Check_in Date:",padx=2,pady=6)
      check_in_date.grid(row=1,column=0,sticky=W)
      txtcheck_in_date=ttk.Entry(lableframeleft,textvariable=self.var_checkin,font=("arial",13,"bold"),width=29)
      txtcheck_in_date.grid(row=1,column=1)

      #Check out Date
      lbl_Check_out=Label(lableframeleft,font=("arial",12,"bold"),text="Check_out Date:",padx=2,pady=6)
      lbl_Check_out.grid(row=2,column=0,sticky=W)
      txt_Check_out=ttk.Entry(lableframeleft,textvariable=self.var_checkout,font=("arial",13,"bold"),width=29)
      txt_Check_out.grid(row=2,column=1)

      #Room type
      label_RoomType=Label(lableframeleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
      label_RoomType.grid(row=3,column=0,sticky=W)

      combo_RoomType=ttk.Combobox(lableframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
      combo_RoomType["value"]=("Single","Double","Luxury")
      combo_RoomType.current(0)
      combo_RoomType.grid(row=3,column=1)

      #Available Room
      lblRoomAvailable=Label(lableframeleft,font=("arial",12,"bold"),text="Available Room:",padx=2,pady=6)
      lblRoomAvailable.grid(row=4,column=0,sticky=W)
      txtRoomAvailable=ttk.Entry(lableframeleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=29)
      txtRoomAvailable.grid(row=4,column=1)

      #Meal
      lblMeal=Label(lableframeleft,font=("arial",12,"bold"),text="Meal:",padx=2,pady=6)
      lblMeal.grid(row=5,column=0,sticky=W)
      txtMeal=ttk.Entry(lableframeleft,textvariable=self.var_meal,font=("arial",13,"bold"),width=29)
      txtMeal.grid(row=5,column=1)

      #No. of Days
      lblNoOfDays=Label(lableframeleft,font=("arial",12,"bold"),text="No. Of Days:",padx=2,pady=6)
      lblNoOfDays.grid(row=6,column=0,sticky=W)
      txtNoOfDays=ttk.Entry(lableframeleft,textvariable=self.var_noofdays,font=("arial",13,"bold"),width=29)
      txtNoOfDays.grid(row=6,column=1)

      #Paid Tax
      lblNoOfDays=Label(lableframeleft,font=("arial",12,"bold"),text="Paid Tax:",padx=2,pady=6)
      lblNoOfDays.grid(row=7,column=0,sticky=W)
      txtNoOfDays=ttk.Entry(lableframeleft,textvariable=self.var_paidtax,font=("arial",13,"bold"),width=29)
      txtNoOfDays.grid(row=7,column=1)

      #Sub Total
      lblNoOfDays=Label(lableframeleft,font=("arial",12,"bold"),text="Sub Total:",padx=2,pady=6)
      lblNoOfDays.grid(row=8,column=0,sticky=W)
      txtNoOfDays=ttk.Entry(lableframeleft,textvariable=self.var_actualtotal,font=("arial",13,"bold"),width=29)
      txtNoOfDays.grid(row=8,column=1)

      #Total Cost
      lblIdNumber=Label(lableframeleft,font=("arial",12,"bold"),text="Total Cost:",padx=2,pady=6)
      lblIdNumber.grid(row=9,column=0,sticky=W)
      txtidNumber=ttk.Entry(lableframeleft,textvariable=self.var_actualtotal,font=("arial",13,"bold"),width=29)
      txtidNumber.grid(row=9,column=1)

      #=========Bill Button===============
      btnBill=Button(lableframeleft,text="Bill",font=("times new roman",10,"bold"),bg="black",fg="gold",width=10)
      btnBill.grid(row=10,column=0,padx=1,sticky=W)

      #=====================button==============================
      Btn_frame=Frame(lableframeleft,bd=2,relief=RIDGE)
      Btn_frame.place(x=0,y=400,width=412,height=40)

      btnAdd=Button(Btn_frame,text="Add",command=self.add_data,font=("times new roman",13,"bold"),bg="black",fg="gold",width=10)
      btnAdd.grid(row=0,column=0,padx=1)

      btnUpdate=Button(Btn_frame,text="Update",command=self.update,font=("times new roman",13,"bold"),bg="black",fg="gold",width=10)
      btnUpdate.grid(row=0,column=1,padx=1)
      
      btnDelete=Button(Btn_frame,text="Delete",command=self.mDelete,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
      btnDelete.grid(row=0,column=2,padx=1)
      
      btnReset=Button(Btn_frame,text="Reset",command=self.reset,font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
      btnReset.grid(row=0,column=3,padx=1)

      #============Right side Image=============
      img3=Image.open("bedroom.jpg")
      img3=img3.resize((520,300),Image.ANTIALIAS)
      self.photoimg3 =ImageTk.PhotoImage(img3)
      lbimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
      lbimg.place(x=760,y=55,width=520,height=200)

      #=======table frame search system=====
      table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",padx=2,font=("times new roman",12,"bold"),pady=2)
      table_frame.place(x=435,y=280,width=860,height=260)

      lblsearchby=Label(table_frame,text="Search By",font=("ariel",12,"bold"),bg="black",fg="white")
      lblsearchby.grid(row=0,column=0,sticky=W,padx=2)

      self.search_var=StringVar()
      combo_Search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("ariel",12,"bold"),width=27,state="readonly")
      combo_Search["value"]=("Contact","Room")
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
      details_table.place(x=0,y=50,width=860,height=180)

      scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

      self.room_table=ttk.Treeview(details_table,column=("contact","checkinDate","checkoutDate","roomtype","roomavailable","meal","noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=RIGHT,fill=Y)

      scroll_x.config(command=self.room_table.xview)
      scroll_y.config(command=self.room_table.yview)

      self.room_table.heading("contact",text="Contact")
      self.room_table.heading("checkinDate",text="Check-in")
      self.room_table.heading("checkoutDate",text="Check-out")
      self.room_table.heading("roomtype",text="Room Type")    
      self.room_table.heading("roomavailable",text="Room No")
      self.room_table.heading("meal",text="Meal")
      self.room_table.heading("noOfdays",text="NoOfdays")

      self.room_table["show"]="headings"

      self.room_table.column("contact",width=100)
      self.room_table.column("checkinDate",width=100)
      self.room_table.column("checkoutDate",width=100)
      self.room_table.column("roomtype",width=100)    
      self.room_table.column("roomavailable",width=100)
      self.room_table.column("meal",width=100)
      self.room_table.column("noOfdays",width=100)
      self.room_table.pack(fill=BOTH,expand=1)

      self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
      self.fetch_data()

  #-------------------add data---------------------------
   def add_data(self):
       if self.var_contact.get()==""or self.var_checkin.get()=="":
          messagebox.showerror("Error","all fields are required",parent=self.root)
       else:
          try:
              conn=mysql.connector.connect(host="localhost",user="root",password="Raunak@1305kalya",database="management")
              my_cursor=conn.cursor()
          
              my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                self.var_contact.get(),
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofdays.get()
                
              ))
              conn.commit()
              self.fetch_data()

              conn.close()
              messagebox.showinfo("success","Room Booked",parent=self.root)
          except Exception as es:
            messagebox.showwarning("warning",f"something went wrong{str(es)}",parent=self.root)
    
    #===================fetch data=====================
   def fetch_data(self):
       conn=mysql.connector.connect(host="localhost",user="root",password="Raunak@1305kalya",database="management")
       my_cursor=conn.cursor()
       my_cursor.execute("select * from room")
       rows=my_cursor.fetchall()
       if len(rows)!=0:
          self.room_table.delete(*self.room_table.get_children())
          for i in rows:
             self.room_table.insert("",END,values=i)
          conn.commit()
          conn.close()

#--------------get Cursor----------------------
   def get_cursor(self,event=""):
      cursor_row=self.room_table.focus()
      content=self.room_table.item(cursor_row)  
      row=content["values"]
      self.var_contact.set(row[0]),
      self.var_checkout.set(row[1]),
      self.var_checkin.set(row[2]),
      self.var_roomtype.set(row[3]),
      self.var_roomavailable.set(row[4]),
      self.var_meal.set(row[5]),
      self.var_noofdays.set(row[6])

#-------------update data--------------------
   def update(self):
       if self.var_contact.get()=="":
          messagebox.showerror("error","please enter mobile number",parent=self.root)
       else:
          conn=mysql.connector.connect(host="localhost",user="root",password="Raunak@1305kalya",database="management")
          my_cursor=conn.cursor()
          my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomAvailable=%s,meal=%s,noOfdays=%s where Contact=%s ",(
             
                                                                                                                                            self.var_checkin.get(),
                                                                                                                                            self.var_checkout.get(),
                                                                                                                                            self.var_roomtype.get(),
                                                                                                                                            self.var_roomavailable.get(),
                                                                                                                                            self.var_meal.get(),
                                                                                                                                            self.var_noofdays.get(),
                                                                                                                                            self.var_contact.get()
          

             
             
          ))
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("update","Room details has been updated successfully",parent=self.root)


    #------------Delete function-------------
   def mDelete(self):
       mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
       if mDelete>0:
          conn=mysql.connector.connect(host="localhost",user="root",password="Raunak@1305kalya",database="management")
          my_cursor=conn.cursor()
          query="delete from room where Contact=%s"
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
       else:
          if not mDelete:
             return
          
       conn.commit()
       self.fetch_data()
   
       conn.close()

    #------------reset function------------
   def reset(self):
      self.var_contact.set("")
      self.var_checkout.set("")
      self.var_checkin.set("")
      self.var_roomtype.set("")
      self.var_roomavailable.set("")
      self.var_meal.set("")
      self.var_noofdays.set("")
      self.var_paidtax.set("")
      self.var_actualtotal.set("")
      self.var_total.set("")


#===================All Data Fetch===================
   def Fetch_contact(self):
      if self.var_contact.get()=="":
        messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
      else:
        conn=mysql.connector.connect(host="localhost",user="root",password="Raunak@1305kalya",database="management")
        my_cursor=conn.cursor()
        query=("select Name from customer where Mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()

        if row==None:
          messagebox.showerror("Error","This number not found",parent=self.root)
        else:
          conn.commit()
          conn.close()

          showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
          showDataFrame.place(x=450,y=55,width=300,height=180)

          lblName=Label(showDataFrame,text="Name:",font=("arial",12,"bold"))
          lblName.place(x=0,y=0)

          lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
          lbl.place(x=90,y=0)

      #=================Gender=========================

        conn=mysql.connector.connect(host="localhost",user="root",password="Raunak@1305kalya",database="management")
        my_cursor=conn.cursor()
        query=("select Gender from customer where Mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()


        lblGender=Label(showDataFrame,text="Gender:",font=("arial",12,"bold"))
        lblGender.place(x=0,y=30)

        lbl2=Label(showDataFrame,text=row,font=("arial",12,"bold"))
        lbl2.place(x=90,y=30)

      #======================email========================

        conn=mysql.connector.connect(host="localhost",user="root",password="Raunak@1305kalya",database="management")
        my_cursor=conn.cursor()
        query=("select Email from customer where Mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
  
  
        lblEmail=Label(showDataFrame,text="Email:",font=("arial",12,"bold"))
        lblEmail.place(x=0,y=60)
        lbl3=Label(showDataFrame,text=row,font=("arial",12,"bold"))
        lbl3.place(x=90,y=60)
  
        #=====================Nationality==================
        conn=mysql.connector.connect(host="localhost",user="root",password="Raunak@1305kalya",database="management")
        my_cursor=conn.cursor()
        query=("select Nationality from customer where Mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
  
  
        lblNationality=Label(showDataFrame,text="Nationality:",font=("arial",12,"bold"))
        lblNationality.place(x=0,y=90)
        lbl4=Label(showDataFrame,text=row,font=("arial",12,"bold"))
        lbl4.place(x=90,y=90)
  
          #=====================Address==================
  
        conn=mysql.connector.connect(host="localhost",user="root",password="Raunak@1305kalya",database="management")
        my_cursor=conn.cursor()
        query=("select Address from customer where Mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
  
  
        lblAddress=Label(showDataFrame,text="Address:",font=("arial",12,"bold"))
        lblAddress.place(x=0,y=120)
        lbl5=Label(showDataFrame,text=row,font=("arial",12,"bold"))
        lbl5.place(x=90,y=120)

   #------------------search---------------------
   def search(self): 
       print("search button clicked") 
       conn=mysql.connector.connect(host="localhost",user="root",password="Raunak@1305kalya",database="management")
       my_cursor=conn.cursor()
       my_cursor.execute("select * from room where"+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
       rows=my_cursor.fetchall()
       if len(rows)!=0: 
          self.room_table.delete(*self.room_table.get_children())
          print("result showed")
          for i in rows:
             self.room_table.insert("",END,values=i)
          conn.commit()   
       else:
          messagebox.showinfo("no result","no matchung record found",parent=self.root) 
       conn.close()
    #------------
   def total(self):
      inDate=self.var_checkin.get()
      outDate=self.var_checkout.get()
      inDate=datetime.strptime(inDate,"%d/%m/%Y")
      outDate=datetime.strptime(outDate,"%d/%m/%Y")
      self.var_noofdays.set(abs(outDate-inDate).days)
      if(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="luxury"):
         q1=float(300)
         q2=float(700)
         q3=float(self.var_noofdays.get())
         q4=float(q1+q2)
         q5=float(q3+q4)
         Tax="Rs."+str("%.2f"%((q5)*0.1))
         ST="Rs."+str("%.2f"%((q5)))
         TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
         self.var_paidtax.set(Tax)
         self.var_actualtotal.set(ST)
         self.var_total.set(TT)
      elif(self.var_meal.get()=="LUNCH" and self.var_roomtype.get()=="Single"):
         q1=float(300)
         q2=float(700)
         q3=float(self.var_noofdays.get())
         q4=float(q1+q2)
         q5=float(q3+q4)
         Tax="Rs."+str("%.2f"%((q5)*0.1))
         ST="Rs."+str("%.2f"%((q5)))
         TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
         self.var_paidtax.set(Tax)
         self.var_actualtotal.set(ST)
         self.var_total.set(TT)



       




if __name__=="__main__":
   root=Tk()
   obj=RoomBooking(root)
   root.mainloop()