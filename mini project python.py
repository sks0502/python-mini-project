# import modules

from tkinter import *
from tkinter import Text, Tk
import os

# Designing window for registration

def register():
    
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("register ")
    register_screen.geometry("300x300")

    global username
    global password
    
    global username_entry
    global password_entry
    
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="").pack()
    
    username_lable = Label(register_screen, text="Username",font=("Calibri", 13))
    username_lable.pack()
    
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    
    password_lable = Label(register_screen, text="Password",font=("Calibri", 13))
    password_lable.pack()
    
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command = register_user).pack()


# Designing window for login 


def login():

    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("login " )
    login_screen.geometry("300x250")
    
    Label(login_screen, text="LOGIN",bg = "light green", width="300", height="2", font=("Calibri", 13,"bold")).pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username",font=("Calibri", 13)).pack()
    
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password",font=("Calibri", 13,)).pack()
    
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

# Implementing event on register button

def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    Button(register_screen, text="login", width=10, height=1, command = login ).pack()

# Implementing event on login button

def login_verify():
    
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()
        
# Designing popup for login success

def login_sucess():
    
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("login screen")
    login_success_screen.geometry("150x100")
    
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK",width=10, height=1, command=main_window).pack()

# Designing popup for login invalid password

def password_not_recognised():
    
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("password not recognised")
    password_not_recog_screen.geometry("150x100")
    
    Label(password_not_recog_screen, text="Invalid Password ",fg="red",font=("arial", 10)).pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found

def user_not_found():
    
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("User not found")
    user_not_found_screen.geometry("150x100")
    
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()

# main window 2

def main_window():
    
    global main_window_screen
    main_window_screen = Toplevel(main_screen)
    main_window_screen.title("hospital management")
    main_window_screen.geometry("400x250")
    
    Label(main_window_screen, text="Welcome to Hospital Management",bg="light blue", width="300", height="2", font=("Calibri", 16,"bold")).pack()
    
    Label(main_window_screen, text="").pack() 
    Button(main_window_screen,text=" personal record ",height="2", width="30",  command= personal_record).pack()
    
    Label(main_window_screen, text="").pack() 
    Button(main_window_screen,text=" medical record ",height="2", width="30", command= medical_record).pack()

    Label(main_window_screen, text="").pack() 
    Button(main_window_screen,text=" Exit ", width=10, height=1, command= login).pack()
    
def delete_main_window():    
    main_window_screen.destroy()

# medical record

def medical_record():
    
    global medical_record_screen
    medical_record_screen = Toplevel(main_screen)
    medical_record_screen.title("medical record")
    medical_record_screen.geometry("400x250")
    
    Label(medical_record_screen, text="Medical Record" ,bg="light blue", width="300", height="2", font=("Calibri", 16,"bold")).pack()
    
    Label(medical_record_screen, text="").pack() 
    Button(medical_record_screen,text=" Present record ", height="2", width="30", command= present_record).pack()
    
    Label(medical_record_screen, text="").pack() 
    Button(medical_record_screen,text=" Past record ", height="2", width="30", command= past_record).pack()
    
    Label(medical_record_screen, text="").pack()      
    Button(medical_record_screen, text="Back", width=10, height=1, bg="YELLOW", command = delete_medical_record_screen).pack()
    


# personal record

def personal_record():
    
    global personal_record_screen
    personal_record_screen = Toplevel(main_screen)
    personal_record_screen.title("personal")
    personal_record_screen.geometry("400x250")
    
    Label(personal_record_screen, text="Personal Record",bg="light blue", width="300", height="2", font=("Calibri", 16,"bold")).pack()
    
    Label(personal_record_screen, text="").pack() 
    Button(personal_record_screen,text=" General Details ", height="2", width="30", command= general).pack()
    
    Label(personal_record_screen, text="").pack() 
    Button(personal_record_screen,text=" Payment Details ", height="2", width="30", command= payment).pack()
    
    Label(personal_record_screen, text="").pack()      
    Button(personal_record_screen, text="Back", width=10, height=1, bg="YELLOW", command = delete_personal_record_screen).pack()

def delete_personal_record_screen():
    personal_record_screen.destroy()

# present record

