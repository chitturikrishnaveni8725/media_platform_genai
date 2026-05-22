import mysql.connector
import streamlit as st

conn_obj=mysql.connector.connect(
    host=st.secrets["host"],
    database=st.secrets["database"],
    port=st.secrets["port"],
    user=st.secrets["user"],
    password=st.secrets["password"]   
)

cursor_obj=conn_obj.cursor(dictionary=True)


cursor_obj.execute("""
               create table if not exists  users3(
                   id int primary key auto_increment,
                   name varchar(50) not null,
                   email varchar(50) unique,
                   password varchar(50) not null
               )
               
               """)


cursor_obj.execute("""
               create table if not exists files3(
                   id int primary key auto_increment,
                   user_id int,
                   file_name varchar(255),
                   file_type varchar(100),
                   file_url text,
                   upload_date timestamp default current_timestamp,
                   foreign key(user_id) references users3(id)
               )
               
               """)


conn_obj.commit()
print("Tables created successfully")