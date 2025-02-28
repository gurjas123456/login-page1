import streamlit as st
import time as t
import sqlite3
from streamlit_option_menu import option_menu

def connectdb():
    conn=sqlite3.connect("use mydb.db")
    return conn

def createTable():
    with connectdb() as conn:
        cur=conn.cursor()
        cur.execute("create table if not exists student(name text,password text,roll int primary key,branch text)")
        conn.commit()
# using sqlite3 
def addRecord(data):
    with connectdb() as conn:
        cur=conn.cursor()
        try:
            # execute use to write querys 
            cur.execute("insert into student(name,password,roll,branch) values(?,?,?,?)",data)
            # commit use to save the changes
            conn.commit()

        except sqlite3.IntegrityError:
            st.error("Student Already Registered :(")

def reset(r,newpass):
    with connectdb() as conn:
        cur=conn.cursor()
        cur.execute("update student set password = ? where roll = ? ",(newpass,r))
        conn.commit()
def delete():
    with connectdb() as conn:
        cur=conn.cursor()
        cur.execute("DELETE FROM student")
        conn.commit()

def display():
    with connectdb() as conn:
        # cursor pointout somthing
        cur=conn.cursor()
        cur.execute("select * from student")
        result=cur.fetchall()
        if st.button("Delete"):
            delete()
    return result

def signup():
    st.title("Registration Page")
    name=st.text_input("Name :")
    password=st.text_input("Password :",type='password')
    repassword=st.text_input("renter your password :",type='password')
    # roll=st.number_input("Roll No :",format="%0.0f")
    roll=st.number_input("Roll No :",min_value=1,max_value=100,step=1)
    branch=st.selectbox("Enter Branch",options=["CSE","AIML","CSIT","ECE","IT"])
    # age=st.text_input("Age :")
    if st.button('SignIn'):
        if password != repassword:
            st.warning("PASSWORD NOT MATCHING")
        else:
            addRecord((name,password,roll,branch))
            st.success("Student Registered !!!")

createTable()
with st.sidebar:
    selected=option_menu("My App",["Sign up","Display All Record","Reset Password"])

if selected == "Sign up":
    signup()
elif selected=="Display All Record":
    data=display()
    st.table(data)
else:
    st.write(" Reset Your Password ")
    newpass=st.text_input("New Password",type="password")
    r=st.number_input("Enter roll no",format="%0.0f")
    if st.button("Reset"):
        if newpass and r :
            reset(r,newpass)
            with st.spinner("just wait"):
                t.sleep(3)
                st.success(" Password reset Succesfully ")
        else:
            st.error("Enter both password and roll no")

# create a menu for reset password which will take a roll number as a input -> it will reset passwrod accroding to the roll number 
# create a filter to filter the student record on the basis of branch 
# search option on the basis of roll number 
# delete student record