def present_record():
    
    global present_record_screen
    present_record_screen = Toplevel(main_screen)
    present_record_screen.title("present recod")
    present_record_screen.geometry("300x250")


    Label(present_record_screen, text="Present Record",  bg="light blue", width="300", height="2", font=("Calibri", 16,"bold")).pack()
    Label(present_record_screen, text="").pack()
    Button(present_record_screen,text=" Physical Examination ", height="2", width="30", command= physical_examination).pack()
    


    Label(present_record_screen, text="").pack()
    Button(present_record_screen,text="  Report ", height="2", width="30", command= recovery_report).pack()
    
    Label(present_record_screen, text="").pack()
    Button(present_record_screen,text=" Back ", width=10, height=1, command=delete_present_record ).pack()

# past record

def past_record():
    
    global past_record_screen
    past_record_screen = Toplevel(main_screen)
    past_record_screen.title("past record")
    past_record_screen.geometry("300x250")

    global record 
    
    global record_entry
    
    record = StringVar()
    
    Label(past_record_screen, text="Past Record", bg="light blue", width="300", height="2", font=("Calibri", 16,"bold") ).pack()
    Label(past_record_screen, text="").pack()
       

    Label(past_record_screen, text="Please enter details below", bg="green").pack()
    Label(past_record_screen, text="if available").pack()
    
    record_lable = Label( past_record_screen, text="photo or sacn of document")
    record_lable.pack()
    
    record_entry = Entry( past_record_screen, textvariable=record  )
    record_entry.pack()
    
    Label(past_record_screen, text="").pack()
    Button(past_record_screen, text="Save", width=10, height=1, bg="YELLOW", command = delete_past_record_screen).pack()

# present record

def present_record():
    
    global present_record_screen
    present_record_screen = Toplevel(main_screen)
    present_record_screen.title("present record")
    present_record_screen.geometry("300x250")
    
    Label(present_record_screen, text="Present Record", bg="light blue", width="300", height="2", font=("Calibri", 16,"bold")).pack()
    
    Label(present_record_screen, text="").pack()
    Button(present_record_screen,text=" Physical Examination ", height="2", width="30", command= physical_examination).pack()
    
    Label(present_record_screen, text="").pack()
    Button(present_record_screen,text=" Report ", height="2", width="30", command= recovery_report).pack()
    
    Label(present_record_screen, text="").pack()
    Button(present_record_screen,text=" Back ", width=10, height=1, command=delete_present_record ).pack()

# physical examination
    
def physical_examination():
    
    global physical_examination_screen
    physical_examination_screen = Toplevel(main_screen)
    physical_examination_screen.title("physical examination")
    physical_examination_screen.geometry("300x250")

    global name
    global caste
    global age
    global gender
    
    global name_entry
    global caste_entry
    global age_entry
    global gender_entry

    
    name = StringVar()
    caste = StringVar()
    age = StringVar()
    gender = StringVar()
    
    

    Label(physical_examination_screen, text="Physical Examination", bg="light blue", width="300", height="2", font=("Calibri", 16,"bold")).pack()
    Label(physical_examination_screen, text="").pack()
    
    name_lable = Label(physical_examination_screen, text=" Patient Name ")
    name_lable.pack()
    
    name_entry = Entry(physical_examination_screen, textvariable=name )
    name_entry.pack()
    
    
    pulse = IntVar()
    Checkbutton(physical_examination_screen, text="Pulse Rate    ", variable=pulse ).pack()
    
    
    bp    = IntVar()
    Checkbutton(physical_examination_screen, text=" Blood Pressure", variable=bp).pack()
    
    
    sugar = IntVar()
    Checkbutton(physical_examination_screen, text="  Sugar         ", variable=sugar).pack()
    
    Label(physical_examination_screen, text="").pack()
    Button(physical_examination_screen, text="Submit", width=10, height=1, bg="YELLOW", command = delete_physical_examination_screen).pack()

# recovery report

def recovery_report():
    
    global recovery_report_screen
    recovery_report_screen = Toplevel(main_screen)
    recovery_report_screen.title("recovery report")
    recovery_report_screen.geometry("400x500")

    global record 
    
    global record_Text
    
    record = StringVar()
    

    Label(recovery_report_screen, text="Report", bg="light blue", width="300", height="2", font=("Calibri", 16,"bold")).pack()
    
    Label(recovery_report_screen, text="").pack()
    record_lable = Label( recovery_report_screen, text="recovery report/Feedback")
    record_lable.pack()
    
    record_Text = Text( recovery_report_screen,height=20, width=40  )
    record_Text.pack()
    
    Label(recovery_report_screen, text="").pack()
    Button(recovery_report_screen, text="Submit", width=10, height=1, bg="YELLOW", command =delete_recovery_report_screen).pack()

