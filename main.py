import streamlit as st
from db_c import conn_obj ,cursor_obj

st.title("Media Platform")

# login,signup=st.tabs(
#                 ["Login","SignUp"]  
#                 )
if "user" not in st.session_state:
    st.session_state.user=None


def dashboard():
    st.sidebar.success("welcome user")
    option=st.sidebar.selectbox("choose:--"["uploadFiles","viewFiles","Logout"])
    st.header("dashboard")
    if option=="uploadFiles":
        st.header("upload your files here")
        choosedFile=st.file_uploader("choose file",type=["pdf","jpg","jpeg","mp3","mp4"])
        if choosedFile:
            st.write(choosedFile.name)
            st.write(choosedFile.type)
    
    
    

def login_function():
    st.header("Login")
    with st.form("Login_Form"):
        email=st.text_input("Email")
        password=st.text_input("Password",type="password")
        btn=st.form_submit_button("Login")
        if btn:
            query="select * from users3 where email=%s and password=%s"
            values=(email,password)
            cursor_obj.execute(query,values)
            loggedin_user=cursor_obj.fetchone()
            st.session_state.user=loggedin_user
            st.write("loggedin successfully")
            st.rerun()
       
     
        
def signup_function():
    st.header("SignUp")
    with st.form("SignUp_form"):
        name=st.text_input("Name")
        Email=st.text_input("Email")
        password=st.text_input("Password",type="password")
        btn=st.form_submit_button("SignUp")
        if btn:
            query="insert into users3(name,Email,password)values(%s,%s,%s)"
            values=(name,Email,password)
            cursor_obj.execute(query,values)
            conn_obj.commit()
            st.write("user added successfully ")
            
if st.session_state.user==None:
    login,signup=st.tabs(
                ["Login","SignUp"]  
                )
    with signup:
        signup_function()
    with login:
        login_function()    
         
    
else:
    dashboard()    
            
        
        
# cursor_obj.execute("show tables")
# dbs=cursor_obj.fetchall()
# for db in dbs:
#     st.write(db)