# deleting pops

def delete_present_record():
    present_record_screen.destroy()

def delete_recovery_report_screen():
    recovery_report_screen.destroy()
    
def delete_physical_examination_screen():
    physical_examination_screen.destroy()

def delete_past_record_screen():
    past_record_screen.destroy()    
    
def delete_present_record_screen():
    present_record_screen.destroy()    
    

# general details

def general():
    
    global general_screen
    general_screen = Toplevel(main_screen)
    general_screen.title("general")
    general_screen.geometry("300x350")

    global name
    global caste
    global age
    global gender
    global social
    
    global name_entry
    global caste_entry
    global age_entry
    global gender_entry
    global social_entry
    
    name = StringVar()
    caste = StringVar()
    age = StringVar()
    gender = StringVar()
    social  = StringVar()
    

    Label(general_screen, text="General Details",bg="light blue", width="300", height="2", font=("Calibri", 16,"bold") ).pack()
    Label(general_screen, text="").pack()
    
    name_lable = Label(general_screen, text="Name ")
    name_lable.pack()
    name_entry = Entry(general_screen, textvariable=name )
    name_entry.pack()
    
    caste_lable = Label(general_screen, text=" Caste")
    caste_lable.pack()
    caste_entry = Entry(general_screen, textvariable=caste)
    caste_entry.pack()
    
    age_lable = Label(general_screen, text="Age  ")
    age_lable.pack()
    age_entry = Entry(general_screen, textvariable=age)
    age_entry.pack()
    
    gender_lable = Label(general_screen, text="Gender(Male/Female)")
    gender_lable.pack()
    gender_entry = Entry(general_screen, textvariable=gender)
    gender_entry.pack()
    
    social_lable = Label(general_screen, text="social contact(if any)")
    social_lable.pack()
    social_entry = Entry(general_screen, textvariable=social)
    social_entry.pack()
    
    Label(general_screen, text="").pack()
    Button(general_screen, text="save", width=10, height=1, bg="YELLOW", command = delete_general_screen).pack()

# payment details

def payment():
    
    global payment_screen
    payment_screen = Toplevel(main_screen)
    payment_screen.title("payment")
    payment_screen.geometry("300x250")

    global cheque 
    global cash
    
    global cheque_entry
    global cash_entry
    
    cheque  = StringVar()
    cash  = StringVar()

    Label(payment_screen, text="Payment",bg="light blue", width="300", height="2", font=("Calibri", 16,"bold")).pack()
    Label(payment_screen, text="").pack()
    
    var1 = IntVar()
    Checkbutton(payment_screen, text="cheque no.", variable=var1).pack()
    
    var2 = IntVar()
    cheque_entry = Entry( payment_screen, textvariable=cheque  )
    cheque_entry.pack()
    
    Label(payment_screen, text="").pack()
    Checkbutton(payment_screen, text="cash amount", variable=var2).pack()
    
    cash_entry = Entry( payment_screen, textvariable=cash )
    cash_entry.pack()
    
    Label(payment_screen, text="").pack()
    Button(payment_screen, text="save", width=10, height=1, bg="YELLOW", command = delete_payment_screen).pack()

# deleting the record

def delete_general_screen():
    general_screen.destroy()

def delete_payment_screen():
    payment_screen.destroy()    
   
          
def delete_personal_record_screen():
    personal_record_screen.destroy()
          
def delete_medical_record_screen():
    medical_record_screen.destroy()
          
def delete_recovery_report_screen():
    recovery_report_screen.destroy()
    
def delete_physical_examination_screen():
    physical_examination_screen.destroy()

def delete_past_record_screen():
    past_record_screen.destroy()

# main login window
def main_account_screen():
    
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x300")
    main_screen.title("login window")
    
    Label(text="HOSPITAL MANGEMENT", bg="light blue", width="300", height="2", font=("Calibri", 16,"bold")).pack()
    Label(main_screen, text="").pack()
    Label(text="Already have a account ?",fg="red",font=("arial", 10)).pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(main_screen, text="").pack()
    Label(text="Register for create a new account",fg="red",font=("arial", 10)).pack()
    Button(text="Register", height="2", width="30", command=register).pack()

#closing modules
    
    main_screen.mainloop()

# closing  main window

main_account_screen()
    
    

